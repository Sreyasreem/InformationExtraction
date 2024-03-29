
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACTUALNAME BDATE BOXOFFICE CELEBRITY CHARNAME HIGHF LDIR LINK LLANGUAGE LMOVIE LOWF LSTORY MOVIELIST MYEAR RUNTIME onlineplatform separator similarMov similarMovLinkstart :  moviename simMov whereTowatch storyline language director producer writer boxoffice runtime crew \n\t         |  highestRated lowestRated birthday exception movieList\n\t         |  highestRated lowestRated birthday movieList\n\t\t\t moviename : LMOVIE\n                 | epsilon simMov : simMov dmov\n              | dmovdmov : similarMovLink similarMov\n            | similarMovLink epsilon\n            | epsilon similarMov whereTowatch : whereTowatch dwatch\n                    | dwatchdwatch : onlineplatform\n              | epsilon storyline : LSTORY \n                 | epsilon language : LLANGUAGE \n                | epsilon director : director dval \n                | dvaldval : LDIR\n            | epsilon producer : lprod producer\n                | lprodwriter : separator lwrite writer\n              | lwrite writer\n              | lwritelwrite : CELEBRITY\n              | epsilon lprod : CELEBRITY\n             | epsilon boxoffice : BOXOFFICE \n                 | epsilon runtime : RUNTIME \n               | epsilon crew : crew lcast\n            | lcast lcast : LINK ACTUALNAME CHARNAME\n             | LINK ACTUALNAME epsilon \n             | LINK epsilon CHARNAME \n             | epsilon ACTUALNAME CHARNAME \n             | epsilon ACTUALNAME epsilon highestRated : HIGHF\n                    | epsilon lowestRated : LOWF\n                   | epsilon birthday : BDATE\n                | epsilon exception : CELEBRITYmovieList : mlist movieList\n                 | mlistmlist : MOVIELIST MYEAR\n             | MOVIELIST epsilon\n             | epsilon MYEAR epsilon : '
    
_lr_action_items = {'LMOVIE':([0,],[4,]),'HIGHF':([0,],[6,]),'similarMovLink':([0,2,4,5,7,8,9,15,19,20,21,],[-55,9,-4,-5,9,-7,-55,-6,-8,-9,-10,]),'similarMov':([0,2,4,5,7,8,9,10,15,17,19,20,21,],[-55,-55,-4,-5,-55,-7,19,21,-6,21,-8,-9,-10,]),'LOWF':([0,3,5,6,],[-55,12,-44,-43,]),'BDATE':([0,3,5,6,11,12,13,],[-55,-55,-44,-43,23,-45,-46,]),'CELEBRITY':([0,3,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,35,36,37,43,44,45,46,47,48,49,50,51,53,54,55,56,57,58,62,],[-55,-55,-44,-43,-55,-7,-55,-55,-45,-46,-55,-6,-12,-14,-13,-8,-9,-10,31,-47,-48,-55,-11,-15,-14,-55,-17,-18,51,-20,-21,-22,55,-19,51,-22,-30,55,55,-28,-29,-23,-31,55,]),'MOVIELIST':([0,3,5,6,11,12,13,22,23,24,29,31,32,33,40,41,42,],[-55,-55,-44,-43,-55,-45,-46,33,-47,-48,33,-49,33,-55,-52,-53,-54,]),'MYEAR':([0,3,5,6,11,12,13,22,23,24,29,31,32,33,34,40,41,42,],[-55,-55,-44,-43,-55,-45,-46,-55,-47,-48,-55,-49,-55,40,42,-52,-53,-54,]),'$end':([1,30,32,33,38,39,40,41,42,68,69,72,73,75,76,77,78,79,80,],[0,-3,-51,-55,-2,-50,-52,-53,-54,-1,-37,-36,-55,-55,-38,-39,-40,-42,-41,]),'onlineplatform':([7,8,9,14,15,16,17,18,19,20,21,26,28,],[18,-7,-55,18,-6,-12,-14,-13,-8,-9,-10,-11,-14,]),'LSTORY':([7,8,9,14,15,16,17,18,19,20,21,26,28,],[-55,-7,-55,27,-6,-12,-14,-13,-8,-9,-10,-11,-14,]),'LLANGUAGE':([7,8,9,14,15,16,17,18,19,20,21,25,26,27,28,],[-55,-7,-55,-55,-6,-12,-14,-13,-8,-9,-10,36,-11,-15,-14,]),'LDIR':([7,8,9,14,15,16,17,18,19,20,21,25,26,27,28,35,36,37,43,44,45,46,48,50,],[-55,-7,-55,-55,-6,-12,-14,-13,-8,-9,-10,-55,-11,-15,-14,45,-17,-18,45,-20,-21,-22,-19,-22,]),'separator':([7,8,9,14,15,16,17,18,19,20,21,25,26,27,28,35,36,37,43,44,45,46,47,48,49,50,51,53,54,55,56,57,58,62,],[-55,-7,-55,-55,-6,-12,-14,-13,-8,-9,-10,-55,-11,-15,-14,-55,-17,-18,-55,-20,-21,-22,53,-19,-24,-22,-30,-55,53,-28,-29,-23,-31,53,]),'BOXOFFICE':([7,8,9,14,15,16,17,18,19,20,21,25,26,27,28,35,36,37,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,67,],[-55,-7,-55,-55,-6,-12,-14,-13,-8,-9,-10,-55,-11,-15,-14,-55,-17,-18,-55,-20,-21,-22,-55,-19,-24,-22,-30,60,-55,-27,-28,-29,-23,-31,-55,-26,-25,]),'RUNTIME':([7,8,9,14,15,16,17,18,19,20,21,25,26,27,28,35,36,37,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,67,],[-55,-7,-55,-55,-6,-12,-14,-13,-8,-9,-10,-55,-11,-15,-14,-55,-17,-18,-55,-20,-21,-22,-55,-19,-24,-22,-30,-55,-55,-27,-28,-29,-23,-31,65,-32,-33,-55,-26,-25,]),'LINK':([7,8,9,14,15,16,17,18,19,20,21,25,26,27,28,35,36,37,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,72,73,75,76,77,78,79,80,],[-55,-7,-55,-55,-6,-12,-14,-13,-8,-9,-10,-55,-11,-15,-14,-55,-17,-18,-55,-20,-21,-22,-55,-19,-24,-22,-30,-55,-55,-27,-28,-29,-23,-31,-55,-32,-33,-55,-26,70,-34,-35,-25,70,-37,-36,-55,-55,-38,-39,-40,-42,-41,]),'ACTUALNAME':([7,8,9,14,15,16,17,18,19,20,21,25,26,27,28,35,36,37,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,78,79,80,],[-55,-7,-55,-55,-6,-12,-14,-13,-8,-9,-10,-55,-11,-15,-14,-55,-17,-18,-55,-20,-21,-22,-55,-19,-24,-22,-30,-55,-55,-27,-28,-29,-23,-31,-55,-32,-33,-55,-26,-55,-34,-35,-25,-55,-37,73,75,-36,-55,-55,-38,-39,-40,-42,-41,]),'CHARNAME':([70,73,74,75,],[-55,76,78,80,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'moviename':([0,],[2,]),'highestRated':([0,],[3,]),'epsilon':([0,2,3,7,9,11,14,22,25,29,32,33,35,43,47,49,52,53,54,59,62,64,68,70,73,75,],[5,10,13,17,20,24,28,34,37,34,34,41,46,50,56,58,61,56,56,66,56,71,71,74,77,79,]),'simMov':([2,],[7,]),'dmov':([2,7,],[8,15,]),'lowestRated':([3,],[11,]),'whereTowatch':([7,],[14,]),'dwatch':([7,14,],[16,26,]),'birthday':([11,],[22,]),'storyline':([14,],[25,]),'exception':([22,],[29,]),'movieList':([22,29,32,],[30,38,39,]),'mlist':([22,29,32,],[32,32,32,]),'language':([25,],[35,]),'director':([35,],[43,]),'dval':([35,43,],[44,48,]),'producer':([43,49,],[47,57,]),'lprod':([43,49,],[49,49,]),'writer':([47,54,62,],[52,63,67,]),'lwrite':([47,53,54,62,],[54,62,54,54,]),'boxoffice':([52,],[59,]),'runtime':([59,],[64,]),'crew':([64,],[68,]),'lcast':([64,68,],[69,72,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> moviename simMov whereTowatch storyline language director producer writer boxoffice runtime crew','start',11,'p_start','task.py',232),
  ('start -> highestRated lowestRated birthday exception movieList','start',5,'p_start','task.py',233),
  ('start -> highestRated lowestRated birthday movieList','start',4,'p_start','task.py',234),
  ('moviename -> LMOVIE','moviename',1,'p_moviename','task.py',240),
  ('moviename -> epsilon','moviename',1,'p_moviename','task.py',241),
  ('simMov -> simMov dmov','simMov',2,'p_simMov','task.py',253),
  ('simMov -> dmov','simMov',1,'p_simMov','task.py',254),
  ('dmov -> similarMovLink similarMov','dmov',2,'p_dmov','task.py',260),
  ('dmov -> similarMovLink epsilon','dmov',2,'p_dmov','task.py',261),
  ('dmov -> epsilon similarMov','dmov',2,'p_dmov','task.py',262),
  ('whereTowatch -> whereTowatch dwatch','whereTowatch',2,'p_whereTowatch','task.py',275),
  ('whereTowatch -> dwatch','whereTowatch',1,'p_whereTowatch','task.py',276),
  ('dwatch -> onlineplatform','dwatch',1,'p_dwatch','task.py',282),
  ('dwatch -> epsilon','dwatch',1,'p_dwatch','task.py',283),
  ('storyline -> LSTORY','storyline',1,'p_storyline','task.py',293),
  ('storyline -> epsilon','storyline',1,'p_storyline','task.py',294),
  ('language -> LLANGUAGE','language',1,'p_language','task.py',306),
  ('language -> epsilon','language',1,'p_language','task.py',307),
  ('director -> director dval','director',2,'p_director','task.py',319),
  ('director -> dval','director',1,'p_director','task.py',320),
  ('dval -> LDIR','dval',1,'p_dval','task.py',326),
  ('dval -> epsilon','dval',1,'p_dval','task.py',327),
  ('producer -> lprod producer','producer',2,'p_producer','task.py',336),
  ('producer -> lprod','producer',1,'p_producer','task.py',337),
  ('writer -> separator lwrite writer','writer',3,'p_writer','task.py',343),
  ('writer -> lwrite writer','writer',2,'p_writer','task.py',344),
  ('writer -> lwrite','writer',1,'p_writer','task.py',345),
  ('lwrite -> CELEBRITY','lwrite',1,'p_lwrite','task.py',350),
  ('lwrite -> epsilon','lwrite',1,'p_lwrite','task.py',351),
  ('lprod -> CELEBRITY','lprod',1,'p_lprod','task.py',359),
  ('lprod -> epsilon','lprod',1,'p_lprod','task.py',360),
  ('boxoffice -> BOXOFFICE','boxoffice',1,'p_boxoffice','task.py',368),
  ('boxoffice -> epsilon','boxoffice',1,'p_boxoffice','task.py',369),
  ('runtime -> RUNTIME','runtime',1,'p_runtime','task.py',382),
  ('runtime -> epsilon','runtime',1,'p_runtime','task.py',383),
  ('crew -> crew lcast','crew',2,'p_crew','task.py',395),
  ('crew -> lcast','crew',1,'p_crew','task.py',396),
  ('lcast -> LINK ACTUALNAME CHARNAME','lcast',3,'p_lcast','task.py',402),
  ('lcast -> LINK ACTUALNAME epsilon','lcast',3,'p_lcast','task.py',403),
  ('lcast -> LINK epsilon CHARNAME','lcast',3,'p_lcast','task.py',404),
  ('lcast -> epsilon ACTUALNAME CHARNAME','lcast',3,'p_lcast','task.py',405),
  ('lcast -> epsilon ACTUALNAME epsilon','lcast',3,'p_lcast','task.py',406),
  ('highestRated -> HIGHF','highestRated',1,'p_highestRated','task.py',424),
  ('highestRated -> epsilon','highestRated',1,'p_highestRated','task.py',425),
  ('lowestRated -> LOWF','lowestRated',1,'p_lowestRated','task.py',437),
  ('lowestRated -> epsilon','lowestRated',1,'p_lowestRated','task.py',438),
  ('birthday -> BDATE','birthday',1,'p_birthday','task.py',450),
  ('birthday -> epsilon','birthday',1,'p_birthday','task.py',451),
  ('exception -> CELEBRITY','exception',1,'p_exception','task.py',461),
  ('movieList -> mlist movieList','movieList',2,'p_movieList','task.py',467),
  ('movieList -> mlist','movieList',1,'p_movieList','task.py',468),
  ('mlist -> MOVIELIST MYEAR','mlist',2,'p_mlist','task.py',472),
  ('mlist -> MOVIELIST epsilon','mlist',2,'p_mlist','task.py',473),
  ('mlist -> epsilon MYEAR','mlist',2,'p_mlist','task.py',474),
  ('epsilon -> <empty>','epsilon',0,'p_epsilon','task.py',489),
]
