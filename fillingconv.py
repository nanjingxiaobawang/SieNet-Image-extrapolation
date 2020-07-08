
import torch
import torch.nn.functional as F
from torch import nn, cuda
from torch.autograd import Variable
import collections
from itertools import repeat
def _ntuple(n):
    def parse(x):
        if isinstance(x, collections.Iterable):
            return x
        return tuple(repeat(x, n))
    return parse

class Parameter(torch.Tensor):
    def __new__(cls, data=None, requires_grad=True):
        if data is None:
            data = torch.Tensor()
        return torch.Tensor._make_subclass(cls, data, requires_grad)

    def __repr__(self):
        return 'Parameter containing:\n' + super(Parameter, self).__repr__()

    def __reduce_ex__(self, proto):
        return Parameter, (super(Parameter, self), self.requires_grad)

class FillingConv2d(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride=1,padding=0, dilation=1, groups=1, bias=False):
        super().__init__()
        self.pad_conv = nn.Conv2d(in_channels, in_channels, kernel_size, 1,
                                  padding+(kernel_size//2), dilation,groups,bias=True)
        self.mask_conv = nn.Conv2d(in_channels, in_channels,kernel_size, 1,
                                   padding+(kernel_size//2),dilation,groups,bias=False)
        nn.init.constant_(self.mask_conv.weight,1)
        _pair = _ntuple(2)
        self.padding = _pair(padding)
        print(self.pad_conv.weight.shape)

    def forward(self, input):
        assert len(input.shape) == 4
        lr, tb = self.padding
        mask = self.mask_conv(input)
        mask = torch.sigmoid(mask)
        padding_feat = self.pad_conv(input)
        pad_input = F.pad(input, pad=[lr, lr, tb, tb])
        output = mask * pad_input + padding_feat * (1 - mask)  # mask: N,C,H+p,W+p
        return output
