# File: L (Python 2.4)

from SpecImports import *
from toontown.toonbase import ToontownGlobals
CogParent = 100007
CogParent1 = 100009
BattlePlace1 = 100004
BattlePlace2 = 100005
BattleCellId = 0
BattleCellId1 = 1
BattleCells = {
    BattleCellId: {
        'parentEntId': BattlePlace1,
        'pos': Point3(0, 0, 0) },
    BattleCellId1: {
        'parentEntId': BattlePlace2,
        'pos': Point3(0, 0, 0) } }
CogData = [
    {
        'parentEntId': CogParent,
        'boss': 0,
        'level': ToontownGlobals.CashbotMintCogLevel,
        'battleCell': BattleCellId,
        'pos': Point3(-8, 4, 0),
        'h': 180,
        'behavior': 'stand',
        'path': None,
        'skeleton': 1 },
    {
        'parentEntId': CogParent,
        'boss': 0,
        'level': ToontownGlobals.CashbotMintCogLevel + 1,
        'battleCell': BattleCellId,
        'pos': Point3(-3, 4, 0),
        'h': 180,
        'behavior': 'stand',
        'path': None,
        'skeleton': 1 },
    {
        'parentEntId': CogParent,
        'boss': 0,
        'level': ToontownGlobals.CashbotMintCogLevel,
        'battleCell': BattleCellId,
        'pos': Point3(3, 4, 0),
        'h': 180,
        'behavior': 'stand',
        'path': None,
        'skeleton': 1 },
    {
        'parentEntId': CogParent,
        'boss': 0,
        'level': ToontownGlobals.CashbotMintCogLevel + 1,
        'battleCell': BattleCellId,
        'pos': Point3(8, 4, 0),
        'h': 180,
        'behavior': 'stand',
        'path': None,
        'skeleton': 1 },
    {
        'parentEntId': CogParent1,
        'boss': 0,
        'level': ToontownGlobals.CashbotMintCogLevel,
        'battleCell': BattleCellId1,
        'pos': Point3(-8, 4, 0),
        'h': 180,
        'behavior': 'stand',
        'path': None,
        'skeleton': 1 },
    {
        'parentEntId': CogParent1,
        'boss': 0,
        'level': ToontownGlobals.CashbotMintCogLevel + 1,
        'battleCell': BattleCellId1,
        'pos': Point3(-3, 4, 0),
        'h': 180,
        'behavior': 'stand',
        'path': None,
        'skeleton': 1 },
    {
        'parentEntId': CogParent1,
        'boss': 0,
        'level': ToontownGlobals.CashbotMintCogLevel,
        'battleCell': BattleCellId1,
        'pos': Point3(3, 4, 0),
        'h': 180,
        'behavior': 'stand',
        'path': None,
        'skeleton': 1 },
    {
        'parentEntId': CogParent1,
        'boss': 0,
        'level': ToontownGlobals.CashbotMintCogLevel + 1,
        'battleCell': BattleCellId1,
        'pos': Point3(8, 4, 0),
        'h': 180,
        'behavior': 'stand',
        'path': None,
        'skeleton': 1 }]
ReserveCogData = []