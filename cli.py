import os
from pathlib import Path
from urllib.parse import urlparse

import fire
from gql import Client
from gql import gql
from gql.transport.aiohttp import AIOHTTPTransport
from markdownify import markdownify as md

# CLI
# 1. Inputs:
#   - Get a LeetCode problem's URL
#       example: https://leetcode.com/problems/report-spam-message/description/
#   - Get problem's category
#       example: binary_search
# 1.a create a directory for the problem's category if it doesn't exists.
# 2. From the URL extract the 3rd component, the titleSlug.
# 3. Query the graphql API with the tittleSlug to extract the problem's id.
# 4. Query the graphql API with the tittleSlug to extract the problem's content.
# 5. Create a directory with the following format.
#   - `id`_`title`, title can't contain whitespaces, only underscores, and it needs to be lower case.
# 6. Create a README file called problem.md within the directory created using the following format.
#   # `id`. `title`, title needs to be capitalize and with withespaces.
#
#   Link: [url]
#
#   ## Description
#   content
#
#   ## Solution
#   [![Python](https://img.shields.io/badge/-Python-black?style=for-the-badge&logo=python)](./solution.py)
# 7. Create a file called solution.py within the directory created.


def main(url: str):
    """_summary_

    Args:
        url (str): _description_
    """

    category = input("Please insert the category of the problem: ")

    current_dir = os.path.dirname(__file__)
    category_dir = os.path.join(current_dir, category)
    Path(category_dir).mkdir(exist_ok=True)

    title_slug = urlparse(url).path.split("/")[2]

    transport = AIOHTTPTransport(url="https://leetcode.com/graphql")
    client = Client(transport=transport, fetch_schema_from_transport=False)

    title_query = gql(
        """
        query questionTitle($titleSlug: String!){
            question(titleSlug: $titleSlug){
                questionId
                title
            }
        }
        """,
    )

    result = client.execute(
        title_query,
        variable_values={"titleSlug": title_slug},
        operation_name="questionTitle",
    )
    problem_id = result["question"]["questionId"]
    problem_title = result["question"]["title"]

    content_query = gql(
        """
        query questionContent($titleSlug: String!){
            question(titleSlug: $titleSlug){
                content
            }
        }
        """,
    )
    result = client.execute(
        content_query,
        variable_values={"titleSlug": title_slug},
        operation_name="questionContent",
    )
    problem_content = result["question"]["content"]

    problem_dir = os.path.join(category_dir, f"{problem_id}_{problem_title.replace(' ', '_').lower()}")
    Path(problem_dir).mkdir(exist_ok=True)

    problem_description_file_path = os.path.join(problem_dir, "description.md")
    Path(problem_description_file_path).touch()

    with open(problem_description_file_path, mode="w", encoding="utf-8") as f:
        f.write(
            "\n".join(
                [
                    f"# {problem_id}. {problem_title}\n",
                    f"Link: [{problem_id}. {problem_title}]({url})\n",
                    "## Description\n",
                    f"{md(problem_content)}",
                    "## Solution\n",
                    "[![Python](https://img.shields.io/badge/-Python-black?style=for-the-badge&logo=python)](./solution.py)\n",
                ],
            ),
        )
    problem_solution_file_path = os.path.join(problem_dir, "solution.py")
    Path(problem_solution_file_path).touch(exist_ok=True)


if __name__ == "__main__":
    fire.Fire(main)
