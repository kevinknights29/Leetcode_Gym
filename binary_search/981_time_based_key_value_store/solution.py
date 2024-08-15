class TimeMap:
    def __init__(self):
        self._hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._hashmap[key] = self._hashmap.get(key, [])
        self._hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        _pairs = self._hashmap.get(key, [])
        result = ""

        # no values to return / search
        if len(_pairs) == 0 or timestamp < _pairs[0][1]:
            return result

        # search based on timestamp
        L = 0
        R = len(_pairs) - 1
        while L <= R:
            mid = L + R  # 2
            # matching timestamp
            if _pairs[mid][1] == timestamp:
                return _pairs[mid][0]
            # search previous timestamps
            if _pairs[mid][1] > timestamp:
                # the left side is closer
                R = mid - 1
            else:
                # the right side is closer
                # update result with the closest value seen so far
                #   matching timestamp_prev <= timestamp
                result = _pairs[mid][0]
                L = mid + 1
        # end of search
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

if __name__ == "__main__":
    # Test Cases
    time_map = TimeMap()
    time_map.set("foo", "bar", 1)  # store the key "foo" and value "bar" along with timestamp = 1.
    assert time_map.get("foo", 1) == "bar"
    assert (
        time_map.get("foo", 3) == "bar"
    )  # since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
    time_map.set("foo", "bar2", 4)  # store the key "foo" and value "bar2" along with timestamp = 4.
    assert time_map.get("foo", 4) == "bar2"
    assert time_map.get("foo", 5) == "bar2"

    print("All passed!")
