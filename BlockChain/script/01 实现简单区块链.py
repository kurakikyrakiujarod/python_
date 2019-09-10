import hashlib
import datetime


class DaDaBlockCoin:  # 电子货币 达达币
    def __init__(self,
                 index,  # 索引
                 timestamp,  # 交易时间
                 data,  # 交易记录
                 next_hash):  # 下一个哈希
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.nexthash = next_hash
        self.selfhash = self.hash_DaDaBlockCoin()

    def hash_DaDaBlockCoin(self):
        sha = hashlib.sha256()
        datastr = str(self.index) + str(self.timestamp) + str(self.data) + str(self.nexthash)
        sha.update(datastr.encode("utf-8"))
        return sha.hexdigest()


def create_first_DadaBlock():  # 创世区块链
    return DaDaBlockCoin(0, datetime.datetime.now(), "love Dada", "0")


def create_money_DadaBlock(last_block):  # 创世区块链的其他块，参数就是上一个区块
    this_index = last_block.index + 1  # 索引加1
    this_timestamp = datetime.datetime.now()  # 当前时间
    this_data = "love Dada" + str(this_index)  # 模拟交易数据
    this_hash = last_block.selfhash  # 取得上一块的哈希
    return DaDaBlockCoin(this_index,
                         this_timestamp,
                         this_data,
                         this_hash)


DaDaBlockCoins = [create_first_DadaBlock()]  # 区块链列表
nums = 100
head_block = DaDaBlockCoins[0]
print(head_block.index,
      head_block.timestamp,
      head_block.selfhash,
      head_block.nexthash)
for i in range(100):
    dadaBlock_add = create_money_DadaBlock(head_block)  # 创建一个区块链的节点
    DaDaBlockCoins.append(dadaBlock_add)
    head_block = dadaBlock_add
    print(dadaBlock_add.index,
          dadaBlock_add.timestamp,
          dadaBlock_add.selfhash,
          dadaBlock_add.nexthash)
