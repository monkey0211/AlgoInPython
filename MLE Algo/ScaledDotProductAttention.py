# 输入是query和 key-value，注意力机制首先计算query与每个key的关联性（compatibility），
# 每个关联性作为每个value的权重（weight），各个权重与value的乘积相加得到输出
import numpy as np
import torch
from torch import nn
class ScaledDotProductAttention(nn.Module):
    # Attention(Q, K, V) = softmax(QKT/sqrt(dk))*V 
    def __init__(self, scale):
        super().__init__()
        self.scale = scale
        self.softmax = nn.Softmax(dim = 2)

    def forward(self, q, k, v, mask = None):
      #  matmul would be the more flexible op allowing for inputs using different shapes and would broadcast the tensors if needed. 
      #  bmm(batch matrix multiply) expects two 3D tensors and will not broadcast them as noted in the docs.
        u = torch.bmm(q, k.transpose(1,2)) # 1. Matmul #k.transpose()
        u = u/self.scale
        
        if mask:
            u = u.masked_fill(mask, -np.inf) #masked_fill(mask, value) 类似fillna
            
        attn = self.softmax(u) #this is attention score
        res = torch.bmm(attn, v) #res = atten * V
        return attn, res
    
#Test
if __name__ == "__main__":
    q1, k1, v1 = 2,4,4
    d_q, d_k, v2 = 128, 128, 64
    q = torch.randn(batch, q1, d_q)
    k = torch.randn(batch, k1, d_k)
    v = torch.randn(batch, v1, v2)
    mask = torch.zeros(batch, q1, k1).bool() #matrix of q1 x k1
    
    attention = ScaledDotProductAttention(scale = np.power(d_k, 0.5))
    attn, res = attention(q, k, v, mask = mask)
    
