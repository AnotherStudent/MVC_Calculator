from decimal import Decimal

class CalcModel(object):
    maxLen = 10
    def __init__(self):
        self.OnResult = None
        self.OnError = None

        self.x = Decimal("0")
        self.y = Decimal("0")
        self.isEnterDot = False 
        self.op = None 
        self.newEnter = False
        self.isError = False

    def Change(self):
        r = '{0:f}'.format(self.x)
        if self.isEnterDot:
            r = r + '.'
        self.OnResult(r)
        pass

    def IsMaximumLenX(self):
        x = '{0:f}'.format(self.x)
        maxLenX = self.maxLen
        if '-' in x:
            maxLenX = maxLenX + 1
        if '.' in x:
            maxLenX = maxLenX + 1
        return maxLenX <= len(x)

    # interface for controller
    def EnterDigit(self, digit):
        if self.isError:
            return
        if self.newEnter:
            self.Clear()
            self.newEnter = False
        if self.IsMaximumLenX():
            return
        x = '{0:f}'.format(self.x)
        if self.isEnterDot:
            x = x + '.'
            self.isEnterDot = False
        x = x + digit
        self.x = Decimal(x)
        self.Change()
        pass

    # interface for controller
    def EnterDot(self):
        if self.isError:
            return
        if self.newEnter:
            self.Clear()
            self.newEnter = False
        if self.IsMaximumLenX():
            return
        if not '.' in str(self.x):
            self.isEnterDot = True
            self.Change()

    # interface for controller
    def Sign(self):
        if self.isError:
            return
        self.x = Decimal("0") - self.x
        self.Change()

    # interface for controller
    def Clear(self):
        if self.isError:
            return
        self.x = Decimal("0")
        self.isEnterDot = False
        self.Change()

    # interface for controller
    def AllClear(self):
        self.x = Decimal("0")
        self.y = Decimal("0")
        self.isEnterDot = False  
        self.op = None
        self.isError = False
        self.Change()

    # interface for controller
    def Addition(self):
        if self.isError:
            return
        self.y = self.x
        self.op = 'ADDITION'
        self.newEnter = True
        pass

    # interface for controller
    def Substraction(self):
        if self.isError:
            return
        self.y = self.x
        self.op = 'SUBSTRACTION'
        self.newEnter = True
        pass

    # interface for controller
    def Multiplication(self):
        if self.isError:
            return
        self.y = self.x
        self.op = 'MULTIPLICATION'
        self.newEnter = True
        pass

    # interface for controller
    def Division(self):
        if self.isError:
            return
        self.y = self.x
        self.op = 'DIVISION'
        self.newEnter = True
        pass

    # interface for controller
    def CalcSqrt(self):
        if self.isError:
            return
        if self.x >= Decimal("0"):
            self.x = self.x.sqrt()
            self.Change()
        else:
            self.isError = True
            self.OnError()

    # interface for controller
    def CalcResult(self):
        if self.isError:
            return
        if self.op == 'ADDITION':
            self.x = self.x + self.y
            self.Change()
        elif self.op == 'SUBSTRACTION':
            self.x = self.y - self.x
            self.Change()
        elif self.op == 'MULTIPLICATION':
            self.x = self.x * self.y
            self.Change()
        elif self.op == 'DIVISION':
            if self.x == Decimal("0"):
                self.OnError()
                self.isError = True
            else:
                self.x = self.y / self.x
                self.Change()
        self.op = None
        self.newEnter = True
        