import numpy as np
#WIP
class MultiHeadAttention(nn.Module):
    def __init__(self, n_head, d_k, d_v, d_k_, d_v_, d_o):
        super().__init__() #remove?
        self.n_head = n_head
        self.d_k = d_k
        self.d_v = d_v
        
        #nn. Linear(n,m) is a module that creates single layer feed forward network with n inputs and m output.
        self.fc_q = nn.Linear(d_k_, n_head * d_k)
        self.fc_k = nn.Linear(d_k_, n_head * d_k)
        self.fc_v = nn.Linear(d_v_, n_head * d_v)
        
        self.attention = ScaleDotProductAttention(scale = np.power(d_k, 0.5))
        
        self.fc_o = nn.Linear(n_head * d_v, d_o)
    def forward(self, q, k, v, mask = None):
        n_head = self.n_head
        d_q = self.d_k
        d_k = self.d_k
        d_v = self.d_v
        
        
    