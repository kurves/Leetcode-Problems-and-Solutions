def generate(numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for i in range(numRows):
            row = [i] * (i +1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j -1] + triangle[i -1][j]
            triangle.append(row)

        return triangle

