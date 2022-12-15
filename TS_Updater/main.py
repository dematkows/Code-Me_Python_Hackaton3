from win32com.client import Dispatch
from win32com.client import constants

xl = Dispatch("Excel.Application")
xl.Range("A1").Value = "Hello"
print(xl.Range("B2").Value)
print(constants.xlThemeColorAccent4)
r = xl.Range("A7:C11")
r.Select()
i = xl.Selection.Interior
i.Pattern = constants.xlSolid
i.PatternColorIndex = constants.xlAutomatic
i.ThemeColor = constants.xlThemeColorAccent4
i.TintAndShade = 0
