# 输入是query和 key-value，注意力机制首先计算query与每个key的关联性（compatibility），
# 每个关联性作为每个value的权重（weight），各个权重与value的乘积相加得到输出
class ScaledDotProductAttention(nn.Module):
    # Attention(Q, K, V) = softmax(QKT/sqrt(dk))*V 
    def __init__(self, scale):
        self.scale = scale
        self.softmax = nn.Softmax(dim = 2)

    def forward(self, q, k, v, mask = None):
      #  matmul would be the more flexible op allowing for inputs using different shapes and would broadcast the tensors if needed. 
      #  bmm(batch matrix multiply) expects two 3D tensors and will not broadcast them as noted in the docs.
        u = torch.bmm(q, k.transpose(1,2)) # 1. Matmul #k.transpose()
        u = u/self.scale
        
        if mask:
            u = u.masked_fill(mask, -np.inf) #masked_fill(mask, value) 类似fillna
            
        attn = self.softmax(u)
        res = torch.bmm(attn, v)
        return res
    
    