# automatically generated by the FlatBuffers compiler, do not modify

# namespace: proto

import flatbuffers

class AuthCryptosignWelcome(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsAuthCryptosignWelcome(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AuthCryptosignWelcome()
        x.Init(buf, n + offset)
        return x

    # AuthCryptosignWelcome
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def AuthCryptosignWelcomeStart(builder): builder.StartObject(0)
def AuthCryptosignWelcomeEnd(builder): return builder.EndObject()