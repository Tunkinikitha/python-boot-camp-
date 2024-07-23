#abstraction ->hidding  the data
#inheritence->inheriting the data from base class(parent)to the derived class(child),single,multiple,multilevel,hybid,hierarical
class jntuh:
    def schedule_acacdemics():
        print("scheduling acadamics")
    def declare_holidays():
        print('national and summar holidays')
    def result():
        print('go to www.jntuhresult.com')
class sridevi(jntuh):
    def fees():
        print('3rd yr fee is 85k')
sobj=sridevi        
sobj.fees()
sobj.schedule_acacdemics()
sobj.declare_holidays()
sobj.result()


class rbibank():
    def interest():
        pass
    def loan():
        print('provide home loans')
class hdfc(rbibank):
    def interest():
        print('7.5% interrest')
class sbi(rbibank):
    def interrest():
        print('11% interest')
aobj=rbibank
aobj.interest()
aobj.loan()

class jntuh:
    def schedule_acacdemics():
        print("scheduling acadamics")
    def declare_holidays():
        print('national and summar holidays')
    def result():
        print('go to www.jntuhresult.com')
class sridevi(jntuh):
    def fees():
        print('3rd yr fee is 85k')
sobj=sridevi
sobj.fees()
sobj.schedule_acacdemics()
sobj.declare_holidays()
sobj.result()

from abc import ABC
class vehicle(ABC):
    def speed():
        pass
    def milage():
        pass
    def model():
        pass
    def brreak():
        print('stop the vehicle')
class rangerover(vehicle):
    def speed():
        print('450 max speed')
    def milage():
        print('12kmph')
    def model():
        print('jgkggkk')
class fortune(vehicle):
    def speed():
        print('300 max speed')
    def milage():
        print('11kmph')
    def model():
        print('jgkggkr')
fobj=rangerover
fobj.speed()
fobj.milage()
fobj.brreak()
fobj.model()   
