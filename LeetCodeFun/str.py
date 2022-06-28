# python3.10

class StrSolution:
    '''把字符串转换成Z型字符后再输出'''
    def convert(self, s: str, numRows: int) -> str:
        '''
        # todo
            1.直接拼接
        '''
        doing = 1
        if doing == 1:
            __len = len(s)
            # 单列或不足一列直接返回
            if __len <= numRows or numRows == 1:
                return s

            # 构建每行存于list中
            r = []
            for i in range(numRows):
                r.append('')

            # 上下不断刷入字符到每行
            p = index = 0
            isUp = False
            while index >= 0 and index < __len:
                if isUp == False:
                    r[p] += s[index]
                    p += 1
                    if p == numRows - 1:
                        isUp = True
                elif isUp == True:
                    r[p] += s[index]
                    p -= 1
                    if p == 0:
                        isUp = False
                index += 1
                print(str(r))

            # 组合输出
            s = ''
            for i in range(numRows):
                s += r[i]
            return s

        return None

# e = StrSolution()
# print(e.convert('AB', 1))
