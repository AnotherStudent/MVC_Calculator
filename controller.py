class CalcController:
    def __init__(self, model, view):
        self.model = model
        self.model.OnResult = self.OnResult
        self.model.OnError = self.OnError

        self.view = view
        self.model.AllClear()

    # interface for view
    def command(self, command):
        if command in ['0','1','2','3','4','5','6','7','8','9']:
            self.model.EnterDigit(command)
        elif command == 'DOT':
            self.model.EnterDot()
        elif command == 'SIGN':
            self.model.Sign()
        elif command == 'CLEAR':
            self.model.Clear()
        elif command == 'ALL_CLEAR':
            self.model.AllClear()
        elif command == 'ADDITION':
            self.model.Addition()
        elif command == 'SUBSTRACTION':
            self.model.Substraction()
        elif command == 'MULTIPLICATION':
            self.model.Multiplication()
        elif command == 'DIVISION':
            self.model.Division()
        elif command == 'SQRT':
            self.model.CalcSqrt()
        elif command == 'CALCULATE':
            self.model.CalcResult()

    def OnResult(self, result):
        self.view.ShowResult(result)

    def OnError(self):
        self.view.ShowResult('ERROR')