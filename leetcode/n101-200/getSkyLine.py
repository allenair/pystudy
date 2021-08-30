class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(buildings) == 0:
            return []

        res_list = [[buildings[0][0], buildings[0][2]]]
        max_x = buildings[0][1]
        now_hight = buildings[0][2]

        for index in range(1, len(buildings)):
            build = buildings[index]
            if build[0] > max_x:
                max_x = build[1]
                now_hight = build[2]
                res_list.append([max_x, 0])
                res_list.append([build[0], now_hight])
            elif build[0] <= max_x < build[1]:
                max_x = build[1]
                if build[2] > now_hight:
                    now_hight = build[2]
                res_list.append([build[0], now_hight])
            else:
                if build[2] > now_hight:
                    now_hight = build[2]
                res_list.append([build[0], now_hight])

        res_list.append([max_x, 0])
        return res_list


app = Solution()
print(app.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))


# [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
