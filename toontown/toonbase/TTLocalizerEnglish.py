from toontown.toonbase.TTLocalizerEnglishProperty import *
from toontown.catalog import CatalogAccessoryItemGlobals
from otp.otpbase import OTPLocalizer as OL
OL.SpeedChatStaticText = OL.SpeedChatStaticTextToontown.copy()
for key in OL.SpeedChatStaticTextCommon.keys():
    OL.SpeedChatStaticText[key] = OL.SpeedChatStaticTextCommon[key]

commitmantst = 'kptmptest - removable'
InterfaceFont = 'phase_3/models/fonts/ImpressBT.ttf'
ToonFont = 'phase_3/models/fonts/ImpressBT.ttf'
SuitFont = 'phase_3/models/fonts/vtRemingtonPortable.ttf'
SignFont = 'phase_3/models/fonts/MickeyFont'
MinnieFont = 'phase_3/models/fonts/MinnieFont.ttf'
FancyFont = 'phase_3/models/fonts/Comedy.ttf'
NametagFonts = (
 'phase_3/models/fonts/AnimGothic.ttf',
 'phase_3/models/fonts/Aftershock.ttf',
 'phase_3/models/fonts/JiggeryPokery.ttf',
 'phase_3/models/fonts/Ironwork.ttf',
 'phase_3/models/fonts/HastyPudding.ttf',
 'phase_3/models/fonts/Comedy.ttf',
 'phase_3/models/fonts/Humanist.ttf',
 'phase_3/models/fonts/Portago.ttf',
 'phase_3/models/fonts/Musicals.ttf',
 'phase_3/models/fonts/Scurlock.ttf',
 'phase_3/models/fonts/Danger.ttf',
 'phase_3/models/fonts/Alie.ttf',
 'phase_3/models/fonts/OysterBar.ttf',
 'phase_3/models/fonts/RedDogSaloon.ttf'
)
NametagFontNames = ('Member',
 'Shivering',
 'Wonky',
 'Fancy',
 'Silly',
 'Zany',
 'Practical',
 'Nautical',
 'Whimsical',
 'Spooky',
 'Action',
 'Poetic',
 'Boardwalk',
 'Western')
NametagLabel = ' Nametag'
UnpaidNameTag = 'Basic'
GM_NAMES = ('CART SURFER',
 'COFFEE SHOP',
 'ASTRO-BARRIER',
 'GC')
BuildingNametagFont = 'phase_3/models/fonts/MickeyFont'
BuildingNametagShadow = None
ProductPrefix = 'TT'
Mickey = 'Mickey'
VampireMickey = 'VampireMickey'
Minnie = 'Minnie'
WitchMinnie = 'WitchMinnie'
Donald = 'Donald'
DonaldDock = 'DonaldDock'
FrankenDonald = 'FrankenDonald'
Daisy = 'Daisy'
SockHopDaisy = 'SockHopDaisy'
Goofy = 'Goofy'
SuperGoofy = 'SuperGoofy'
Pluto = 'Pluto'
WesternPluto = 'WesternPluto'
Flippy = 'Flippy'
Chip = 'Chip'
Dale = 'Dale'
JailbirdDale = 'JailbirdDale'
PoliceChip = 'PoliceChip'
lTheBrrrgh = 'HOT CHOCOLATE'
lDaisyGardens = 'LANDING PAD'
lDonaldsDock = "PIZZA CHEF"
lDonaldsDreamland = "PAINT BY LETTERS"
lMinniesMelodyland = "MINE"
lToontownCentral = 'CONSTRUCTION WORKER'
lToonHQ = 'JET PACK ADVENTURE'
lSellbotHQ = 'GIFT SHOP'
lGoofySpeedway = 'HIKING IN THE FOREST'
lOutdoorZone = "RESCUE SQUAD"
lGolfZone = "PET SHOP"
lPartyHood = 'SKI VILLAGE'
GlobalStreetNames = {20000: ('to', 'on', 'Tutorial Terrace'),
 1000: ('SKI HILL', 'ICE HOCKEY', 'Playground'),
 1100: ('to', 'on', 'SNOWBALL FIGHT'),
 1200: ('to', 'on', 'SNOW FORTS'),
 1300: ('to', 'on', 'SOCCER'),
 2000: ('FOOTBALL', 'BEACH', 'Playground'),
 2100: ('to', 'on', 'BASEBALL'),
 2200: ('to', 'on', 'EMERALD PRINCESS'),
 2300: ('to', 'on', 'BEAN COUNTERS'),
 3000: ('NEWSPAPER ARCHIVES', 'MANHOLE COVER', 'Playground'),
 3100: ('to', 'on', 'UNDERGROUND POOL'),
 3200: ('to', 'on', 'SCUBA DIVING'),
 3300: ('to', 'on', 'ICE FISHING'),
 4000: ('CRATES AND BOXES', 'CASE OF THE MISSING COINS', 'Playground'),
 4100: ('to', 'on', 'ANVIL SMITH'),
 4200: ('to', 'on', 'HALLOWEEN'),
 4300: ('to', 'on', 'KNIGHT'),
 5000: ('MEDIEVAL PARTY', 'BLACK PUFFLE', 'Playground'),
 5100: ('to', 'on', 'BLUE PUFFLE'),
 5200: ('to', 'on', 'PINK PUFFLE'),
 5300: ('to', 'on', 'GREEN PUFFLE'),
 9000: ('PURPLE PUFFLE', 'PUFFLE FURNITURE', 'Playground'),
 9100: ('to', 'on', 'RED PUFFLE'),
 9200: ('to', 'on', 'YELLOW PUFFLE'),
 10000: ('to', 'in', 'SUMMER PARTY'),
 10100: ('LIFE RING', 'O BERRY', 'GRAY FISH'),
 10200: ('GARY THE GADGET GUY', 'COINS', 'JOLLY ROGER FLAG'),
 10500: ('KLUTZY', 'YARR', 'BUOYS'),
 10600: ('SNOW CASTLE', 'HOT SAUCE', 'HERBERT P. BEAR'),
 10700: ('BETA PARTY', 'CHRISTMAS CAROLS', 'AUNT ARCTIC'),
 11000: ('SNOW SHOVEL', 'SECRET AGENT', 'HIDDEN ITEMS'),
 11100: ('ICE CREAM', 'CAPTAIN ROCKHOPPER', 'THE MIGRATOR'),
 11200: ('FLUFFY THE FISH', 'UNDERGROUND FLOOD', 'MULLET'),
 11500: ('GADGET ROOM', 'FLOORING UPGRADE', 'SHARK'),
 12000: ('to', 'in', 'JACKHAMMER'),
 12100: ('NIGHT VISION GOGGLES', 'THIN ICE', 'JET PACK'),
 12500: ('SPACE ADVENTURE', 'DRAGON', 'MIGHTY PLUNGER'),
 12600: ('PUFFLE ROUND-UP', 'SLED RACING', 'TOUR GUIDE'),
 12700: ('SHADOW GUY & GAMMA GAL', 'SNOW GLOBE IGLOO', 'AC3000'),
 13000: ('to', 'in', 'AVALANCHE'),
 13100: ('FIREFIGHTER', 'CATCHIN\' WAVES', 'WATER PARTY'),
 13200: ('CACTUS', 'OCTOPUS', "AQUA GRABBER"),
 13300: ('WHITE PUFFLE', 'NINJA', 'TIPPING THE ICEBERG'),
 13400: ('BLAST', 'KEEPER OF THE BOILER ROOM', 'Yarr'),
 13500: ('POP', 'CHIRP', 'FLARE'),
 13600: ('BOUNCER', 'FLIT', 'LOOP')}
DonaldsDock = ('to', 'in', lDonaldsDock)
ToontownCentral = ('to', 'in', lToontownCentral)
TheBrrrgh = ('to', 'in', lTheBrrrgh)
MinniesMelodyland = ('to', 'in', lMinniesMelodyland)
DaisyGardens = ('to', 'in', lDaisyGardens)
OutdoorZone = ('to', 'in', lOutdoorZone)
FunnyFarm = ('SNOWY NIGHT', 'NIBLET', 'ED MCCOOL AND DESTRUCTO')
GoofySpeedway = ('to', 'in', lGoofySpeedway)
DonaldsDreamland = ('to', 'in', lDonaldsDreamland)
BossbotHQ = ('to', 'in', 'PUFFLES ON THE LOOSE')
SellbotHQ = ('to', 'in', 'CADENCE AND THE KEEPER')
CashbotHQ = ('to', 'in', 'GOLDEN PUFFLE')
LawbotHQ = ('to', 'in', 'METEOR PUFFLE')
Tutorial = ('ABOMINABLE SNOW PUFFLE', 'RAINBOW PUFFLE', 'Toon-torial')
MyEstate = ('to', 'in', 'Club Penguin Times')
WelcomeValley = ('to', 'in', 'Can of Worms')
GolfZone = ('to', 'in', lGolfZone)
PartyHood = ('Invisible Ninja Suit', 'Winter Fiesta Party', lPartyHood)
Factory = 'Factory'
Headquarters = 'Headquarters'
SellbotFrontEntrance = 'Penguin Mail'
SellbotSideEntrance = 'Bumble Bee'
Office = 'Office'
FactoryNames = {0: 'Pizzatron 3000',
 11500: 'Card-Jitsu',
 13300: 'Adopt-A-Puffle'}
FactoryTypeLeg = 'Leg'
FactoryTypeArm = 'Arm'
FactoryTypeTorso = 'Torso'
MintFloorTitle = 'Floor %s'
lCancel = 'Cancel'
lClose = 'Close'
lOK = 'OK'
lNext = 'Next'
lQuit = 'Quit'
lYes = 'Yes'
lNo = 'No'
sleep_auto_reply = '%s is sleeping right now'
lHQOfficerF = 'Rock & Roll Suit'
lHQOfficerM = 'Construction'
MickeyMouse = 'Hidden Pins'
AIStartDefaultDistrict = 'Sillyville'
Cog = 'Cog'
Cogs = 'Cogs'
ACog = 'Treasure Hunt Game'
TheCogs = 'DJ3K'
ASkeleton = 'Surf Boards'
Skeleton = 'Skelecog'
SkeletonP = 'Skelecogs'
Av2Cog = 'Beach Chair Chilling'
v2Cog = 'Telescope'
v2CogP = 'Fish Costume'
ASkeleton = 'Crow\'s Nest'
Foreman = 'The Cove'
ForemanP = 'Captain\'s Quarters'
AForeman = 'Iceberg'
CogVP = Cog + ' V.P.'
CogVPs = "The Lounge"
ACogVP = ACog + ' V.P.'
Supervisor = 'Rockhopper\'s Key'
SupervisorP = 'Penguins That Time Forgot'
ASupervisor = 'Team Blue Rally'
CogCFO = Cog + ' C.F.O.'
CogCFOs = "Jet Pack Adventure"
ACogCFO = ACog + ' C.F.O.'
TheFish = 'Ruby and the Ruby'
AFish = 'Snowball Fight'
Level = 'Level'
QuestsCompleteString = 'Complete'
QuestsNotChosenString = 'Snowball Press'
Period = '.'
Laff = 'Laff'
QuestInLocationString = ' %(inPhrase)s %(location)s'
QuestsDefaultGreeting = ('Hello, _avName_!',
 'Hi, _avName_!',
 'Hey there, _avName_!',
 'Say there, _avName_!',
 'Welcome, _avName_!',
 'Howdy, _avName_!',
 'How are you, _avName_?',
 'Greetings _avName_!')
QuestsDefaultIncomplete = ("How's that task coming, _avName_?",
 'Music Jam',
 'Keep up the good work, _avName_!',
 'Puffle Chew-Chew',
 'Fairy Fables',
 'Jelly Fish')
QuestsDefaultIncompleteProgress = ('Hydro Hopper', 'Fish Bait', 'Pirate')
QuestsDefaultIncompleteWrongNPC = ('Nice work on that ToonTask. You should go visit _toNpcName_._where_', 'Looks like you are ready to finish your ToonTask. Go see _toNpcName_._where_.', 'Go see _toNpcName_ to finish your ToonTask._where_')
QuestsDefaultComplete = ('Puffle O\'s', 'Great job, _avName_! Take this reward...', 'Wonderful job, _avName_! Here is your reward...')
QuestsDefaultLeaving = ('Bye!',
 'Goodbye!',
 'So long, _avName_.',
 'See ya, _avName_!',
 'Fall Fair Games',
 'Thinga-ma-jig 3000',
 'Rad Scientist')
QuestsDefaultReject = ('Hello.',
 'Quip and Qua',
 'Twee',
 'Coins For Change',
 "I'm a little busy now, _avName_.",
 'Yes?',
 'Howdy, _avName_!',
 'Welcome, _avName_!',
 "Hey, _avName_! How's it going?",
 'Surfing with the Sharks',
 'Dance Contest',
 'Purple Octopus',
 'Penguin Band' + Cog + 'Giant Squid',
 'Dojo Sketch',
 Cog + 'Flare Flinger 3000',
 'Coffee Delivery Truck' + Cogs + 'Herbert & Klutzy',
 'Anniversary Party',
 'Halloween Party',
 'Sensei',
 'Jackhammers',
 'Quest for the Golden Puffle' + Cog + ' defeated.',
 'Rockhopper' + Cog + 'Storm',
 'Camera',
 'Wigs',
 "Pizza Parlor",
 'If a ' + Cog + 'Coffee Machine',
 'Pet Shop Staff' + Cog + 'Costume Trunk',
 'Defeating ' + Cogs + 'Stompin\' Bob')
QuestsDefaultTierNotDone = ('Hello, _avName_! You must finish your current ToonTasks before getting a new one.', 'G Billy', 'Hi, _avName_! Before I can give you a new ToonTask, you need to finish the ones you have.')
QuestsDefaultQuest = None
QuestsDefaultVisitQuestDialog = ('I heard _toNpcName_ is looking for you._where_',
 'Stop by and see _toNpcName_ when you get a chance._where_',
 'Pay a visit to _toNpcName_ next time you are over that way._where_',
 'If you get a chance, stop in and say hi to _toNpcName_._where_',
 '_toNpcName_ will give you your next ToonTask._where_')
QuestsLocationArticle = ''

def getLocalNum(num):
    return str(num)


QuestsItemNameAndNum = '%(num)s %(name)s'
QuestsCogQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogQuestHeadline = 'WANTED'
QuestsCogQuestSCStringS = 'I need to defeat %(cogName)s%(cogLoc)s.'
QuestsCogQuestSCStringP = 'I need to defeat some %(cogName)s%(cogLoc)s.'
QuestsCogQuestDefeat = 'Defeat %s'
QuestsCogQuestDefeatDesc = '%(numCogs)s %(cogName)s'
QuestsCogNewNewbieQuestObjective = 'Help a new Toon defeat %s'
QuestsCogNewNewbieQuestCaption = 'Help a new Toon %d Laff or less'
QuestsCogOldNewbieQuestObjective = 'Help a Toon with %(laffPoints)d Laff or less defeat %(objective)s'
QuestsCogOldNewbieQuestCaption = 'Help a Toon %d Laff or less'
QuestsCogNewbieQuestAux = 'Defeat:'
QuestsNewbieQuestHeadline = 'APPRENTICE'
QuestsCogTrackQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogTrackQuestHeadline = 'WANTED'
QuestsCogTrackQuestSCStringS = 'I need to defeat %(cogText)s%(cogLoc)s.'
QuestsCogTrackQuestSCStringP = 'I need to defeat some %(cogText)s%(cogLoc)s.'
QuestsCogTrackQuestDefeat = 'Defeat %s'
QuestsCogTrackDefeatDesc = '%(numCogs)s %(trackName)s'
QuestsCogLevelQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogLevelQuestHeadline = 'WANTED'
QuestsCogLevelQuestDefeat = 'Defeat %s'
QuestsCogLevelQuestDesc = 'a Level %(level)s+ %(name)s'
QuestsCogLevelQuestDescC = '%(count)s Level %(level)s+ %(name)s'
QuestsCogLevelQuestDescI = 'some Level %(level)s+ %(name)s'
QuestsCogLevelQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsBuildingQuestFloorNumbers = ('',
 'two+',
 'three+',
 'four+',
 'five+')
QuestsBuildingQuestBuilding = 'Building'
QuestsBuildingQuestBuildings = 'Buildings'
QuestsBuildingQuestHeadline = 'DEFEAT'
QuestsBuildingQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsBuildingQuestString = 'Defeat %s'
QuestsBuildingQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsBuildingQuestDesc = 'a %(type)s Building'
QuestsBuildingQuestDescF = 'a %(floors)s story %(type)s Building'
QuestsBuildingQuestDescC = '%(count)s %(type)s Buildings'
QuestsBuildingQuestDescCF = '%(count)s %(floors)s story %(type)s Buildings'
QuestsBuildingQuestDescI = 'some %(type)s Buildings'
QuestsBuildingQuestDescIF = 'some %(floors)s story %(type)s Buildings'
QuestFactoryQuestFactory = 'Factory'
QuestsFactoryQuestFactories = 'Factories'
QuestsFactoryQuestHeadline = 'DEFEAT'
QuestsFactoryQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsFactoryQuestString = 'Defeat %s'
QuestsFactoryQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsFactoryQuestDesc = 'a %(type)s Factory'
QuestsFactoryQuestDescC = '%(count)s %(type)s Factories'
QuestsFactoryQuestDescI = 'some %(type)s Factories'
QuestMintQuestMint = 'Mint'
QuestsMintQuestMints = 'Mints'
QuestsMintQuestHeadline = 'DEFEAT'
QuestsMintQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsMintQuestString = 'Defeat %s'
QuestsMintQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsMintQuestDesc = 'Outdoor Igloo'
QuestsMintQuestDescC = '%(count)s Cog Mints'
QuestsMintQuestDescI = 'Ticket Booth'
QuestsRescueQuestProgress = '%(progress)s of %(numToons)s rescued'
QuestsRescueQuestHeadline = 'RESCUE'
QuestsRescueQuestSCStringS = 'I need to rescue a Toon%(toonLoc)s.'
QuestsRescueQuestSCStringP = 'I need to rescue some Toons%(toonLoc)s.'
QuestsRescueQuestRescue = 'Rescue %s'
QuestsRescueQuestRescueDesc = '%(numToons)s Toons'
QuestsRescueQuestToonS = 'Ridge Run'
QuestsRescueQuestToonP = 'Toons'
QuestsRescueQuestAux = 'Rescue:'
QuestsRescueNewNewbieQuestObjective = 'Help a new Toon rescue %s'
QuestsRescueOldNewbieQuestObjective = 'Help a Toon with %(laffPoints)d Laff or less rescue %(objective)s'
QuestCogPartQuestCogPart = 'Clock Tower'
QuestsCogPartQuestFactories = 'Factories'
QuestsCogPartQuestHeadline = 'RETRIEVE'
QuestsCogPartQuestProgressString = '%(progress)s of %(num)s retrieved'
QuestsCogPartQuestString = 'Retrieve %s'
QuestsCogPartQuestSCString = 'I need to retrieve %(objective)s%(location)s.'
QuestsCogPartQuestAux = 'Retrieve:'
QuestsCogPartQuestDesc = 'White Puffles'
QuestsCogPartQuestDescC = '%(count)s Cog Suit Parts'
QuestsCogPartQuestDescI = 'Dojo Courtyard'
QuestsCogPartNewNewbieQuestObjective = 'Help a new Toon retrieve %s'
QuestsCogPartOldNewbieQuestObjective = 'Help a Toon with %(laffPoints)d Laff or less retrieve %(objective)s'
QuestsDeliverGagQuestProgress = '%(progress)s of %(numGags)s delivered'
QuestsDeliverGagQuestHeadline = 'DELIVER'
QuestsDeliverGagQuestToSCStringS = 'I need to deliver %(gagName)s.'
QuestsDeliverGagQuestToSCStringP = 'I need to deliver some %(gagName)s.'
QuestsDeliverGagQuestSCString = 'Rocking Horse'
QuestsDeliverGagQuestString = 'Deliver %s'
QuestsDeliverGagQuestStringLong = 'Deliver %s to _toNpcName_.'
QuestsDeliverGagQuestInstructions = 'Penguin Style'
QuestsDeliverItemQuestProgress = ''
QuestsDeliverItemQuestHeadline = 'DELIVER'
QuestsDeliverItemQuestSCString = 'I need to deliver %(article)s%(itemName)s.'
QuestsDeliverItemQuestString = 'Deliver %s'
QuestsDeliverItemQuestStringLong = 'Deliver %s to _toNpcName_.'
QuestsVisitQuestProgress = ''
QuestsVisitQuestHeadline = 'VISIT'
QuestsVisitQuestStringShort = 'Visit'
QuestsVisitQuestStringLong = 'Visit _toNpcName_'
QuestsVisitQuestSeeSCString = 'I need to see %s.'
QuestsRecoverItemQuestProgress = '%(progress)s of %(numItems)s recovered'
QuestsRecoverItemQuestHeadline = 'RECOVER'
QuestsRecoverItemQuestSeeHQSCString = 'Stage Director' + lHQOfficerM + '.'
QuestsRecoverItemQuestReturnToHQSCString = 'I need to return %s to an ' + lHQOfficerM + '.'
QuestsRecoverItemQuestReturnToSCString = 'I need to return %(item)s to %(npcName)s.'
QuestsRecoverItemQuestGoToHQSCString = 'Conductor'
QuestsRecoverItemQuestGoToPlaygroundSCString = 'I need to go to %s Playground.'
QuestsRecoverItemQuestGoToStreetSCString = 'I need to go %(to)s %(street)s in %(hood)s.'
QuestsRecoverItemQuestVisitBuildingSCString = 'I need to visit %s%s.'
QuestsRecoverItemQuestWhereIsBuildingSCString = 'Where is %s%s?'
QuestsRecoverItemQuestRecoverFromSCString = 'I need to recover %(item)s from %(holder)s%(loc)s.'
QuestsRecoverItemQuestString = 'Recover %(item)s from %(holder)s'
QuestsRecoverItemQuestHolderString = '%(level)s %(holder)d+ %(cogs)s'
QuestsTrackChoiceQuestHeadline = 'CHOOSE'
QuestsTrackChoiceQuestSCString = 'I need to choose between %(trackA)s and %(trackB)s.'
QuestsTrackChoiceQuestMaybeSCString = 'Maybe I should choose %s.'
QuestsTrackChoiceQuestString = 'Choose between %(trackA)s and %(trackB)s'
QuestsFriendQuestHeadline = 'FRIEND'
QuestsFriendQuestSCString = 'Beacon'
QuestsFriendQuestString = 'Discovering The Underground'
QuestsMailboxQuestHeadline = 'MAIL'
QuestsMailboxQuestSCString = 'Franky'
QuestsMailboxQuestString = 'Petey K.'
QuestsPhoneQuestHeadline = 'CLARABELLE'
QuestsPhoneQuestSCString = 'Boombox'
QuestsPhoneQuestString = 'Mild Mannered Reporter'
QuestsFriendNewbieQuestString = 'Make %d friends %d laff or less'
QuestsFriendNewbieQuestProgress = '%(progress)s of %(numFriends)s made'
QuestsFriendNewbieQuestObjective = 'Make friends with %d new Toons'
QuestsTrolleyQuestHeadline = 'TROLLEY'
QuestsTrolleyQuestSCString = 'The Twelfth Fish'
QuestsTrolleyQuestString = 'April Fool\'s Day Party'
QuestsTrolleyQuestStringShort = 'Plasma Glow Wave'
QuestsMinigameNewbieQuestString = '%d Minigames'
QuestsMinigameNewbieQuestProgress = '%(progress)s of %(numMinigames)s Played'
QuestsMinigameNewbieQuestObjective = 'Play %d minigames with new Toons'
QuestsMinigameNewbieQuestSCString = 'Cowbell'
QuestsMinigameNewbieQuestCaption = 'Help a new Toon %d laff or less'
QuestsMinigameNewbieQuestAux = 'Play:'
QuestsMaxHpReward = 'Your Laff limit has been increased by %s.'
QuestsMaxHpRewardPoster = 'Reward: %s point Laff boost'
QuestsMoneyRewardSingular = 'O Berry Bush'
QuestsMoneyRewardPlural = 'You get %s jellybeans.'
QuestsMoneyRewardPosterSingular = 'Chester The Time Traveler'
QuestsMoneyRewardPosterPlural = 'Reward: %s jellybeans'
QuestsMaxMoneyRewardSingular = '101 Days of Fun'
QuestsMaxMoneyRewardPlural = 'You can now carry %s jellybeans.'
QuestsMaxMoneyRewardPosterSingular = 'Color Vote'
QuestsMaxMoneyRewardPosterPlural = 'Reward: Carry %s jellybeans'
QuestsMaxGagCarryReward = 'You get a %(name)s. You can now carry %(num)s gags.'
QuestsMaxGagCarryRewardPoster = 'Reward: %(name)s (%(num)s)'
QuestsMaxQuestCarryReward = 'You can now have %s ToonTasks.'
QuestsMaxQuestCarryRewardPoster = 'Reward: Carry %s ToonTasks'
QuestsTeleportReward = 'You now have teleport access to %s.'
QuestsTeleportRewardPoster = 'Reward: Teleport access to %s'
QuestsTrackTrainingReward = 'You can now train for "%s" gags.'
QuestsTrackTrainingRewardPoster = 'Christmas Party'
QuestsTrackProgressReward = 'You now have frame %(frameNum)s of the %(trackName)s track animation.'
QuestsTrackProgressRewardPoster = 'Reward: "%(trackName)s" track animation frame %(frameNum)s'
QuestsTrackCompleteReward = 'You may now carry and use "%s" gags.'
QuestsTrackCompleteRewardPoster = 'Reward: Final %s track training'
QuestsClothingTicketReward = 'Viking Opera'
QuestsClothingTicketRewardPoster = 'Water Balloons'
TIPQuestsClothingTicketReward = 'Tuba'
TIPQuestsClothingTicketRewardPoster = 'Rockhopper\'s Plants'
QuestsCheesyEffectRewardPoster = 'Reward: %s'
QuestsCogSuitPartReward = 'You now have a %(cogTrack)s %(part)s Cog Suit Part.'
QuestsCogSuitPartRewardPoster = 'Reward: %(cogTrack)s %(part)s Part'
QuestsStreetLocationThisPlayground = 'Adventure Party'
QuestsStreetLocationThisStreet = 'Penguin Play Awards'
QuestsStreetLocationNamedPlayground = 'in the %s playground'
QuestsStreetLocationNamedStreet = 'on %(toStreetName)s in %(toHoodName)s'
QuestsLocationString = '%(string)s%(location)s'
QuestsLocationBuilding = "%s's building is called"
QuestsLocationBuildingVerb = 'All-Access Pass'
QuestsLocationParagraph = '\x07%(building)s "%(buildingName)s"...\x07...%(buildingVerb)s %(street)s.'
QuestsGenericFinishSCString = 'Cadence\'s Autograph'
QuestsMediumPouch = 'Treasure Book'
QuestsLargePouch = 'Black Hoodie'
QuestsSmallBag = 'Propellor Cap'
QuestsMediumBag = 'Dessert Pizza'
QuestsLargeBag = 'Black Electric Guitar'
QuestsSmallBackpack = 'Mastering The Elements'
QuestsMediumBackpack = 'Elite Penguin Force'
QuestsLargeBackpack = 'Switchbox 3000'
QuestsItemDict = {1: ['Pair of Glasses', 'Pairs of Glasses', 'a '],
 2: ['Key', 'Keys', 'a '],
 3: ['Blackboard', 'Blackboards', 'a '],
 4: ['Book', 'Books', 'a '],
 5: ['Candy Bar', 'Candy Bars', 'a '],
 6: ['Piece of Chalk', 'Pieces of Chalk', 'a '],
 7: ['Recipe', 'Recipes', 'a '],
 8: ['Note', 'Notes', 'a '],
 9: ['Adding machine', 'Adding machines', 'an '],
 10: ['Clown car tire', 'Clown car tires', 'a '],
 11: ['Air pump', 'Air pumps', 'an '],
 12: ['Octopus ink', 'Octopus inks', 'some '],
 13: ['Package', 'Package', 'a '],
 14: ['Goldfish receipt', 'Goldfish receipts', 'a '],
 15: ['Goldfish', 'Goldfish', 'a '],
 16: ['Oil', 'Oils', 'some '],
 17: ['Grease', 'Greases', 'some '],
 18: ['Water', 'Waters', 'some '],
 19: ['Gear report', 'Gear reports', 'a '],
 20: ['Blackboard Eraser', 'Blackboard Erasers', 'a '],
 110: ['TIP Clothing Ticket', 'Clothing Tickets', 'a '],
 1000: ['Clothing Ticket', 'Clothing Tickets', 'a '],
 2001: ['Inner Tube', 'Inner Tubes', 'an '],
 2002: ['Monocle Prescription', 'Monocle Prescriptions', 'a '],
 2003: ['Eyeglass Frames', 'Eyeglass Frames', 'some '],
 2004: ['Monocle', 'Monocles', 'a '],
 2005: ['Big White Wig', 'Big White Wigs', 'a '],
 2006: ['Bushel of Ballast', 'Bushels of Ballast', 'a '],
 2007: ['Cog Gear', 'Cog Gears', 'a '],
 2008: ['Sea Chart', 'Sea Charts', 'a '],
 2009: ['Cruddy Clovis', 'Cruddy Clovi', 'a '],
 2010: ['Clean Clovis', 'Clean Clovi', 'a '],
 2011: ['Clock Spring', 'Clock Springs', 'a '],
 2012: ['Counter Weight', 'Counter Weights', 'a '],
 4001: ["Tina's Inventory", "Tina's Inventories", ''],
 4002: ["Yuki's Inventory", "Yuki's Inventories", ''],
 4003: ['Inventory Form', 'Inventory Forms', 'an '],
 4004: ["Fifi's Inventory", "Fifi's Inventories", ''],
 4005: ["Lumber Jack's Ticket", "Lumber Jack's Tickets", ''],
 4006: ["Tabitha's Ticket", "Tabitha's Tickets", ''],
 4007: ["Barry's Ticket", "Barry's Tickets", ''],
 4008: ['Cloudy Castanet', 'Cloudy Castanets', ''],
 4009: ['Blue Squid Ink', 'Blue Squid Ink', 'some '],
 4010: ['Clear Castanet', 'Clear Castanets', 'a '],
 4011: ["Leo's Lyrics", "Leo's Lyrics", ''],
 5001: ['Silk necktie', 'Silk neckties', 'a '],
 5002: ['Pinstripe Suit', 'Pinstripe Suits', 'a '],
 5003: ['Pair of Scissors', 'Pairs of Scissors', 'a '],
 5004: ['Postcard', 'Postcards', 'a '],
 5005: ['Pen', 'Pens', 'a '],
 5006: ['Inkwell', 'Inkwells', 'an '],
 5007: ['Notepad', 'Notepads', 'a '],
 5008: ['Office Lockbox', 'Office Lockboxes', 'an '],
 5009: ['Bag of Bird Seed', 'Bags of Bird Seed', 'a '],
 5010: ['Sprocket', 'Sprockets', 'a '],
 5011: ['Salad', 'Salads', 'a '],
 5012: ['Key to ' + lDaisyGardens, 'Keys to ' + lDaisyGardens, 'a '],
 5013: [lSellbotHQ + ' Blueprints', lSellbotHQ + 'Medieval Party', 'some '],
 5014: [lSellbotHQ + ' Memo', lSellbotHQ + ' Memos', 'a '],
 5015: [lSellbotHQ + ' Memo', lSellbotHQ + ' Memos', 'a '],
 5016: [lSellbotHQ + ' Memo', lSellbotHQ + ' Memos', 'a '],
 5017: [lSellbotHQ + ' Memo', lSellbotHQ + ' Memos', 'a '],
 3001: ['Soccer ball', 'Soccer balls', 'a '],
 3002: ['Toboggan', 'Toboggans', 'a '],
 3003: ['Ice cube', 'Ice cubes', 'an '],
 3004: ['Love letter', 'Love letters', 'a '],
 3005: ['Wiener dog', 'Wiener dogs', 'a '],
 3006: ['Engagement ring', 'Engagement rings', 'an '],
 3007: ['Sardine whiskers', 'Sardine whiskers', 'some '],
 3008: ['Calming potion', 'Calming potion', 'a '],
 3009: ['Broken tooth', 'Broken teeth', 'a '],
 3010: ['Gold tooth', 'Gold teeth', 'a '],
 3011: ['Pine cone bread', 'Pine cone breads', 'a '],
 3012: ['Lumpy cheese', 'Lumpy cheeses', 'some '],
 3013: ['Simple spoon', 'Simple spoons', 'a '],
 3014: ['Talking toad', 'Talking toad', 'a '],
 3015: ['Ice cream cone', 'Ice cream cones', 'an '],
 3016: ['Wig powder', 'Wig powders', 'some '],
 3017: ['Rubber ducky', 'Rubber duckies', 'a '],
 3018: ['Fuzzy dice', 'Fuzzy dice', 'some '],
 3019: ['Microphone', 'Microphones', 'a '],
 3020: ['Electric keyboard', 'Electric keyboards', 'an '],
 3021: ['Platform shoes', 'Platform shoes', 'some '],
 3022: ['Caviar', 'Caviar', 'some '],
 3023: ['Make-up powder', 'Make-up powders', 'some '],
 3024: ['Yarn', 'Yarn', 'some '],
 3025: ['Knitting Needle', 'Knitting Needles', 'a '],
 3026: ['Alibi', 'Alibis', 'an '],
 3027: ['External Temperature Sensor', 'External Temperature Sensors', 'an '],
 6001: ['Cashbot HQ Plans', 'Cashbot HQ Plans', 'some '],
 6002: ['Rod', 'Rods', 'a '],
 6003: ['Drive Belt', 'Drive Belts', 'a '],
 6004: ['Pair of Pincers', 'Pairs of Pincers', 'a '],
 6005: ['Reading Lamp', 'Reading Lamps', 'a '],
 6006: ['Zither', 'Zithers', 'a '],
 6007: ['Zamboni', 'Zambonis', 'a '],
 6008: ['Zebra Zabuton', 'Zebra Zabutons', 'a '],
 6009: ['Zinnias', 'Zinnias', 'some '],
 6010: ['Zydeco Records', 'Zydeco Records', 'some '],
 6011: ['Zucchini', 'Zucchinis', 'a '],
 6012: ['Zoot Suit', 'Zoot Suits', 'a '],
 7001: ['Plain Bed', 'Plain Beds', 'a '],
 7002: ['Fancy Bed', 'Fancy Beds', 'a '],
 7003: ['Blue Bedspread', 'Blue Bedspreads', 'a '],
 7004: ['Paisley Bedspread', 'Paisley Bedspreads', 'a '],
 7005: ['Pillows', 'Pillows', 'some '],
 7006: ['Hard Pillows', 'Hard Pillows', 'some '],
 7007: ['Pajamas', 'Pajamas', 'a pair of '],
 7008: ['Footie Pajamas', 'Footie Pajamas', 'a pair of '],
 7009: ['Puce Footie Pajamas', 'Puce Footie Pajamas', 'a pair of '],
 7010: ['Fuchsia Footie Pajamas', 'Fuchsia Footie Pajamas', 'a pair of '],
 7011: ['Cauliflower Coral', 'Cauliflower Coral', 'some '],
 7012: ['Slimy Kelp', 'Slimy Kelp', 'some '],
 7013: ['Pestle', 'Pestles', 'a '],
 7014: ['Jar of Wrinkle Cream', 'Jars of Wrinkle Cream', 'a ']}
QuestsHQOfficerFillin = lHQOfficerM
QuestsHQWhereFillin = ''
QuestsHQBuildingNameFillin = lToonHQ
QuestsHQLocationNameFillin = 'Cadence'
QuestsTailorFillin = 'Tailor'
QuestsTailorWhereFillin = ''
QuestsTailorBuildingNameFillin = 'Cloud Wave'
QuestsTailorLocationNameFillin = 'Ghost Sheet'
QuestsTailorQuestSCString = 'Cart Surfer'
QuestMovieQuestChoiceCancel = 'Keytar'
QuestMovieTrackChoiceCancel = 'X-treme Jetpack'
QuestMovieQuestChoice = 'Box Dimension'
QuestMovieTrackChoice = 'Gold Viking Helmet'
GREETING = 0
QUEST = 1
INCOMPLETE = 2
INCOMPLETE_PROGRESS = 3
INCOMPLETE_WRONG_NPC = 4
COMPLETE = 5
LEAVING = 6
TheBrrrghTrackQuestDict = {GREETING: '',
 QUEST: 'Gary The Gadget Guy',
 INCOMPLETE_PROGRESS: 'Rockhopper\'s Cannon',
 INCOMPLETE_WRONG_NPC: 'Multi-Player',
 COMPLETE: 'Fire Battle',
 LEAVING: 'Fired Up'}
QuestDialog_3225 = {QUEST: "Oh, thanks for coming, _avName_!\x07The Cogs in the neighborhood frightened away my delivery person.\x07I don't have anyone to deliver this salad to _toNpcName_!\x07Can you do it for me? Thanks so much!_where_"}
QuestDialog_2910 = {QUEST: 'Back so soon?\x07Great job on the spring.\x07The final item is a counter weight.\x07Stop by and see _toNpcName_ and bring back whatever you can get._where_'}
QuestDialogDict = {160: {GREETING: '',
       QUEST: "Goldsmith",
       INCOMPLETE_PROGRESS: TheCogs + 'Scroll',
       INCOMPLETE_WRONG_NPC: 'Volcano',
       COMPLETE: QuestsDefaultComplete,
       LEAVING: QuestsDefaultLeaving},
 161: {GREETING: '',
       QUEST: "Ready For Battle",
       INCOMPLETE_PROGRESS: TheCogs + 'Flying Flippers Emporium',
       INCOMPLETE_WRONG_NPC: 'Duel',
       COMPLETE: QuestsDefaultComplete,
       LEAVING: QuestsDefaultLeaving},
 162: {GREETING: '',
       QUEST: 'Concentrate',
       INCOMPLETE_PROGRESS: TheCogs + 'Interior Construction',
       INCOMPLETE_WRONG_NPC: 'Elements Hideout',
       COMPLETE: QuestsDefaultComplete,
       LEAVING: QuestsDefaultLeaving},
 163: {GREETING: '',
       QUEST: "Scavenger Hunt",
       INCOMPLETE_PROGRESS: TheCogs + 'Fire Wheel',
       INCOMPLETE_WRONG_NPC: 'Amulet Construction',
       COMPLETE: QuestsDefaultComplete,
       LEAVING: QuestsDefaultLeaving},
 164: {QUEST: 'You look like you could use some new gags.\x07Go see %s, maybe he can help you out._where_' % Flippy},
 165: {QUEST: 'Fire Dance'},
 166: {QUEST: 'Sketched Action'},
 167: {QUEST: 'Fire Guardian'},
 168: {QUEST: 'Hot Sauce Reserve'},
 169: {QUEST: 'Sketched: Volcano'},
 170: {QUEST: 'Nice work, now you know the difference between the 4 types of Cogs.\x07I think you are ready to start training for your third gag track.\x07Go talk to _toNpcName_ to choose your next gag track - he can give you some expert advice._where_'},
 171: {QUEST: 'Nice work, now you know the difference between the 4 types of Cogs.\x07I think you are ready to start training for your third gag track.\x07Go talk to _toNpcName_ to choose your next gag track - he can give you some expert advice._where_'},
 172: {QUEST: 'Nice work, now you know the difference between the 4 types of Cogs.\x07I think you are ready to start training for your third gag track.\x07Go talk to _toNpcName_ to choose your next gag track - she can give you some expert advice._where_'},
 175: {GREETING: '',
       QUEST: "Orange Sky",
       INCOMPLETE_PROGRESS: 'Sketched: Enter',
       COMPLETE: 'Amulet',
       LEAVING: QuestsDefaultLeaving},
 400: {GREETING: '',
       QUEST: 'A New Journey',
       INCOMPLETE_PROGRESS: 'Fire Door & Key',
       INCOMPLETE_WRONG_NPC: 'Sensei Fire',
       COMPLETE: 'Fire Ninja',
       LEAVING: QuestsDefaultLeaving},
 1039: {QUEST: 'Visit _toNpcName_ if you want to get around town more easily._where_'},
 1040: {QUEST: 'Visit _toNpcName_ if you want to get around town more easily._where_'},
 1041: {QUEST: 'Monkey King' + lToontownCentral + ' if you help out a friend of mine.\x07Seems the Cogs are causing trouble over on Loopy Lane.  Go visit _toNpcName_._where_'},
 1042: {QUEST: 'Jet Pack Pilot' + lToontownCentral + ' if you help out a friend of mine.\x07Seems the Cogs are causing trouble over on Loopy Lane.  Go visit _toNpcName_._where_'},
 1043: {QUEST: 'Fairy Princess' + lToontownCentral + ' if you help out a friend of mine.\x07Seems the Cogs are causing trouble over on Loopy Lane.  Go visit _toNpcName_._where_'},
 1044: {QUEST: 'Puffle Grooming',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Halloween Costumes'},
 1045: {QUEST: 'Costume Show',
        LEAVING: '',
        COMPLETE: 'Bean Counters' + lToontownCentral + 'Soccer Match' + lToontownCentral + '.'},
 1046: {QUEST: 'The Cashbots have really been bothering the Funny Money Savings and Loan.\x07Stop by there and see if there is anything you can do._where_'},
 1047: {QUEST: 'Earth Day Recycling',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Penguin Play Awards'},
 1048: {QUEST: 'Wow!  Thanks for finding our adding machines.\x07Hm... They look a little damaged.\x07Say, could you take them over to _toNpcName_ over at her shop, "Tickle Machines" on this street?\x07See if she can fix them.',
        LEAVING: ''},
 1049: {QUEST: "Goal!",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Bamboo Forest Sketch'},
 1053: {QUEST: "The Mine Cave is Safe!",
        LEAVING: '',
        COMPLETE: "Mine Cave Construction"},
 1054: {QUEST: '_toNpcName_ needs some help with his clown cars._where_'},
 1055: {QUEST: "The Fair" + lToontownCentral + 'Guardian Dog',
        GREETING: 'Woohoo!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Hockey Gear'},
 1056: {QUEST: 'Fan-flying-tastic!  Now I can get this old clown car on the road again!\x07Hey, I thought I had an air pump around here to inflate these tires...\x07Maybe _toNpcName_ borrowed it?\x07Could you go ask for it back for me?_where_',
        LEAVING: ''},
 1057: {QUEST: "Puffle Show",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Holiday Gifts'},
 1058: {QUEST: "Good job - I knew you could do it.\x07Here's the pump.  I'm sure _toNpcName_ will be glad to get it back.",
        LEAVING: '',
        GREETING: '',
        COMPLETE: "Holiday Activities"},
 1059: {QUEST: '_toNpcName_ is running low on supplies.  Maybe you can give him a hand?_where_'},
 1060: {QUEST: "Stadium",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Igloo Items'},
 1061: {QUEST: "Elite Penguin Sketch" + lToontownCentral + 'Music Jam',
        LEAVING: '',
        COMPLETE: 'Festival of Flight',
        INCOMPLETE_PROGRESS: 'Test Glider'},
 1062: {QUEST: "Fancy Formal Wear" + lToontownCentral + 'Puffle Paddle',
        LEAVING: '',
        COMPLETE: 'The Docks',
        INCOMPLETE_PROGRESS: 'Orange Puffle'},
 900: {QUEST: 'I hear _toNpcName_ needs help with a package._where_'},
 1063: {QUEST: 'Community Tree',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Community Garden'},
 1067: {QUEST: "That's it, all right!\x07Hey, the address is smudged...\x07All I can read is that it's for a Dr. - the rest is all blurry.\x07Maybe it's for _toNpcName_?  Could you take it to him?_where_",
        LEAVING: ''},
 1068: {QUEST: "Island Adventure Party" + lToontownCentral + '.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Shops in Igloos"},
 1069: {QUEST: "Seafarer's Gown",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Music Jam Dancers'},
 1070: {QUEST: "Music Jam Rock Stage",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Music Jam Pop Stage'},
 1071: {QUEST: "Underwater Adventure",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Norman Swarm'},
 1072: {QUEST: 'Great - you got it back!\x07Maybe you should try _toNpcName_, it could be for him._where_',
        LEAVING: ''},
 1073: {QUEST: 'Oh, thanks for bringing me my packages.\x07Wait a second, I was expecting two.  Could you check with _toNpcName_ and see if he has the other one?',
        INCOMPLETE: 'Puffle Rescuer',
        LEAVING: ''},
 1074: {QUEST: 'Everyday Phoning Facility',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Jet Packs'},
 1075: {QUEST: 'I guess there was a second package after all!\x07Hurry and take it over to _toNpcName_ with my apologies.',
        COMPLETE: 'Pumpkin Igloo',
        LEAVING: ''},
 1076: {QUEST: "There's been some trouble over at 14 Karat Goldfish.\x07_toNpcName_ could probably use a hand._where_"},
 1077: {QUEST: "Treasure Hunt Adventure",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Destroyed PSA HQ'},
 1078: {QUEST: "Oh, you have my fish!\x07Huh?  What's this - a receipt?\x07Sigh, I guess they are Cogs, after all.\x07I can't make heads or tails out of this receipt.  Could you take it to _toNpcName_ and see if he can read it?_where_",
        INCOMPLETE: 'What did _toNpcName_ have to say about the receipt?',
        LEAVING: ''},
 1079: {QUEST: "Captains",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "April Fools"},
 1092: {QUEST: "The Great Snow Maze",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Jacques Hammer"},
 1080: {QUEST: "Throne of April Fools",
        LEAVING: '',
        COMPLETE: 'The Test',
        INCOMPLETE_PROGRESS: 'Cloud Maker 3000'},
 1081: {QUEST: '_toNpcName_ appears to be in a sticky situation. He sure could use a hand._where_'},
 1082: {QUEST: "Super Exclusives",
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: 'Rockslide at the Mine'},
 1083: {QUEST: "Mer-penguins",
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: 'Puffer Fish'},
 1084: {QUEST: "Garden Hose",
        LEAVING: '',
        GREETING: '',
        COMPLETE: "Fixing the Mine Shack",
        INCOMPLETE_PROGRESS: 'Puffle Circus'},
 1085: {QUEST: '_toNpcName_ is conducting some research on the Cogs.\x07Go talk to him if you want to help out._where_'},
 1086: {QUEST: "Puffle Play Sketch",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Dragon Statue"},
 1089: {QUEST: "Popcorn Party",
        INCOMPLETE: 'White Puffle Room',
        COMPLETE: "Good work _avName_, we'll take this one from here.",
        LEAVING: ''},
 1090: {QUEST: '_toNpcName_ has some useful information for you._where_'},
 1091: {QUEST: 'Green Puffle Sketch',
        COMPLETE: 'Fishbowl Igloo',
        LEAVING: ''},
 401: {GREETING: '',
       QUEST: 'Ship Battle Adventure',
       INCOMPLETE_PROGRESS: 'Elite Penguin Force',
       INCOMPLETE_WRONG_NPC: 'Rockhopper\'s Notice Board',
       COMPLETE: 'Squid Lid',
       LEAVING: QuestsDefaultLeaving},
 2201: {QUEST: 'Those sneaky Cogs are at it again.\x07_toNpcName_ has reported another missing item. Stop by and see if you can straighten it out._where_'},
 2202: {QUEST: "Hi, _avName_. Thank goodness you're here. A mean looking Penny Pincher was just in here and he made off with an inner tube.\x07I fear they may use it for their vile purposes.\x07Please see if you can find him and bring it back.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Hidden Lake',
        COMPLETE: 'Orange Puffle Wagon'},
 2203: {QUEST: TheCogs + ' are wreaking havoc over at the bank.\x07Go see Captain Carl and see what you can do._where_'},
 2204: {QUEST: "Welcome aboard, matey.\x07Argh! Those rapscallion Cogs smashed my monocle and I can't sort me change without it.\x07Be a good landlubber and take this prescription to _toNpcName_ and fetch me a new one._where_",
        GREETING: '',
        LEAVING: ''},
 2205: {QUEST: "Haunted House",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Fire Dragon'},
 2206: {QUEST: 'Excellent!\x07Just a second...\x07Your prescription is filled. Please take this monocle straight to Captain Carl._where_',
        GREETING: '',
        LEAVING: '',
        COMPLETE: "Puffle Rescue: Underground"},
 2207: {QUEST: "Barnacle Barbara has a Cog in her shop!\x07You'd better get over there pronto._where_"},
 2208: {QUEST: "Double Necked Guitar",
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: "Puffle Rescue: Ice Floes",
        COMPLETE: "Spy Phone"},
 2209: {QUEST: 'Melville is preparing for an important voyage.\x07Pop in and see what you can do to help sort him out._where_'},
 2210: {QUEST: "I can use your help.\x07I've been asked by Toon HQ to take a voyage and see if I can find where the Cogs are coming from.\x07I'll need a few things for my ship but I don't have many jellybeans.\x07Stop by and pick up some ballast from Alice. You'll have to do a favor for her to get it._where_",
        GREETING: 'Howdy, _avName_',
        LEAVING: ''},
 2211: {QUEST: "Dance Contest",
        INCOMPLETE_PROGRESS: 'Crab Costume',
        GREETING: 'Puffle Washer',
        LEAVING: ''},
 2212: {QUEST: "A deal's a deal.\x07Here's your ballast for that cheapskate Melville._where_",
        GREETING: 'Green Jackhammer',
        LEAVING: ''},
 2213: {QUEST: "Excellent work. I knew she'd be reasonable.\x07Next I'll need a sailing chart from Art.\x07I don't think my credit is good there either so you'll have to work something out with him._where_",
        GREETING: '',
        LEAVING: ''},
 2214: {QUEST: "The Veggie Villain",
        INCOMPLETE_PROGRESS: "Island Lifter 3000",
        GREETING: 'Welcome!',
        LEAVING: 'Flare'},
 2215: {QUEST: "Ooh! These gears will do rather nicely.\x07Here's the chart. Give it to Melville with my compliments._where_",
        GREETING: '',
        LEAVING: '',
        COMPLETE: "Popcorn Device"},
 901: {QUEST: "If you're up for it Ahab could use some assistance over at his place..._where_"},
 2902: {QUEST: "Are you the new recruit?\x07Good, good. Maybe you can help me.\x07I'm building a giant prefab crab to confuse the Cogs.\x07I could use a clovis though. Go see Claggart and bring one back, please._where_"},
 2903: {QUEST: "Hi there!\x07Yes, I heard about the giant crab Ahab's working on.\x07The best clovis I have is a little on the dirty side though.\x07Be a sport and run it by the cleaners for me before you drop it off._where_",
        LEAVING: 'Thanks!'},
 2904: {QUEST: 'You must be the one that Claggart sent over.\x07I think I can clean that up in short order.\x07Just a minute...\x07There you are. Good as new!\x07Tell Ahab I said hello._where_'},
 2905: {QUEST: "Ah, now this is exactly what I was looking for.\x07While you're here, I'm also going to need a very large clock spring.\x07Take a walk over to Hook's place and see if he has one._where_"},
 2906: {QUEST: "Field-Ops"},
 2907: {QUEST: "Let's have a look then...\x07Smashing. Simply Smashing.\x07Sometimes I even surprise myself.\x07Here you go: one large spring for Ahab!_where_",
        LEAVING: 'Recipe for Disaster'},
 2911: {QUEST: "I'd be happy to help the cause, _avName_.\x07But I'm afraid the streets are no longer safe.\x07Why don't you go take out some Cashbot Cogs and we'll talk.",
        INCOMPLETE_PROGRESS: 'Elite Agent'},
 2916: {QUEST: 'Aunt Arctic Sketch',
        INCOMPLETE_PROGRESS: 'Yeti Cave'},
 2921: {QUEST: "Shocktopus",
        INCOMPLETE_PROGRESS: "Puffle Rescue: Underwater"},
 2925: {QUEST: "All done?\x07Well, I guess it's safe enough now.\x07Here's the counter weight for Ahab._where_"},
 2926: {QUEST: "Hidden Lake Lock",
        INCOMPLETE_PROGRESS: 'Knight\'s Quest',
        COMPLETE: 'Spooky Igloo Contest'},
 3200: {QUEST: "I just got a call in from _toNpcName_.\x07He's having a hard day. Maybe you can help him out!\x07Drop by and see what he needs._where_"},
 3201: {QUEST: 'Oh, thanks for coming!\x07I need someone to take this new silk tie to _toNpcName_.\x07Would you be able to do that for me?_where_'},
 3203: {QUEST: 'Halloween Countdown!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Stormy Skies",
        COMPLETE: '5th Anniversary Party'},
 3204: {QUEST: "_toNpcName_ just called to report a theft.\x07Why don't you stop by and see if you can sort things out?_where_"},
 3205: {QUEST: "Hello, _avName_! Have you come to help me?\x07I just chased a Bloodsucker out of my shop. Whew! That was scary.\x07But now I can't find my scissors anywhere! I'm sure that Bloodsucker took them.\x07Find that Bloodsucker, and recover my scissors for me.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: '5th Anniversary Cake',
        COMPLETE: '5th Anniversary Yearbook'},
 3206: {QUEST: 'It sounds like _toNpcName_ is having problems with some Cogs.\x07Go see if you can help him out._where_'},
 3207: {QUEST: 'Hi, _avName_! Thanks for coming by!\x07A bunch of Double Talkers just broke in and stole a stack of postcards from my counter.\x07Please go out and defeat all those Double Talkers to get my postcards back!',
        INCOMPLETE_PROGRESS: "Snowball Fight!",
        COMPLETE: 'Find Four'},
 3208: {QUEST: "Cozy Ski Lodge" + lDaisyGardens + '.'},
 3209: {QUEST: 'Book Room Adventures' + lDaisyGardens + 'Holiday Decorations!'},
 3247: {QUEST: "Halloween Forest" + lDaisyGardens + '.'},
 3210: {QUEST: 'Brown Puffle Rocket',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Fun at the Fair!"},
 3211: {QUEST: "Ski Hill Challenge",
        INCOMPLETE_PROGRESS: 'Holiday Party Skating',
        COMPLETE: 'Treasure!'},
 3212: {QUEST: '_toNpcName_ needs some help looking for something she lost.\x07Go visit her and see what you can do._where_'},
 3213: {QUEST: 'Hi, _avName_. Can you help me?\x07I seem to have misplaced my pen. I think maybe some Cogs took it.\x07Defeat Cogs to find my stolen pen.',
        INCOMPLETE_PROGRESS: 'Lumberjack Look'},
 3214: {QUEST: "Pink Sparkle Snowshoes",
        INCOMPLETE_PROGRESS: "Holiday Tree 2010"},
 3215: {QUEST: "Fill the Lighthouse!",
        INCOMPLETE_PROGRESS: 'Wilderness Machine'},
 3216: {QUEST: "Expedition Boat",
        INCOMPLETE_PROGRESS: 'Wilderness Expedition Cave',
        COMPLETE: 'Water Party Prep'},
 3217: {QUEST: "Water Dance"},
 3218: {QUEST: 'Stamp Collectors'},
 3219: {QUEST: 'Explore the Wilderness'},
 3244: {QUEST: "Coins for Change 2010!"},
 3245: {QUEST: 'Penguin Colors'},
 3246: {QUEST: 'Fairy Fables'},
 3220: {QUEST: "I just heard that _toNpcName_ was asking around for you.\x07Why don't you drop by and see what she wants?_where_"},
 3221: {QUEST: 'Hi, _avName_! There you are!\x07I heard you were quite an expert in squirt attacks.\x07I need someone to set a good example for all the Toons in ' + lDaisyGardens + 'Penguins That Time Forgot'},
 3222: {QUEST: "EPF Sketch"},
 3223: {QUEST: 'Cove Stories'},
 3224: {QUEST: 'Orange Circus Puffle',
        COMPLETE: 'You did it, _avName_!\x07You demonstrated your superior Toonmanship.',
        GREETING: ''},
 3225: {QUEST: "_toNpcName_ says she needs some help.\x07Why don't you go see what you can do to help out?_where_"},
 3235: {QUEST: "Oh, this is the salad I ordered!\x07Thank you for bringing it to me.\x07All those Cogs must have frightened away _toNpcName_'s regular delivery person again.\x07Why don't you do us a favor and defeat some of the Cogs out there?\x07Defeat 10 Cogs in " + lDaisyGardens + ' and then report back to _toNpcName_.',
        INCOMPLETE_PROGRESS: "Hydro Hopper",
        COMPLETE: 'Igloo Party!',
        INCOMPLETE_WRONG_NPC: "Go tell _toNpcName_ about the Cogs you've defeated._where_"},
 3236: {QUEST: 'Life Underwater'},
 3237: {QUEST: 'Herbert\'s Monologue'},
 3238: {QUEST: 'Paint By Letters' + lDaisyGardens + 'Enemy Bots'},
 3239: {QUEST: "Fireworks" + lDaisyGardens + 'Secret Agent'},
 3242: {QUEST: 'Popcorn Explosion' + lDaisyGardens + 'EPF Tech Agent'},
 3243: {QUEST: "Sumo Smash" + lDaisyGardens + 'Walk Your Puffle'},
 3240: {QUEST: "I've just heard from _toNpcName_ that a Legal Eagle stole a bag of his bird seed.\x07Defeat Legal Eagles until you recover Bud's bird seed, and take it to him.\x07Legal Eagles are only found inside Lawbot buildings._where_",
        COMPLETE: 'inventive Brown Puffle',
        INCOMPLETE_WRONG_NPC: 'Good job getting that bird seed back!\x07Now take it to _toNpcName_._where_'},
 3241: {QUEST: 'Holiday Party Tree'},
 3250: {QUEST: 'EPF Enemies'},
 3251: {QUEST: "Tall Tree Maze"},
 3252: {QUEST: "Sled 'n Slide"},
 3253: {QUEST: "Underwater at the Stage"},
 3254: {QUEST: "Wilderness Expedition Travel",
        COMPLETE: "Catch the Mullet!"},
 3255: {QUEST: '_toNpcName_ is investigating Sellbot Headquarters.\x07Go see if you can help._where_'},
 3256: {QUEST: '_toNpcName_ is investigating Sellbot Headquarters.\x07Go see if you can help._where_'},
 3257: {QUEST: '_toNpcName_ is investigating Sellbot Headquarters.\x07Go see if you can help._where_'},
 3258: {QUEST: 'Great Puffle Circus'},
 3259: {QUEST: 'Intense Black Puffle'},
 3260: {QUEST: 'Brown Puffle Storyboard'},
 3261: {QUEST: 'Excellent job _avName_! What does the memo say?\x07"Attn Sellbots:"\x07"Toons have somehow found a way to infiltrate Sellbot Towers."\x07"I\'ll call you tonight during dinner to give you the details."\x07"Signed, Telemarketer"\x07Hmmm... I wonder how Toons are breaking in....\x07Please bring back one more memo and I think we\'ll have enough info for now.',
        COMPLETE: 'I knew you could do it! Ok, the memo says....\x07"Attn Sellbots:"\x07"I was having lunch with Mr. Hollywood yesterday."\x07"He reports that the V.P. is very busy these days."\x07"He will only be taking appointments from Cogs that deserve a promotion."\x07"Forgot to mention, Gladhander is golfing with me on Sunday."\x07"Signed, Name Dropper"\x07Well... _avName_, this has been very helpful.\x07Here is your reward.'},
 3262: {QUEST: "_toNpcName_ has some new information about the Sellbot HQ Factory.\x07Go see what he's got._where_"},
 3263: {GREETING: 'Java Jump',
        QUEST: 'Master the Elements',
        LEAVING: 'Fairy Fables Stage',
        COMPLETE: 'Creative Puffles'},
 4001: {GREETING: '',
        QUEST: 'Goofy Green Puffle',
        INCOMPLETE_PROGRESS: 'EPF Test Room',
        INCOMPLETE_WRONG_NPC: 'Snowball Battle',
        COMPLETE: 'Fabulous Purple Puffle',
        LEAVING: QuestsDefaultLeaving},
 4002: {GREETING: '',
        QUEST: 'Water Party Sketch',
        INCOMPLETE_PROGRESS: 'Zany Orange Puffle',
        INCOMPLETE_WRONG_NPC: 'Sporty Pink Puffle',
        COMPLETE: 'Wii Game Day "Goal!"',
        LEAVING: QuestsDefaultLeaving},
 4200: {QUEST: "I bet Tom could use some help with some research he's doing._where_"},
 4201: {GREETING: 'Howdy!',
        QUEST: "I'm very concerned about a rash of musical instrument theft.\x07I'm conducting a survey among my fellow merchants.\x07Perhaps I can find a pattern to help me crack this case.\x07Stop by and ask Tina for a concertina inventory._where_"},
 4202: {QUEST: 'Yes, I talked to Tom this morning.\x07I have the inventory right here.\x07Bring it right back to him, ok?_where_'},
 4203: {QUEST: "Great! One down...\x07Now swing by and get Yuki's._where_"},
 4204: {QUEST: 'Epic White Puffle',
        INCOMPLETE_PROGRESS: 'Awesome Blue Puffle',
        GREETING: ''},
 4205: {QUEST: 'Ah, there you are.\x07Thanks for giving me some time.\x07Take this to Tom and tell him I said Hello._where_'},
 4206: {QUEST: "Hmmm, very interesting.\x07Now we are getting somewhere.\x07Ok, the last inventory is Fifi's._where_"},
 4207: {QUEST: "Inventory?\x07How can I do an inventory if I don't have the form?\x07Go see Cleff and see if he has one for me._where_",
        INCOMPLETE_PROGRESS: '"Feed a Puffle"'},
 4208: {QUEST: "Ninja Battle",
        GREETING: 'The Mystery of Sensei',
        LEAVING: 'Master the Elements',
        INCOMPLETE_PROGRESS: "Brown Puffle"},
 4209: {GREETING: '',
        QUEST: 'Mmmm...\x07Dem mighty nice!\x07Here be your form for Fifi._where_'},
 4210: {GREETING: '',
        QUEST: "Thank you. That's a big help.\x07Let's see...Fiddles: 2\x07All done! Off you go!_where_",
        COMPLETE: "Great work, _avName_.\x07I'm sure I'll get to the bottom of these thefts now.\x07Why don't you get to the bottom of this!"},
 4211: {QUEST: 'Say, Dr. Fret keeps calling every five minutes. Can you go see what his problem is?_where_'},
 4212: {QUEST: "Fire Wave",
        INCOMPLETE_PROGRESS: 'Black Puffles in Cart Surfer'},
 4213: {QUEST: "Mountain Expedition",
        INCOMPLETE_PROGRESS: "Climbing the Mountain"},
 4214: {GREETING: '',
        LEAVING: '',
        QUEST: "Top of Toughest Mountain",
        INCOMPLETE_PROGRESS: 'Cart Surfer Stamps',
        COMPLETE: "Stamp Book"},
 4215: {QUEST: "Anna desperately needs someone to help her.\x07Why don't you drop in and see what you can do._where_"},
 4216: {QUEST: "Stormy Sky",
        INCOMPLETE_PROGRESS: 'Water Wave Sketches'},
 4217: {QUEST: "Oh, great. You found it!\x07Now be a trooper and run in by Jack's for me, would you?_where_"},
 4218: {QUEST: "Great Googely Moogely!\x07Alaska here I come!\x07I can't take these infernal Cogs anymore.\x07Say, I think Anna needs you again._where_"},
 4219: {QUEST: "Storm Baffles Gary",
        INCOMPLETE_PROGRESS: "Water Ninja"},
 4220: {QUEST: 'Sweet!\x07Could you swing this one by his place for me too?_where_'},
 4221: {GREETING: '',
        LEAVING: 'The First Rainstorm',
        QUEST: "Cool, daddio!\x07Now I'm in fat city, _avName_.\x07Before you split, you better go check out Anna Banana again..._where_"},
 4222: {QUEST: "Ninja Face-off",
        INCOMPLETE_PROGRESS: "C'mon, _avName_.\x07Barry is counting on you."},
 4223: {QUEST: "This should put a smile on Barry's face._where_"},
 4224: {GREETING: '',
        LEAVING: '',
        QUEST: 'Hello, Hello, HELLO!\x07Terrific!\x07I just know me and the boys are going to clean up this year.\x07Anna says to swing back by and get your reward._where_\x07Goodbye, Goodbye, GOODBYE!',
        COMPLETE: 'Thanks for all your help, _avName_.\x07You really are an asset here in Toontown.\x07Speaking of assets...'},
 902: {QUEST: 'Go see Leo.\x07He needs someone to deliver a message for him._where_'},
 4903: {QUEST: 'Dude!\x07My castanets are all cloudy and I have a big show tonight.\x07Take them to Carlos and see if he can polish them up._where_'},
 4904: {QUEST: 'Earning the Water Suit',
        GREETING: 'Hola!',
        LEAVING: 'Adios!',
        INCOMPLETE_PROGRESS: "Water Pumping Gadget"},
 4905: {QUEST: "Preparing the Water Dojo",
        GREETING: 'Hola!',
        LEAVING: 'Adios!',
        INCOMPLETE_PROGRESS: 'Gate to the Water Dojo'},
 4906: {QUEST: 'Bery good!\x07Here are de castanets for Leo._where_'},
 4907: {GREETING: '',
        QUEST: "Cool, dude!\x07They look awesome!\x07Now I need you to get a copy of the lyrics to 'A Beat Christmas' from Hedy._where_"},
 4908: {QUEST: "Water Suit"},
 4909: {QUEST: "Sign From The Elements"},
 4910: {QUEST: 'All done!\x07Sorry it took so long.\x07Take this back to Leo._where_',
        GREETING: '',
        COMPLETE: 'Sensei - Master of Water'},
 5247: {QUEST: 'This neighborhood is pretty tough...\x07You might want to learn some new tricks.\x07_toNpcName_ taught me everything I know, so maybe he can help you too._where_'},
 5248: {GREETING: 'Water Ninja Poster Sketch',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Water Ninja Sketch',
        QUEST: 'Water Beats Fire Sketch'},
 5249: {GREETING: 'Mmmmm.',
        QUEST: 'Blast',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Flare'},
 5250: {GREETING: '',
        LEAVING: '',
        QUEST: 'Chirp',
        INCOMPLETE_PROGRESS: 'Pop'},
 5258: {GREETING: '',
        LEAVING: '',
        QUEST: 'Loop',
        INCOMPLETE_PROGRESS: 'Flit'},
 5259: {GREETING: '',
        LEAVING: '',
        QUEST: 'Bouncer',
        INCOMPLETE_PROGRESS: 'Ed McCool and Destructo'},
 5260: {GREETING: '',
        LEAVING: '',
        QUEST: 'Niblet',
        INCOMPLETE_PROGRESS: 'Snowy Night'},
 5200: {QUEST: 'Those sneaky Cogs are at it again.\x07_toNpcName_ has reported another missing item. Stop by and see if you can straighten it out._where_'},
 5201: {GREETING: '',
        QUEST: 'Hi, _avName_.  I reckon I should thank you for coming.\x07A group of those Head Hunters came in and stole my soccer ball.\x07The leader told me that I had to make some cutbacks and just grabbed it away from me!\x07Can you get my ball back?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Puffles on the Loose',
        COMPLETE: 'Cadence and the Keeper'},
 5261: {GREETING: '',
        QUEST: 'Hi, _avName_.  I reckon I should thank you for coming.\x07A group of those Two-Faces came in and stole my soccer ball.\x07The leader told me that I had to make some cutbacks and just grabbed it away from me!\x07Can you get my ball back?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Golden puffle',
        COMPLETE: 'Meteor puffle'},
 5262: {GREETING: '',
        QUEST: 'Hi, _avName_.  I reckon I should thank you for coming.\x07A group of those Money Bags came in and stole my soccer ball.\x07The leader told me that I had to make some cutbacks and just grabbed it away from me!\x07Can you get my ball back?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Rainbow puffle',
        COMPLETE: 'Abominable snow puffle'},
 5263: {GREETING: '',
        QUEST: 'Hi, _avName_.  I reckon I should thank you for coming.\x07A group of those Spin Doctors came in and stole my soccer ball.\x07The leader told me that I had to make some cutbacks and just grabbed it away from me!\x07Can you get my ball back?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Black Puffle',
        COMPLETE: 'Blue Puffle'},
 5202: {QUEST: lTheBrrrgh + " has been overrun with some of the toughest Cogs we've seen yet.\x07You will probably want to carry more gags around here.\x07I hear _toNpcName_ may have a large bag you can use to carry more gags._where_"},
 5203: {GREETING: 'Pink Puffle',
        QUEST: "Green Puffle",
        LEAVING: 'Purple Puffle',
        INCOMPLETE_PROGRESS: "Red Puffle"},
 5204: {GREETING: '',
        LEAVING: '',
        QUEST: "Is that my toboggan?  I don't see any bag here.\x07I think Bumpy Noggin was on the team... maybe he has it?_where_"},
 5205: {GREETING: 'Yellow Puffle',
        LEAVING: '',
        QUEST: "Puffle Round Up",
        INCOMPLETE_PROGRESS: "Fire Ninja Force"},
 5206: {GREETING: '',
        LEAVING: '',
        QUEST: "Ahhh, that feels much better!\x07So you're looking for Ted's bag, huh?\x07I think it ended up on Sam Simian's head after the crash._where_"},
 5207: {GREETING: 'Eeeep!',
        LEAVING: '',
        QUEST: 'Halloween Swamp',
        INCOMPLETE_PROGRESS: 'Prepare for Pumpkins',
        COMPLETE: 'Finding Rockhopper'},
 5208: {GREETING: '',
        LEAVING: 'Eeeek!',
        QUEST: 'Elite Puffle: Flare'},
 5209: {GREETING: 'Dude!',
        LEAVING: 'Later!',
        QUEST: "Giant Pearl",
        INCOMPLETE_PROGRESS: "Water Stamps",
        COMPLETE: "EPF Agents"},
 5210: {QUEST: '_toNpcName_ is secretly in love with someone in the neighborhood.\x07If you help her, she may reward you handsomely._where_'},
 5211: {GREETING: 'Puffle Rescue',
        QUEST: 'Fire Dojo Challenge',
        LEAVING: 'System Defender',
        INCOMPLETE_PROGRESS: 'Adventurous Red Puffle'},
 5264: {GREETING: 'G and the Machine',
        QUEST: 'Enemies of the System',
        LEAVING: 'Holiday Dojo Lights',
        INCOMPLETE_PROGRESS: 'Wii Rollin\' Riot'},
 5265: {GREETING: 'EPF Under Attack',
        QUEST: 'Elite Comm Class Agents',
        LEAVING: 'Brown Puffle Cliff',
        INCOMPLETE_PROGRESS: 'Coins for Change Goal!'},
 5266: {GREETING: 'Sensei Water Battle',
        QUEST: 'Green Puffles in Jet Pack Adve',
        LEAVING: 'Water Dojo',
        INCOMPLETE_PROGRESS: 'White Puffle'},
 5212: {QUEST: 'Yarr',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Keeper of the Boiler Room"},
 5213: {GREETING: "Mobile Fire 1",
        QUEST: "Mobile Snow 1",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Mobile Water 1'},
 5214: {GREETING: '',
        LEAVING: 'Toodleloo!',
        QUEST: "Thank you for bringing back my little beauties.\x07Let's take a look at your letter now...\nMmmm, it seems I have yet another secret admirer.\x07This calls for a trip to my dear friend Carl.\x07I'm sure you'll like him immensely._where_"},
 5215: {GREETING: 'Mobile Fire Power Card 1Contents',
        LEAVING: 'Puffle Species',
        INCOMPLETE_PROGRESS: "Blue",
        QUEST: "About Puffles"},
 5216: {QUEST: 'Puffle Card',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Puffle Fun',
        COMPLETE: 'What Is A Puffle?'},
 5217: {QUEST: 'It sounds like _toNpcName_ could use some help._where_'},
 5218: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Puffles are small, round, furry creatures. Each color is unique. And they make great pets!",
        QUEST: "Most species are native to the wilds of Club Penguin, but some were discovered far away."},
 5219: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Personality",
        QUEST: "Toys"},
 5220: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Observed',
        QUEST: "in the Wild"},
 5221: {GREETING: '',
        LEAVING: '',
        QUEST: "You know what, maybe it isn't the Cogs at all!\x07Could you ask Fanny to make me a soothing potion?  Maybe that would help...._where_"},
 5222: {LEAVING: '',
        QUEST: "Favorite Snack",
        INCOMPLETE_PROGRESS: 'Best Game'},
 5223: {QUEST: 'Cool Fact',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Would you like to purchase a new puffle?'},
 5224: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Puffle Quiz',
        QUEST: "Which puffle is the most like you?",
        COMPLETE: "Stats"},
 5225: {QUEST: 'Ever since the incident with the turnip bread, Grumpy Phil has been mad at _toNpcName_.\x07Maybe you could help Gus fix things between them?_where_'},
 5226: {QUEST: 'Name',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Weight'},
 5227: {QUEST: "That's terrific!  Go tell Phil what you've done._where_"},
 5228: {QUEST: 'Personality',
        GREETING: 'Mmmmrrphh.',
        LEAVING: 'Toy',
        INCOMPLETE_PROGRESS: 'Favorite Game'},
 5229: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Adopt",
        QUEST: "Ready to adopt"},
 5267: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "your new puffle?",
        QUEST: "Name Ideas"},
 5268: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Adopt",
        QUEST: "Feeding"},
 5269: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Bathing",
        QUEST: "Grooming"},
 5230: {GREETING: '',
        QUEST: "Manual",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'I, agree to adopt for 400 coins.'},
 5270: {GREETING: '',
        QUEST: "You currently have coins.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Yes'},
 5271: {GREETING: '',
        QUEST: "No",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Walk'},
 5272: {GREETING: '',
        QUEST: "Igloo",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'you\'d make a great puffle owner.'},
 5231: {QUEST: "Adopt",
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'I, agree to adopt for 400 coins.'},
 5232: {QUEST: "Ready to adopt your new healthy, happy puffle?",
        LEAVING: '',
        GREETING: ''},
 5233: {QUEST: "Adopt",
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Adventerous, extreme",
        COMPLETE: "Sporty, cheery"},
 903: {QUEST: 'You may be ready to see _toNpcName_ the Blizzard Wizard for your final test._where_'},
 5234: {GREETING: '',
        QUEST: 'Fabulous, particular',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Intense, strong'},
 5278: {GREETING: '',
        QUEST: 'Playful, funny',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Shy, powerful, gentle'},
 5235: {GREETING: '',
        QUEST: 'Creative, spontaneous',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Curious, unpredictable, zany'},
 5279: {GREETING: '',
        QUEST: 'Super smart, inventive',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Loyal, content, team player'},
 5236: {GREETING: '',
        QUEST: 'TBD',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Your puffle will let you know when it is happy, sad, tired or hungry.'},
 5237: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Click the Food tab to feed it, the Play tab to get its toys, or the Care tab to groom, walk, or ask your puffle to sleep.',
        QUEST: "Oh, that is certainly a talking toad.  Give him to me.\x07What's that you say, toad?\x07Uh huh.\x07Uh huh...\x07The toad has spoken.  We need dessert.\x07Bring us some ice cream cones from _toNpcName_.\x07The toad likes red bean flavored ice cream for some reason._where_"},
 5238: {GREETING: '',
        QUEST: "If you want to look at the Handbook or read/print your pet's Adoption Certificate, click \"Pet Papers\".",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'If you care for your puffle, it\'ll be in your igloo. If it isn\'t happy and healthy, it will return to its natural habitat.'},
 5280: {GREETING: '',
        QUEST: "Care",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Certificate'},
 5239: {QUEST: "Feed",
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Handbook'},
 5240: {GREETING: '',
        QUEST: 'Play',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Pet Papers'},
 5281: {GREETING: '',
        QUEST: 'Caring for your Puffle',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Play'},
 5241: {QUEST: 'Puffles can dig up coins around the island. So walk a puffle wherever you go!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'The longer you\'ve cared for your puffle, the more it will find!'},
 5242: {GREETING: '',
        QUEST: 'Catchin\' Waves',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Dance Contest',
        COMPLETE: 'Aqua Grabber'},
 5243: {QUEST: 'Sweaty Pete is starting to stink up the street.\x07Can you talk him into taking a shower or something?_where_'},
 5244: {GREETING: '',
        QUEST: "DJ3K",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Cart Surfer"},
 5245: {GREETING: '',
        QUEST: 'Jet Pack Adventure',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Walk'},
 5246: {QUEST: "Puffles love to walk with you, one at a time. They'll even dance when you do!",
        LEAVING: '',
        COMPLETE: "Treasure",
        INCOMPLETE_PROGRESS: "Puffles love to play in your igloo. Give them their favorite toy! Or decorate with puffle furniture!"},
 5251: {QUEST: 'Lounge Lassard is supposed to be playing a gig tonight.\x07I hear he might be having some trouble with his equipment._where_'},
 5252: {GREETING: '',
        QUEST: 'Red',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Pink"},
 5253: {GREETING: '',
        QUEST: "Purple",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Black'},
 5273: {GREETING: '',
        QUEST: "Green",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'White'},
 5274: {GREETING: '',
        QUEST: "Yellow",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Orange'},
 5275: {GREETING: '',
        QUEST: "Brown",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Care'},
 5254: {GREETING: '',
        QUEST: "Games",
        LEAVING: '',
        COMPLETE: "Play",
        INCOMPLETE_PROGRESS: "Walk"},
 5282: {GREETING: '',
        QUEST: "They're known for their awesome team work. Few realize that each week blue puffles eat their weight in cookies.",
        LEAVING: '',
        COMPLETE: "From the wilds of Rockhopper Island, they love adventure. Puffle experts wonder what secrets they hold.",
        INCOMPLETE_PROGRESS: "It is said that the pink puffle's fur can hold 30 times its weight in water."},
 5283: {GREETING: '',
        QUEST: "The flash of a disco ball transforms this stylish puffle into a powerful dance force.",
        LEAVING: '',
        COMPLETE: "Although mostly quiet, sudden fiery outbursts show there is more to these intense creatures than meets the eye.",
        INCOMPLETE_PROGRESS: "Are experts on unicycles. They are"},
 5284: {GREETING: '',
        QUEST: "also known for their love of",
        LEAVING: '',
        COMPLETE: "April Fool's parties.",
        INCOMPLETE_PROGRESS: "It may be smaller than all other puffles, but its power is unmeasurable"},
 5255: {QUEST: 'You look like you could use more Laff points.\x07Maybe _toNpcName_ could sort you out._where_'},
 5256: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "It is rumored that the yellow puffle creates artwork from food and furniture.",
        QUEST: "This species has teeth strong enough to demolish petrified Puffle O's. And everything else."},
 5276: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "It is documented that the brown puffle blinks more than all other puffles. Its dreams have graph paper backgrounds.",
        QUEST: "Loyal, team player"},
 5257: {GREETING: '',
        LEAVING: '',
        COMPLETE: "Adventurous, extreme",
        INCOMPLETE_PROGRESS: "Athletic, cheery",
        QUEST: "Fabulous, particular"},
 5277: {GREETING: '',
        LEAVING: '',
        COMPLETE: "Intense, strong",
        INCOMPLETE_PROGRESS: "Playful, funny",
        QUEST: "Shy, powerful, gentle"},
 5301: {QUEST: "I can't help you with Laff points, but maybe _toNpcName_ will cut you a deal.\x07He's a little on tempermental side though..._where_"},
 5302: {GREETING: '',
        LEAVING: '',
        COMPLETE: "Creative, spontaneous",
        INCOMPLETE_PROGRESS: 'Curious, zany',
        QUEST: 'Smart, inventive'},
 5303: {QUEST: lTheBrrrgh + " is teeming with very dangerous Cogs.\x07If I were you, I'd carry more gags around here.\x07I hear _toNpcName_ can make you a large bag if you are willing to do the legwork._where_"},
 5304: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Ball, snowballs',
        QUEST: "Bowling pins, cannon"},
 5305: {GREETING: 'Howdy!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Skipping rope, snorkel, trampoline",
        QUEST: "Disco ball, bubble wand"},
 5306: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Skateboard',
        QUEST: "Propeller Cap, unicycle"},
 5307: {GREETING: '',
        LEAVING: 'Ice skates, snowflakes',
        INCOMPLETE_PROGRESS: "Paintbrush, easel",
        QUEST: "Box, wagon, truck",
        COMPLETE: "Beakers, rockets"},
 5308: {GREETING: '',
        LEAVING: '',
        QUEST: 'I hear _toNpcName_ is having some legal troubles.\x07Can you stop by and check it out?_where_'},
 5309: {GREETING: "Rallying teams together",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Hunting for buried treasure',
        QUEST: "Using bubblegum to float"},
 5310: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Bursting into flames after eating Puffle O\'s',
        QUEST: "Thanks. I feel a little better now.\x07 But there is one more thing...\x07Could you drop by _toNpcName_'s and get me an alibi?_where_"},
 5311: {GREETING: 'WHAAAA!!!!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Vacuums up cookies",
        QUEST: "with its mouth"},
 5312: {GREETING: 'Finally!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '',
        COMPLETE: "Makes music that gets everyone dancing",
        QUEST: "Super! You'd better run these back to _toNpcName_!"},
 6201: {QUEST: 'Powers Erge needs some help. Could you drop by and lend her a hand?_where_'},
 6202: {GREETING: '',
        LEAVING: '',
        QUEST: "Choosing just the right outfit for just the right occasion",
        INCOMPLETE_PROGRESS: "Freezes liquid at will",
        COMPLETE: "Good job on those Cogs, _avName_.\x07Now, are you sure I can't interest you in some electricity? Might come in handy....\x07No? OK, suit yourself.\x07Hunh? Oh yeah, I remember. Here ya go. This is sure to help with those nasty Cogs.\x07Keep up the good work!"},
 6206: {QUEST: "Well, _avName_, I don't have anything for you right now.\x07Wait! I think Susan Siesta was looking for help. Why don't you go see her?_where_"},
 6207: {GREETING: '',
        LEAVING: '',
        QUEST: "I'll never get rich with those darn Cogs driving away all my business!\x07You've got to help me, _avName_.\x07Clear out a few Cog buildings for the sake of the neighborhood and I'll add to your riches.",
        INCOMPLETE_PROGRESS: "Making quick decisions",
        COMPLETE: "Superior machine"},
 6211: {QUEST: 'Hey _avName_! I heard Lawful Linda was looking for you.\x07You should stop by and pay her a visit._where_'},
 6212: {GREETING: '',
        LEAVING: '',
        QUEST: "building skills",
        INCOMPLETE_PROGRESS: 'Favorite Place'},
 6213: {GREETING: '',
        LEAVING: '',
        QUEST: "Pretzels",
        INCOMPLETE: "Stinky cheese"},
 6214: {GREETING: '',
        LEAVING: '',
        QUEST: "Watermelon",
        INCOMPLETE_PROGRESS: 'Fish burger',
        COMPLETE: "Tacos"},
 6221: {QUEST: 'I heard Rocco was looking for help. See what you can do for him._where_'},
 6222: {GREETING: '',
        LEAVING: '',
        QUEST: "Performing and creating",
        INCOMPLETE_PROGRESS: "Hey, _avName_, what's up wid youse?\x07You gotta keep after dem Bossbots. We got a deal, remember?\x07Rocco always keeps his word.",
        COMPLETE: "Yo, _avName_! Youse ok in my book.\x07Dem Bossbots ain't so bossy now, is they?\x07Here ya go! A nice big boost. Now, you stay outta trouble, ya hear!"},
 6231: {QUEST: 'Nat over on Pajama Place heard rumors about a Cashbot Headquarters.\x07Head over there and see if you can help him out._where_'},
 6232: {GREETING: '',
        LEAVING: '',
        QUEST: "I got a nibble about some strange goings on.\x07Well, maybe it's the fleas but something is going on anyway.\x07All these Cashbots!\x07I think they've opened another headquarters right off Pajama Place.\x07P.J. knows his way around.\x07Go see _toNpcName_ _where_ Ask him if he's heard anything.",
        INCOMPLETE_PROGRESS: "Hummus and pita"},
 6233: {GREETING: '',
        LEAVING: '',
        QUEST: "Hey there _avName_, where are you headed?\x07Cashbot Headquarters?? I haven't seen anything.\x07Could you go to the end of Pajama Place and see if it's true?\x07Find some Cashbot Cogs in their headquarters, defeat a few of them, and come tell me about it.",
        INCOMPLETE_PROGRESS: "Yogurt parfait"},
 6234: {GREETING: '',
        LEAVING: '',
        QUEST: "Socks",
        INCOMPLETE_PROGRESS: "Astronaut ice cream"},
 6235: {GREETING: '',
        LEAVING: '',
        QUEST: "Can bounce really high",
        INCOMPLETE_PROGRESS: "Originally from",
        COMPLETE: "Rockhopper Island"},
 6241: {QUEST: "The Countess has been looking everywhere for you! Please pay her a visit so she'll stop calling._where_"},
 6242: {GREETING: '',
        LEAVING: '',
        QUEST: "_avName_, I'm counting on you to help me!\x07You see, these Cogs are making so much noise that I simply can't concentrate.\x07I keep losing count of my sheep!\x07If you'll cut down on the noise, I'll help you out too! You can count on it!\x07Now, where was I? Right, one hundred thirty-six, one hundred thirty-seven....",
        INCOMPLETE_PROGRESS: "Loves to exercise and swim",
        COMPLETE: "Super good at skateboarding"},
 6251: {QUEST: "Poor Zari broke her zipper and now she can't make deliveries to her customers. She could sure use your help._where_"},
 6252: {GREETING: '',
        LEAVING: '',
        QUEST: "Oh, hi _avName_. You're here to help with my deliveries?\x07That's terrific! This broken zipper makes it tough to zip around.\x07Let me see...ok, this should be easy. Cowboy George ordered a zither last week.\x07Could you please bring it over to him? _where_",
        INCOMPLETE_PROGRESS: 'Laughs an average of 14.7 times a day'},
 6253: {GREETING: '',
        LEAVING: '',
        QUEST: "Wears a beret to paint",
        INCOMPLETE_PROGRESS: "Uses a sleep mask for beauty rest"},
 6254: {GREETING: '',
        LEAVING: '',
        QUEST: "That was fast. What's next on my list?\x07Right. Master Mike ordered a Zamboni. That zany guy.\x07Could you bring this to him, please?_where_",
        INCOMPLETE_PROGRESS: 'That Zamboni needs to go to Master Mike._where_'},
 6255: {GREETING: '',
        LEAVING: '',
        QUEST: "Slightly smaller than",
        INCOMPLETE_PROGRESS: 'other species'},
 6256: {GREETING: '',
        LEAVING: '',
        QUEST: "Rumored to eat fridges whole",
        INCOMPLETE_PROGRESS: "Afraid of balloons"},
 6257: {GREETING: '',
        LEAVING: '',
        QUEST: "So, Master Mike was happy with his Zamboni? Great.\x07Who's next? Oh, Zen Glen ordered a zebra-striped zabuton.\x07Here it is! Could you zoom over to his place, please?_where_",
        INCOMPLETE_PROGRESS: 'Catchin\' Waves'},
 6258: {GREETING: '',
        LEAVING: '',
        QUEST: "Aqua Grabber",
        INCOMPLETE_PROGRESS: 'Cart Surfer'},
 6259: {GREETING: '',
        LEAVING: '',
        QUEST: 'Peace and quiet at last. Thanks, _avName_.\x07Please tell Zari how happy I am. OM....',
        INCOMPLETE_PROGRESS: 'DJ3K'},
 6260: {GREETING: '',
        LEAVING: '',
        QUEST: "I'm glad to hear that Zen Glen is happy with his zebra zabuton.\x07Oh, these zinnias just came in for Rose Petals.\x07Since you seem to have some zeal for deliveries, perhaps you could take them over to her?_where_",
        INCOMPLETE_PROGRESS: "Dance Contest"},
 6261: {GREETING: '',
        LEAVING: '',
        QUEST: 'What lovely zinnias! Zari sure does deliver.\x07Oh, well, I guess YOU deliver, _avName_. Please thank Zari for me!',
        INCOMPLETE_PROGRESS: "Snow Forts"},
 6262: {GREETING: '',
        LEAVING: '',
        QUEST: "Welcome back, _avName_. You're pretty zippy.\x07Let's see...what's next on my list to deliver? Zydeco records for Wyda Wake._where_",
        INCOMPLETE_PROGRESS: "Are you sure you want to return to its natural habitat?"},
 6263: {GREETING: '',
        LEAVING: '',
        QUEST: "Zydeco records? I don't remember asking for Zydeco records.\x07Oh, I bet Lullaby Lou ordered them._where_",
        INCOMPLETE_PROGRESS: 'No, those Zydeco records are for Lullaby Lou._where_'},
 6264: {GREETING: '',
        LEAVING: '',
        QUEST: "Your puffle was returned successfully.",
        INCOMPLETE_PROGRESS: "Ok"},
 6265: {GREETING: '',
        LEAVING: '',
        QUEST: "Zucchini? Hmm. Well, someone will want it, I'm sure.\x07Ok, we're nearly done with my list. One more delivery to make.\x07Babyface MacDougal ordered a zoot suit._where_",
        INCOMPLETE_PROGRESS: "Your coins:"},
 6266: {GREETING: '',
        LEAVING: '',
        QUEST: "0",
        INCOMPLETE_PROGRESS: 'This certifies that',
        COMPLETE: "belongs to:"},
 6271: {QUEST: "Drowsy Dave is having some trouble that you might be able to help with. Why don't you stop by his shop?_where_"},
 6272: {GREETING: '',
        LEAVING: '',
        QUEST: "Adopted on:/2",
        INCOMPLETE_PROGRESS: "Zzzzz...huh? Oh, it's you, _avName_.\x07Back already? I was just taking a little nap.\x07Come back when you're done with those buildings.",
        COMPLETE: "What? I dropped off to sleep for a minute there.\x07Now that those Cog buildings are gone I can finally relax.\x07Thanks for your help, _avName_.\x07See you later! I think maybe I'll take a little nap."},
 6281: {QUEST: "Head over and call on Teddy Blair. He's got a job for you._where_"},
 6282: {GREETING: '',
        LEAVING: '',
        QUEST: "Do you want to take for a walk or back to your igloo?",
        INCOMPLETE_PROGRESS: "Pizza Parlor",
        COMPLETE: "You had fun? Huh? Oh!\x07You're done! Great. Really nice of you to help out this way.\x07I found this in the back room but I don't have any use for it.\x07Maybe you'll find something to do with it. So long, _avName_!"},
 6291: {QUEST: 'The Dojo'},
 6292: {QUEST: 'Jet Pack Adventure',
        INCOMPLETE_PROGRESS: 'Buy a membership',
        COMPLETE: "Print"},
 7201: {QUEST: 'Nina Nightlight was looking for you, _avName_. She needs some help._where_'},
 7202: {GREETING: '',
        LEAVING: '',
        QUEST: "Oh! I'm so glad to see you, _avName_. I could use some help!\x07Those darn Cogs have kept the delivery folks away and I have no beds in stock.\x07Could you go see Hardy O'Toole and bring me back a bed?_where_ ",
        INCOMPLETE_PROGRESS: "To adopt and care for more than 2 puffles, you must",
        COMPLETE: ''},
 7203: {GREETING: '',
        LEAVING: '',
        QUEST: 'become a member.',
        INCOMPLETE_PROGRESS: 'We\'d love to have you join!',
        COMPLETE: ''},
 7204: {GREETING: '',
        LEAVING: '',
        QUEST: "OOPS!",
        INCOMPLETE_PROGRESS: "Popcorn",
        COMPLETE: ''},
 7205: {GREETING: '',
        LEAVING: '',
        QUEST: "Ok",
        INCOMPLETE_PROGRESS: "Learn More",
        COMPLETE: ''},
 7206: {GREETING: '',
        LEAVING: '',
        QUEST: 'Hey there _avName_!\x07You did a bang-up job on those Cogs.\x07The bed is all ready. Could you please deliver it for me?\x07Now that those Cogs are gone, business will be brisk!',
        INCOMPLETE_PROGRESS: "Everyone can adopt 2 puffles (red and blue).",
        COMPLETE: 'What a lovely bed!\x07Now my customers will be happy. Thanks, _avName_.\x07Say, you might be able to use this. Someone left it here.'},
 7209: {QUEST: 'Go see Honey Moon. She needs some help._where_'},
 7210: {GREETING: '',
        LEAVING: '',
        QUEST: "Oh! I'm so glad to see you, _avName_. I really need some help!\x07I haven't been able to get my beauty sleep for ages. You see, those Cogs stole my bedspread.\x07Say, could you please run over and see if Ed's got anything in blue?_where_",
        INCOMPLETE_PROGRESS: 'And members can adopt every color',
        COMPLETE: ''},
 7211: {GREETING: '',
        LEAVING: '',
        QUEST: "- up to!",
        INCOMPLETE_PROGRESS: 'Still working on this blue bedspread, _avName_. Keep at those Cogs!',
        COMPLETE: ''},
 7212: {GREETING: '',
        LEAVING: '',
        QUEST: "Auto Disconnect, your penguin has been idle for more than 10 minutes",
        INCOMPLETE_PROGRESS: 'You need more coins',
        COMPLETE: ''},
 7213: {GREETING: '',
        LEAVING: '',
        QUEST: "You can only have one Club Penguin window open at a time. Please close any other windows and tabs in your internet browser to connect.",
        INCOMPLETE_PROGRESS: 'The connection has been lost.',
        COMPLETE: ''},
 7214: {GREETING: '',
        LEAVING: '',
        QUEST: "Thank you for playing Club Penguin.",
        INCOMPLETE_PROGRESS: "Waddle on!",
        COMPLETE: ''},
 7215: {GREETING: '',
        LEAVING: '',
        QUEST: "Find out more",
        INCOMPLETE_PROGRESS: "Done",
        COMPLETE: "Oh! That's lovely! Paisley suits me quite well.\x07Time for my beauty sleep, then! So long, _avName_.\x07What? You're still here? Can't you see I'm trying to sleep?\x07Here, take this and let me rest. I must look a fright!"},
 7218: {QUEST: 'Dreamy Daphne could use a hand._where_'},
 7219: {GREETING: '',
        LEAVING: '',
        QUEST: "Oh, _avName_, I'm glad to see you! Those Cogs took my pillows.\x07Could you go see if Tex has some pillows?_where_\x07I'm sure he can help.",
        INCOMPLETE_PROGRESS: 'Sorry, that name is unavailable!',
        COMPLETE: ''},
 7220: {GREETING: '',
        LEAVING: '',
        QUEST: "Howdy! Daphne needs some pillows, huh? Well, you came to the right place, pardner!\x07More pillows in here than there's spines on a cactus.\x07Here you go, _avName_. Take these back over to Daphne with my compliments.\x07Always glad to help a gal out.",
        INCOMPLETE_PROGRESS: 'You already own the maximum number of puffles!',
        COMPLETE: ''},
 7221: {GREETING: '',
        LEAVING: '',
        QUEST: "Penguin is playing Aqua Grabber",
        INCOMPLETE_PROGRESS: 'Penguin is playing Astro Barrier',
        COMPLETE: ''},
 7222: {GREETING: '',
        LEAVING: '',
        QUEST: "Penguin is playing Bean Counters",
        INCOMPLETE_PROGRESS: "Penguin is Cart Surfing",
        COMPLETE: ''},
 7223: {GREETING: '',
        LEAVING: '',
        QUEST: "Penguin is Ice Fishing",
        INCOMPLETE_PROGRESS: "Penguin is flying a Jet Pack",
        COMPLETE: 'Penguin is playing Thin Ice'},
 7226: {QUEST: "Drop by to see Sandy Sandman. She's lost her pajamas._where_"},
 7227: {GREETING: '',
        LEAVING: '',
        QUEST: "I have no pajamas! They're missing!\x07What will I do? Oh! I know!\x07Go see Big Mama. She'll have pajamas for me._where_",
        INCOMPLETE_PROGRESS: 'Penguin is Surfing',
        COMPLETE: ''},
 7228: {GREETING: '',
        LEAVING: '',
        QUEST: "Hey there, little toon! Big Mama's got the best pajamas from the Bahamas.\x07Oh, something for Sandy Sandman, huh? Well, let me see what I've got.\x07Here's a little something. Now she can sleep in style!\x07Would you run these back over to her for me? I can't leave the shop just now.\x07Thanks, _avName_. See you around!",
        INCOMPLETE_PROGRESS: 'You need to take those pajamas to Sandy._where_',
        COMPLETE: ''},
 7229: {GREETING: '',
        LEAVING: '',
        QUEST: "Penguin is playing Hydro Hopper",
        INCOMPLETE_PROGRESS: 'Penguin is making pizzas',
        COMPLETE: ''},
 7230: {GREETING: '',
        LEAVING: '',
        QUEST: "Penguin is rounding up puffles",
        INCOMPLETE_PROGRESS: 'Penguin is playing Manacala',
        COMPLETE: ''},
 7231: {GREETING: '',
        LEAVING: '',
        QUEST: "Penguin is playing Find Four",
        INCOMPLETE_PROGRESS: "Penguin is in a Sled Race",
        COMPLETE: ''},
 7232: {GREETING: '',
        LEAVING: '',
        QUEST: "That's too bad. These are the only pajamas with feet I have.\x07Oh, I've got an idea. Go ask Cat. She may have some pajamas with feet._where_",
        INCOMPLETE_PROGRESS: "Nope, those are all the pajamas I've got. Go see what Cat has._where_",
        COMPLETE: ''},
 7233: {GREETING: '',
        LEAVING: '',
        QUEST: "Penguin is reading a Book",
        INCOMPLETE_PROGRESS: "Penguin is reading a Book",
        COMPLETE: ''},
 7234: {GREETING: '',
        LEAVING: '',
        QUEST: "Penguin is reading a Book",
        INCOMPLETE_PROGRESS: 'Penguin is Mixing Music',
        COMPLETE: ''},
 7235: {GREETING: '',
        LEAVING: '',
        QUEST: "Not puce either. Hmm....\x07By my whiskers, I know I have some other ones.\x07They'll take a little while to find. Let's make a deal.\x07I'll find the other pajamas if you'll get rid of some of these Cog buildings. They're very unsettling.\x07I'll have the pajamas ready when you get back, _avName_.",
        INCOMPLETE_PROGRESS: 'Penguin is digging for treasure',
        COMPLETE: ''},
 7236: {GREETING: '',
        LEAVING: '',
        QUEST: 'Penguin is playing Balloon Pop',
        INCOMPLETE_PROGRESS: "Sandy's waiting for those pajamas, _avName_.",
        COMPLETE: "Penguin is playing Ring The Bell"},
 7239: {QUEST: "Go see Smudgy Mascara. She's been looking for some help._where_"},
 7240: {GREETING: '',
        LEAVING: '',
        QUEST: 'Those darn Cogs took my wrinkle cream!\x07My customers simply MUST have wrinkle cream while I work on them.\x07Go see Rip and see if he has my special formula in stock._where_',
        INCOMPLETE_PROGRESS: 'Penguin is playing Feed-A-Puffle'},
 7241: {GREETING: '',
        LEAVING: '',
        QUEST: "Penguin is playing Memory Card Game",
        INCOMPLETE_PROGRESS: "Penguin is playing Puffle Paddle"},
 7242: {GREETING: '',
        LEAVING: '',
        QUEST: "Penguin is playing Puffle Shuffle",
        INCOMPLETE_PROGRESS: "Penguin is playing Puffle Soaker"},
 7243: {GREETING: '',
        LEAVING: '',
        QUEST: "Oooh! Very slimy kelp you've got there, _avName_.\x07Now, I just crush some pearls with the mortar and pestle.\x07Um, where's my pestle? What good is a mortar without a pestle?\x07I bet that darn Loan Shark took it when he came in here!\x07You need to help me find it! He was headed for Cashbot HQ!",
        INCOMPLETE_PROGRESS: 'Penguin is playing Spin To Win'},
 7244: {GREETING: '',
        LEAVING: '',
        QUEST: "Penguin is playing Card-Jitsu",
        INCOMPLETE_PROGRESS: "Penguin is playing Card-Jitsu Fire",
        COMPLETE: "Didn't Rip have a bigger jar of wrinkle cream than this? No?\x07Well, I guess I'll just order more when I run out.\x07So long, _avName_.\x07What? You're still here? Can't you see I'm trying to work?\x07Here, take this."},
 11000: {GREETING: '',
         LEAVING: '',
         QUEST: 'If you are interested in Lawbot disguise parts you should visit _toNpcName_.\x07I hear he could use some help with his weather research._where_'},
 11001: {GREETING: '',
         LEAVING: '',
         QUEST: 'Yes, yes. I have Lawbot disguise parts.\x07But they are of no interest to me.\x07The focus of my research is fluctuations in the ambient temperature of Toontown.\x07I will gladly trade you disguise parts for cog temperature sensors.\x07You can start on %s.' % GlobalStreetNames[2100][-1],
         INCOMPLETE_PROGRESS: 'Have you tried looking on %s?' % GlobalStreetNames[2100][-1],
         COMPLETE: 'Penguin is playing Card-Jitsu Water'},
 11002: {GREETING: '',
         LEAVING: '',
         QUEST: 'For more Lawbot disguise parts you should visit _toNpcName_ again.\x07I hear he needs more research assistants._where_'},
 11003: {GREETING: '',
         LEAVING: '',
         QUEST: 'More Lawbot disguise parts?\x07Well, if you insist...\x07but I will require another cog temperature sensor.\x07This time look on %s.' % GlobalStreetNames[2200][-1],
         INCOMPLETE_PROGRESS: 'You are looking on %s, right?' % GlobalStreetNames[2200][-1],
         COMPLETE: 'Penguin is challenging the Sensei'},
 11004: {GREETING: '',
         LEAVING: '',
         QUEST: 'If you need more Lawbot disguise parts you should return to _toNpcName_.\x07I hear he still needs help with his weather reasearch._where_'},
 11005: {GREETING: '',
         LEAVING: '',
         QUEST: "You're proving yourself quite useful!\x07Can you take a look on %s?" % GlobalStreetNames[2300][-1],
         INCOMPLETE_PROGRESS: "Are you sure you're looking on %s?" % GlobalStreetNames[2300][-1],
         COMPLETE: "Penguin is challenging the Sensei"},
 11006: {GREETING: '',
         LEAVING: '',
         QUEST: 'You-know-who needs more temperature readings.\x07Stop by if you would like another disguise part._where_'},
 11007: {GREETING: '',
         LEAVING: '',
         QUEST: 'Back again?\x07You are very dedicated...\x07The next stop is %s.' % GlobalStreetNames[1100][-1],
         INCOMPLETE_PROGRESS: 'Have you tried looking on %s?' % GlobalStreetNames[1100][-1],
         COMPLETE: 'Penguin is challenging the Sensei'},
 11008: {GREETING: '',
         LEAVING: '',
         QUEST: "If you're up for another Lawbot disguise part..._where_"},
 11009: {GREETING: '',
         LEAVING: '',
         QUEST: 'Fancy seeing you here!\x07Now I need readings on %s.' % GlobalStreetNames[1200][-1],
         INCOMPLETE_PROGRESS: 'You are looking on %s, right?' % GlobalStreetNames[1200][-1],
         COMPLETE: 'Penguin is in a Dance Contest!'},
 11010: {GREETING: '',
         LEAVING: '',
         QUEST: 'I believe _toNpcName_ has more work for you._where_'},
 11011: {GREETING: '',
         LEAVING: '',
         QUEST: 'Good to see you again, _avName_!\x07Can you get a reading on %s, please?' % GlobalStreetNames[1300][-1],
         INCOMPLETE_PROGRESS: 'Have you tried looking on %s?' % GlobalStreetNames[1300][-1],
         COMPLETE: "Penguin is Rescuing Puffles"},
 11012: {GREETING: '',
         LEAVING: '',
         QUEST: 'You know the drill._where_'},
 11013: {GREETING: '',
         LEAVING: '',
         QUEST: '_avName_, my dear friend!\x07Can you go to %s and find another temperature sensor?' % GlobalStreetNames[5100][-1],
         INCOMPLETE_PROGRESS: "Are you sure you're looking on %s?" % GlobalStreetNames[5100][-1],
         COMPLETE: "Penguin is playing System Defender"},
 11014: {GREETING: '',
         LEAVING: '',
         QUEST: "_toNpcName_ was asking for you by name.\x07It appears you've made quite an impression!_where_"},
 11015: {GREETING: '',
         LEAVING: '',
         QUEST: "Welcome back!\x07I've been waiting for you.\x07The next reading I need is on %s." % GlobalStreetNames[5200][-1],
         INCOMPLETE_PROGRESS: 'You are looking on %s, right?' % GlobalStreetNames[5200][-1],
         COMPLETE: "Penguin is playing Bits and Bolts"},
 11016: {GREETING: '',
         LEAVING: '',
         QUEST: 'If you need to finish your Lawbot disguise...\x07_toNpcName_ can help you out._where_'},
 11017: {GREETING: '',
         LEAVING: '',
         QUEST: 'Hello, Junior Research Scientist!\x07We still need readings from %s.' % GlobalStreetNames[5300][-1],
         INCOMPLETE_PROGRESS: 'Have you tried looking on %s?' % GlobalStreetNames[5300][-1],
         COMPLETE: 'Penguin is on an Adventure'},
 11018: {GREETING: '',
         LEAVING: '',
         QUEST: "_toNpcName_ has another job for you.\x07If you're not sick of him yet..._where_"},
 11019: {GREETING: '',
         LEAVING: '',
         QUEST: 'Well, then.\x07Are you ready for another recovery?\x07This time try %s.' % GlobalStreetNames[4100][-1],
         INCOMPLETE_PROGRESS: "Are you sure you're looking on %s?" % GlobalStreetNames[4100][-1],
         COMPLETE: 'Penguin is on an Adventure'},
 11020: {GREETING: '',
         LEAVING: '',
         QUEST: 'Are you still after Lawbot disguise parts?_where_'},
 11021: {GREETING: '',
         LEAVING: '',
         QUEST: 'You could probably guess by now...\x07but I need readings from %s.' % GlobalStreetNames[4200][-1],
         INCOMPLETE_PROGRESS: 'You are looking on %s, right?' % GlobalStreetNames[4200][-1],
         COMPLETE: 'Penguin is on an Adventure'},
 11022: {GREETING: '',
         LEAVING: '',
         QUEST: 'I hate to say it, but..._where_'},
 11023: {GREETING: '',
         LEAVING: '',
         QUEST: 'What do you think about %s? Could you get a sensor from there too?' % GlobalStreetNames[4300][-1],
         INCOMPLETE_PROGRESS: 'Have you tried looking on %s?' % GlobalStreetNames[4300][-1],
         COMPLETE: 'Another excellent job, _avName_'},
 11024: {GREETING: '',
         LEAVING: '',
         QUEST: 'Go visit the Professor if you still need disguise parts._where_'},
 11025: {GREETING: '',
         LEAVING: '',
         QUEST: 'I believe we still need a reading from %s.' % GlobalStreetNames[9100][-1],
         INCOMPLETE_PROGRESS: "Are you sure you're looking on %s?" % GlobalStreetNames[9100][-1],
         COMPLETE: 'Penguin is on an Adventure'},
 11026: {GREETING: '',
         LEAVING: '',
         QUEST: '_toNpcName_ has one final mission for you._where_'},
 11027: {GREETING: '',
         LEAVING: '',
         QUEST: 'Back so soon?\x07The final reading is on %s.' % GlobalStreetNames[9200][-1],
         INCOMPLETE_PROGRESS: 'You are looking on %s, right?' % GlobalStreetNames[9200][-1],
         COMPLETE: "Penguin is on an Adventure"},
 12000: {GREETING: '',
         LEAVING: '',
         QUEST: 'If you are interested in Bossbot disguise parts you should visit _toNpcName_._where_'},
 12001: {GREETING: '',
         LEAVING: '',
         QUEST: "Penguin is on an Adventure",
         INCOMPLETE_PROGRESS: "Penguin is on an Adventure",
         COMPLETE: "Penguin is on an Adventure"},
 12002: {GREETING: '',
         LEAVING: '',
         QUEST: "_toNpcName_ needs more help, if you're up for it._where_"},
 12003: {GREETING: '',
         LEAVING: '',
         QUEST: 'Penguin is on an Adventure',
         INCOMPLETE_PROGRESS: 'Penguin is on an Adventure',
         COMPLETE: "Penguin is on an Adventure"},
 12004: {GREETING: '',
         LEAVING: '',
         QUEST: "There's really only one place to go for Bossbot parts._where_"},
 12005: {GREETING: '',
         LEAVING: '',
         QUEST: 'Penguin is in the Town',
         INCOMPLETE_PROGRESS: 'Penguin is in the Coffee Shop',
         COMPLETE: "Penguin is in the Book Room"},
 12006: {GREETING: '',
         LEAVING: '',
         QUEST: '_toNpcName_ has more parts for you...'},
 12007: {GREETING: '',
         LEAVING: '',
         QUEST: "Penguin is in the Dance Club",
         INCOMPLETE_PROGRESS: 'Try looking on %s' % GlobalStreetNames[1100][-1],
         COMPLETE: "Penguin is in the Dance Lounge"},
 12008: {GREETING: '',
         LEAVING: '',
         QUEST: 'Head on over to..._where_'},
 12009: {GREETING: '',
         LEAVING: '',
         QUEST: "Penguin is in the Clothes Shop",
         INCOMPLETE_PROGRESS: 'Having trouble? Try looking on %s' % GlobalStreetNames[3100][-1],
         COMPLETE: "Penguin is in the Ski Village"},
 12010: {GREETING: '',
         LEAVING: '',
         QUEST: 'I think you know where to go by now..._where_'},
 12011: {GREETING: '',
         LEAVING: '',
         QUEST: 'Penguin is on top of the Mountain',
         INCOMPLETE_PROGRESS: 'Penguin is in the Sport Shop',
         COMPLETE: "Penguin is in the Plaza"},
 12012: {GREETING: '',
         LEAVING: '',
         QUEST: '_toNpcName_ needs more Bossbots.'},
 12013: {GREETING: '',
         LEAVING: '',
         QUEST: "Penguin is in the Pet Shop",
         INCOMPLETE_PROGRESS: 'Penguin is in the Dojo',
         COMPLETE: "Penguin is in the Dojo Courtyard"},
 12014: {GREETING: '',
         LEAVING: '',
         QUEST: 'If you want more disguise parts, go to..._where_'},
 12015: {GREETING: '',
         LEAVING: '',
         QUEST: 'Penguin is in Hiding',
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: "Penguin is in the Fire Dojo"},
 12016: {GREETING: '',
         LEAVING: '',
         QUEST: '_toNpcName_ was looking for you...'},
 12017: {GREETING: '',
         LEAVING: '',
         QUEST: 'Penguin is in the Water Dojo',
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: 'Penguin is in the Pizza Parlor'},
 12018: {GREETING: '',
         LEAVING: '',
         QUEST: 'Could you swing by..._where_'},
 12019: {GREETING: '',
         LEAVING: '',
         QUEST: 'Penguin is at the Beach',
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: 'Penguin is in the Lighthouse'},
 12020: {GREETING: '',
         LEAVING: '',
         QUEST: 'If you get a chance, stop by and see _toNpcName_.'},
 12021: {GREETING: '',
         LEAVING: '',
         QUEST: 'Penguin is at the Lighthouse Beacon',
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: "Penguin is on the Pirate Ship"},
 12022: {GREETING: '',
         LEAVING: '',
         QUEST: 'You know..._where_'},
 12023: {GREETING: '',
         LEAVING: '',
         QUEST: "Penguin is in the Pirate Ship Hold",
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: 'Penguin is in the Captain\'s Quarters'},
 12024: {GREETING: '',
         LEAVING: '',
         QUEST: "Penguin is in the Crow's Nest"},
 12025: {GREETING: '',
         LEAVING: '',
         QUEST: 'Penguin is at the Dock',
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: "Penguin is at the Snow Forts"},
 12026: {GREETING: '',
         LEAVING: '',
         QUEST: 'Please go see _toNpcName_ again.'},
 12027: {GREETING: '',
         LEAVING: '',
         QUEST: "Penguin is hiding",
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: "Penguin is hiding"},
 12028: {GREETING: '',
         LEAVING: '',
         QUEST: "Penguin is hiding"},
 12029: {GREETING: '',
         LEAVING: '',
         QUEST: 'Penguin is in the Everyday Phoning Facility',
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: 'Penguin is hiding'},
 12030: {GREETING: '',
         LEAVING: '',
         QUEST: '_toNpcName_ is starting to sound like a broken record...'},
 12031: {GREETING: '',
         LEAVING: '',
         QUEST: "Penguin is in the Boiler Room",
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: "Penguin is on the Iceberg (hidden on your map)"},
 12032: {GREETING: '',
         LEAVING: '',
         QUEST: 'Penguin is in the Cave (hidden underground)',
         INCOMPLETE_PROGRESS: 'Penguin is in the Mine (hidden underground)',
         COMPLETE: 'Penguin is in the Mine Shack'}}
ChatGarblerDog = ['woof', 'arf', 'rruff']
ChatGarblerCat = ['meow', 'mew']
ChatGarblerMouse = ['squeak', 'squeaky', 'squeakity']
ChatGarblerHorse = ['neigh', 'brrr']
ChatGarblerRabbit = ['eek',
 'eepr',
 'eepy',
 'eeky']
ChatGarblerDuck = ['quack', 'quackity', 'quacky']
ChatGarblerMonkey = ['ooh', 'ooo', 'ahh']
ChatGarblerBear = ['growl', 'grrr']
ChatGarblerPig = ['oink', 'oik', 'snort']
ChatGarblerDefault = ['blah']
Bossbot = 'Bossbot'
Lawbot = 'Lawbot'
Cashbot = 'Cashbot'
Sellbot = 'Sellbot'
BossbotS = 'Penguin is in the Forest'
LawbotS = 'Penguin is at the Cove'
CashbotS = 'Penguin is in the Box Dimension'
SellbotS = 'Penguin is digging for gold in the Gold Mine'
BossbotP = 'Bossbots'
LawbotP = 'Lawbots'
CashbotP = 'Cashbots'
SellbotP = 'Sellbots'
BossbotSkelS = 'Penguin is at the Hidden Lake'
LawbotSkelS = 'Penguin is in the Underwater Room'
CashbotSkelS = 'Penguin is in the University'
SellbotSkelS = 'Penguin is ???'
BossbotSkelP = 'Penguin is in an igloo'
LawbotSkelP = 'Penguin is in their igloo'
CashbotSkelP = 'Penguin is in your igloo'
SellbotSkelP = 'Would you like to addme to your ignore list?'
SkeleRevivePostFix = ' v2.0'
AvatarDetailPanelOK = lOK
AvatarDetailPanelCancel = lCancel
AvatarDetailPanelClose = lClose
AvatarDetailPanelLookup = 'Looking up details for %s.'
AvatarDetailPanelFailedLookup = 'Unable to get details for %s.'
AvatarDetailPanelPlayer = 'Player: %(player)s\nWorld: %(world)s'
AvatarDetailPanelPlayerShort = '%(player)s\nWorld: %(world)s\nLocation: %(location)s'
AvatarDetailPanelRealLife = 'Offline'
AvatarDetailPanelOnline = 'District: %(district)s\nLocation: %(location)s'
AvatarDetailPanelOnlinePlayer = 'District: %(district)s\nLocation: %(location)s\nPlayer: %(player)s'
AvatarDetailPanelOffline = 'Done'
AvatarShowPlayer = 'Would you like to removeme from your ignore list?'
OfflineLocation = 'Offline'
PlayerToonName = 'Toon: %(toonname)s'
PlayerShowToon = 'Done'
PlayerPanelDetail = 'Town'
AvatarPanelFriends = 'Friends'
AvatarPanelWhisper = 'Whisper'
AvatarPanelSecrets = 'Coffee Shop'
AvatarPanelGoTo = 'Book Room'
AvatarPanelPet = 'Dance Club'
AvatarPanelIgnore = 'Ignore'
AvatarPanelIgnoreCant = 'Okay'
AvatarPanelStopIgnoring = 'Dance Lounge'
AvatarPanelReport = 'Report'
AvatarPanelCogLevel = 'Level: %s'
AvatarPanelCogDetailClose = lClose
AvatarPanelDetail = 'Clothes Shop'
AvatarPanelGroupInvite = 'Invite'
AvatarPanelGroupRetract = 'Ski Village'
AvatarPanelGroupMember = 'Ski Lodge'
AvatarPanelGroupMemberKick = 'Remove'
ReportPanelTitle = 'Lodge Attic'
ReportPanelBody = 'This feature will send a complete report to a Moderator. Instead of sending a report, you might choose to do one of the following:\n\n  - Teleport to another district\n  - Use "Ignore" on the toon\'s panel\n\nDo you really want to report %s to a Moderator?'
ReportPanelBodyFriends = 'This feature will send a complete report to a Moderator. Instead of sending a report, you might choose to do one of the following:\n\n  - Teleport to another district\n  - Break your friendship\n\nDo you really want to report %s to a Moderator?\n\n(This will also break your friendship)'
ReportPanelCategoryBody = 'You are about to report %s. A Moderator will be alerted to your complaint and will take appropriate action for anyone breaking our rules. Please choose the reason you are reporting %s:'
ReportPanelBodyPlayer = 'Sport Shop'
ReportPanelCategoryLanguage = 'Mountain'
ReportPanelCategoryPii = 'Plaza'
ReportPanelCategoryRude = 'Pet Shop'
ReportPanelCategoryName = 'Dojo'
ReportPanelCategoryHacking = 'Hacking'
ReportPanelConfirmations = ('You are about to report that %s has used obscene, bigoted or sexually explicit language.',
 'You are about to report that %s is being unsafe by giving out or requesting a phone number, address, last name, email address, password or account name.',
 'You are about to report that %s is bullying, harassing, or using extreme behavior to disrupt the game.',
 "You are about to report that %s has created a name that does not follow Disney's House Rules.",
 'You are about to report that %s has hacked/tampered with the game or used third party software.')
ReportPanelWarning = "Dojo Courtyard"
ReportPanelThanks = 'Ninja Hideout'
ReportPanelRemovedFriend = 'We have automatically removed %s from your Toon Friends List.'
ReportPanelRemovedPlayerFriend = 'We have automatically removed %s as a Player friend so as such you will not see them as your friend in any Disney product.'
ReportPanelAlreadyReported = 'You have already reported %s during this session. A Moderator will review your previous report.'
IgnorePanelTitle = 'Fire Dojo'
IgnorePanelAddIgnore = 'Would you like to ignore %s for the rest of this session?'
IgnorePanelIgnore = 'You are now ignoring %s.'
IgnorePanelRemoveIgnore = 'Would you like to stop ignoring %s?'
IgnorePanelEndIgnore = 'You are no longer ignoring %s.'
IgnorePanelAddFriendAvatar = '%s is your friend, you cannot ignore them while you are friends.'
IgnorePanelAddFriendPlayer = '%s (%s)is your friend, you cannot ignore them while you are friends.'
PetPanelFeed = 'Feed'
PetPanelCall = 'Call'
PetPanelGoTo = 'Water Dojo'
PetPanelOwner = 'Pizza Parlor'
PetPanelDetail = 'Stage'
PetPanelScratch = 'Scratch'
PetDetailPanelTitle = 'Beach'
PetTrickStrings = {0: 'Jump',
 1: 'Beg',
 2: 'Lighthouse',
 3: 'Rollover',
 4: 'Backflip',
 5: 'Dance',
 6: 'Speak'}
PetMoodAdjectives = {'neutral': 'neutral',
 'hunger': 'hungry',
 'boredom': 'bored',
 'excitement': 'excited',
 'sadness': 'sad',
 'restlessness': 'restless',
 'playfulness': 'playful',
 'loneliness': 'lonely',
 'fatigue': 'tired',
 'confusion': 'confused',
 'anger': 'angry',
 'surprise': 'surprised',
 'affection': 'affectionate'}
SpokenMoods = {'neutral': 'neutral',
 'hunger': ["I'm tired of JellyBeans! How'bout giving me a slice of pie?", "How'bout a Red JellyBean? I'm tired of the Green ones!", "Oh, those JellyBeans were for planting?!! But I'm hungry!"],
 'boredom': ["I'm dying of boredom over here!", "You didn't think I understood you, huh?", 'Could we, like, DO something already?'],
 'excitement': ["Wow, it's you, it's you, it's you!",
                'Beacon',
                'Pirate Ship',
                "Ship Hold"],
 'sadness': ["Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go...", "I'll be good, I promise!", "I don't know WHY I'm sad, I just am!!!"],
 'restlessness': ["I'm sooo restless!!!"],
 'playfulness': ["Let's play, Let's play, Let's play, Let's play, Let's play, Let's play, Let's play, Let's play, Let's play...", 'Play with me or I dig up some flowers!', 'Lets run around and  around and around and around and around and around...'],
 'loneliness': ['Where have you been?', 'Wanna cuddle?', 'I want to go with you when you fight Cogs!'],
 'fatigue': ['That swim in the pond really tired me out!', 'Being a Doodle is exhausting!', 'I gotta get to Dreamland!'],
 'confusion': ['Where am I? Who are you again?', "What's a Toon-up again?", "Whoa, I'm standing between you and the Cogs! Run away!"],
 'anger': ['... and you wonder why I never give you a Toon-up?!!!', 'You always leave me behind!', 'You love your gags more than you love me!'],
 'surprise': ['Of course Doodles can talk!', 'Toons can talk?!!', 'Whoa, where did you come from?'],
 'affection': ["You're the best Toon EVER!!!!!!!!!!", 'Do you even KNOW how great you are?!?', 'I am SO lucky to be with you!!!']}
DialogQuestion = '?'
FriendsListLabel = 'Friends'
TeleportPanelOK = lOK
TeleportPanelCancel = lCancel
TeleportPanelYes = lYes
TeleportPanelNo = lNo
TeleportPanelCheckAvailability = 'Trying to go to %s.'
TeleportPanelNotAvailable = '%s is busy right now; try again later.'
TeleportPanelIgnored = '%s is ignoring you.'
TeleportPanelNotOnline = "%s isn't online right now."
TeleportPanelWentAway = '%s went away.'
TeleportPanelUnknownHood = "You don't know how to get to %s!"
TeleportPanelUnavailableHood = '%s is not available right now; try again later.'
TeleportPanelDenySelf = "Captain's Quarters"
TeleportPanelOtherShard = "%(avName)s is in district %(shardName)s, and you're in district %(myShardName)s.  Do you want to switch to %(shardName)s?"
TeleportPanelBusyShard = '%(avName)s is in a full District. Playing in a full District can severely slow down game performance. Are you sure you want to switch districts?'
BattleBldgBossTaunt = "Crow's Nest"
CogdoBattleBldgBossTaunt = "Dock"
FactoryBossTaunt = "Snow Forts"
FactoryBossBattleTaunt = 'Stadium'
MintBossTaunt = "HQ"
MintBossBattleTaunt = 'EPF Command Room'
StageBossTaunt = "The Facility"
StageBossBattleTaunt = 'Everyday Phoning Facility'
CountryClubBossTaunt = "VR Room"
CountryClubBossBattleTaunt = 'Boiler Room'
ForcedLeaveCountryClubAckMsg = 'Iceberg'
ToonHealJokes = [['What goes TICK-TICK-TICK-WOOF?', 'A watchdog! '],
 ['Why do male deer need braces?', "Because they have 'buck teeth'!"],
 ['Why is it hard for a ghost to tell a lie?', 'Because you can see right through him.'],
 ['What did the ballerina do when she hurt her foot?', 'She called the toe truck!'],
 ['What has one horn and gives milk?', 'A milk truck!'],
 ["Why don't witches ride their brooms when they're angry?", "They don't want to fly off the handle!"],
 ['Why did the dolphin cross the ocean?', 'To get to the other tide.'],
 ['What kind of mistakes do spooks make?', 'Boo boos.'],
 ['Why did the chicken cross the playground?', 'To get to the other slide!'],
 ['Where does a peacock go when he loses his tail?', 'A retail store.'],
 ["Why didn't the skeleton cross the road?", "He didn't have the guts."],
 ["Why wouldn't they let the butterfly into the dance?", 'Because it was a moth ball.'],
 ["What's gray and squirts jam at you?", 'A mouse eating a doughnut.'],
 ['What happened when 500 hares got loose on the main street?', 'The police had to comb the area.'],
 ["What's the difference between a fish and a piano?", "You can tune a piano, but you can't tuna fish!"],
 ['What do people do in clock factories?', 'They make faces all day.'],
 ['What do you call a blind dinosaur?', "An I-don't-think-he-saurus."],
 ['If you drop a white hat into the Red Sea, what does it become?', 'Wet.'],
 ['Why was Cinderella thrown off the basketball team?', 'She ran away from the ball.'],
 ['Why was Cinderella such a bad player?', 'She had a pumpkin for a coach.'],
 ["What two things can't you have for breakfast?", 'Lunch and dinner.'],
 ['What do you give an elephant with big feet?', 'Big shoes.'],
 ['Where do baby ghosts go during the day?', 'Day-scare centers.'],
 ['What did Snow White say to the photographer?', 'Some day my prints will come.'],
 ["What's Tarzan's favorite song?", 'Jungle bells.'],
 ["What's green and loud?", 'A froghorn.'],
 ["What's worse than raining cats and dogs?", 'Hailing taxis.'],
 ['When is the vet busiest?', "When it's raining cats and dogs."],
 ['What do you call a gorilla wearing ear-muffs?', "Anything you want, he can't hear you."],
 ['Where would you weigh a whale?', 'At a whale-weigh station.'],
 ['What travels around the world but stays in the corner?', 'A stamp.'],
 ['What do you give a pig with a sore throat?', 'Oinkment.'],
 ['What did the hat say to the scarf?', 'You hang around while I go on a head.'],
 ["What's the best parting gift?", 'A comb.'],
 ['What kind of cats like to go bowling?', 'Alley cats.'],
 ["What's wrong if you keep seeing talking animals?", "You're having Disney spells."],
 ['What did one eye say to the other?', 'Between you and me, something smells.'],
 ["What's round, white and giggles?", 'A tickled onion.'],
 ['What do you get when you cross Bambi with a ghost?', 'Bamboo.'],
 ['Why do golfers take an extra pair of socks?', 'In case they get a hole in one.'],
 ['What do you call a fly with no wings?', 'A walk.'],
 ['Who did Frankenstein take to the prom?', 'His ghoul friend.'],
 ['What lies on its back, one hundred feet in the air?', 'A sleeping centipede.'],
 ['How do you keep a bull from charging?', 'Take away his credit card.'],
 ['What do you call a chicken at the North Pole?', 'Lost.'],
 ['What do you get if you cross a cat with a dog?', 'An animal that chases itself.'],
 ['What did the digital watch say to the grandfather clock?', 'Look dad, no hands.'],
 ['Where does Ariel the mermaid go to see movies?', 'The dive-in.'],
 ['What do you call a mosquito with a tin suit?', 'A bite in shining armor.'],
 ['What do giraffes have that no other animal has?', 'Baby giraffes.'],
 ['Why did the man hit the clock?', 'Because the clock struck first.'],
 ['Why did the apple go out with a fig?', "Because it couldn't find a date."],
 ['What do you get when you cross a parrot with a monster?', 'A creature that gets a cracker whenever it asks for one.'],
 ["Why didn't the monster make the football team?", 'Because he threw like a ghoul!'],
 ['What do you get if you cross a Cocker Spaniel with a Poodle and a rooster?', 'A cockapoodledoo!'],
 ['What goes dot-dot-dash-dash-squeak?', 'Mouse code.'],
 ["Why aren't elephants allowed on beaches?", "They can't keep their trunks up."],
 ['What is at the end of everything?', 'The letter G.'],
 ['How do trains hear?', 'Through the engineers.'],
 ['What does the winner of a marathon lose?', 'His breath.'],
 ['Why did the pelican refuse to pay for his meal?', 'His bill was too big.'],
 ['What has six eyes but cannot see?', 'Three blind mice.'],
 ["What works only when it's fired?", 'A rocket.'],
 ["Why wasn't there any food left after the monster party?", 'Because everyone was a goblin!'],
 ['What bird can be heard at mealtimes?', 'A swallow.'],
 ['What goes Oh, Oh, Oh?', 'Santa walking backwards.'],
 ['What has green hair and runs through the forest?', 'Moldy locks.'],
 ['Where do ghosts pick up their mail?', 'At the ghost office.'],
 ['Why do dinosaurs have long necks?', 'Because their feet smell.'],
 ['What do mermaids have on toast?', 'Mermarlade.'],
 ['Why do elephants never forget?', 'Because nobody ever tells them anything.'],
 ["What's in the middle of a jellyfish?", 'A jellybutton.'],
 ['What do you call a very popular perfume?', 'A best-smeller.'],
 ["Why can't you play jokes on snakes?", 'Because you can never pull their legs.'],
 ['Why did the baker stop making donuts?', 'He got sick of the hole business.'],
 ['Why do mummies make excellent spies?', "They're good at keeping things under wraps."],
 ['How do you stop an elephant from going through the eye of a needle?', 'Tie a knot in its tail.'],
 ["What goes 'Ha Ha Ha Thud'?", 'Someone laughing his head off.'],
 ["My friend thinks he's a rubber band.", 'I told him to snap out of it.'],
 ["My sister thinks she's a pair of curtains.", 'I told her to pull herself together!'],
 ['Did you hear about the dentist that married the manicurist?', 'Within a month they were fighting tooth and nail.'],
 ['Why do hummingbirds hum?', "Because they don't know the words."],
 ['Why did the baby turkey bolt down his food?', 'Because he was a little gobbler.'],
 ['Where did the whale go when it was bankrupt?', 'To the loan shark.'],
 ['How does a sick sheep feel?', 'Baah-aahd.'],
 ["What's gray, weighs 10 pounds and squeaks?", 'A mouse that needs to go on a diet.'],
 ['Why did the dog chase his tail?', 'To make ends meet.'],
 ['Why do elephants wear running shoes?', 'For jogging of course.'],
 ['Why are elephants big and gray?', "Because if they were small and yellow they'd be canaries."],
 ['If athletes get tennis elbow what do astronauts get?', 'Missile toe.'],
 ['Did you hear about the man who hated Santa?', 'He suffered from Claustrophobia.'],
 ['Why did ' + Donald + ' sprinkle sugar on his pillow?', 'Because he wanted to have sweet dreams.'],
 ['Why did ' + Goofy + ' take his comb to the dentist?', 'Because it had lost all its teeth.'],
 ['Why did ' + Goofy + ' wear his shirt in the bath?', 'Because the label said wash and wear.'],
 ['Why did the dirty chicken cross the road?', 'For some fowl purpose.'],
 ["Why didn't the skeleton go to the party?", 'He had no body to go with.'],
 ['Why did the burglar take a shower?', 'To make a clean getaway.'],
 ['Why does a sheep have a woolly coat?', "Because he'd look silly in a plastic one."],
 ['Why do potatoes argue all the time?', "They can't see eye to eye."],
 ['Why did ' + Pluto + ' sleep with a banana peel?', 'So he could slip out of bed in the morning.'],
 ['Why did the mouse wear brown sneakers?', 'His white ones were in the wash.'],
 ['Why are false teeth like stars?', 'They come out at night.'],
 ['Why are Saturday and Sunday so strong?', 'Because the others are weekdays.'],
 ['Why did the archaeologist go bankrupt?', 'Because his career was in ruins.'],
 ['What do you get if you cross the Atlantic on the Titanic?', 'Very wet.'],
 ['What do you get if you cross a chicken with cement?', 'A brick-layer.'],
 ['What do you get if you cross a dog with a phone?', 'A golden receiver.'],
 ['What do you get if you cross an elephant with a shark?', 'Swimming trunks with sharp teeth.'],
 ['What did the tablecloth say to the table?', "Don't move, I've got you covered."],
 ['Did you hear about the time ' + Goofy + ' ate a candle?', 'He wanted a light snack.'],
 ['What did the balloon say to the pin?', 'Hi Buster.'],
 ['What did the big chimney say to the little chimney?', "You're too young to smoke."],
 ['What did the carpet say to the floor?', 'I got you covered.'],
 ['What did the necklace say to the hat?', "You go ahead, I'll hang around."],
 ['What goes zzub-zzub?', 'A bee flying backwards.'],
 ['How do you communicate with a fish?', 'Drop him a line.'],
 ["What do you call a dinosaur that's never late?", 'A prontosaurus.'],
 ['What do you get if you cross a bear and a skunk?', 'Winnie-the-phew.'],
 ['How do you clean a tuba?', 'With a tuba toothpaste.'],
 ['What do frogs like to sit on?', 'Toadstools.'],
 ['Why was the math book unhappy?', 'It had too many problems.'],
 ['Why was the school clock punished?', 'It tocked too much.'],
 ["What's a polygon?", 'A dead parrot.'],
 ['What needs a bath and keeps crossing the street?', 'A dirty double crosser.'],
 ['What do you get if you cross a camera with a crocodile?', 'A snap shot.'],
 ['What do you get if you cross an elephant with a canary?', 'A very messy cage.'],
 ['What do you get if you cross a jeweler with a plumber?', 'A ring around the bathtub.'],
 ['What do you get if you cross an elephant with a crow?', 'Lots of broken telephone poles.'],
 ['What do you get if you cross a plum with a tiger?', 'A purple people eater.'],
 ["What's the best way to save water?", 'Dilute it.'],
 ["What's a lazy shoe called?", 'A loafer.'],
 ["What's green, noisy and dangerous?", 'A thundering herd of cucumbers.'],
 ['What color is a shout?', 'Yellow!'],
 ['What do you call a sick duck?', 'A mallardy.'],
 ["What's worse then a giraffe with a sore throat?", "A centipede with athlete's foot."],
 ['What goes ABC...slurp...DEF...slurp?', 'Someone eating alphabet soup.'],
 ["What's green and jumps up and down?", 'Lettuce at a dance.'],
 ["What's a cow after she gives birth?", 'De-calf-inated.'],
 ['What do you get if you cross a cow and a camel?', 'Lumpy milk shakes.'],
 ["What's white with black and red spots?", 'A Dalmatian with measles.'],
 ["What's brown has four legs and a trunk?", 'A mouse coming back from vacation.'],
 ["What does a skunk do when it's angry?", 'It raises a stink.'],
 ["What's gray, weighs 200 pounds and says, Here Kitty, kitty?", 'A 200 pound mouse.'],
 ["What's the best way to catch a squirrel?", 'Climb a tree and act like a nut.'],
 ["What's the best way to catch a rabbit?", 'Hide in a bush and make a noise like lettuce.'],
 ['What do you call a spider that just got married?', 'A newly web.'],
 ['What do you call a duck that robs banks?', 'A safe quacker.'],
 ["What's furry, meows and chases mice underwater?", 'A catfish.'],
 ["What's a funny egg called?", 'A practical yolker.'],
 ["What's green on the outside and yellow inside?", 'A banana disguised as a cucumber.'],
 ['What did the elephant say to the lemon?', "Let's play squash."],
 ['What weighs 4 tons, has a trunk and is bright red?', 'An embarrassed elephant.'],
 ["What's gray, weighs 4 tons, and wears glass slippers?", 'Cinderelephant.'],
 ["What's an elephant in a fridge called?", 'A very tight squeeze.'],
 ['What did the elephant say to her naughty child?', 'Tusk!  Tusk!'],
 ['What did the peanut say to the elephant?', "Nothing -- Peanuts can't talk."],
 ['What do elephants say when they bump into each other?', "Small world, isn't it?"],
 ['What did the cashier say to the register?', "I'm counting on you."],
 ['What did the flea say to the other flea?', 'Shall we walk or take the cat?'],
 ['What did the big hand say to the little hand?', 'Got a minute.'],
 ['What does the sea say to the sand?', 'Not much.  It usually waves.'],
 ['What did the stocking say to the shoe?', 'See you later, I gotta run.'],
 ['What did one tonsil say to the other tonsil?', 'It must be spring, here comes a swallow.'],
 ['What did the soil say to the rain?', 'Stop, or my name is mud.'],
 ['What did the puddle say to the rain?', 'Drop in sometime.'],
 ['What did the bee say to the rose?', 'Hi, bud.'],
 ['What did the appendix say to the kidney?', "The doctor's taking me out tonight."],
 ['What did the window say to the venetian blinds?', "If it wasn't for you it'd be curtains for me."],
 ['What did the doctor say to the sick orange?', 'Are you peeling well?'],
 ['What do you get if you cross a chicken with a banjo?', 'A self-plucking chicken.'],
 ['What do you get if you cross a hyena with a bouillon cube?', 'An animal that makes a laughing stock of itself.'],
 ['What do you get if you cross a rabbit with a spider?', 'A hare net.'],
 ['What do you get if you cross a germ with a comedian?', 'Sick jokes.'],
 ['What do you get if you cross a hyena with a mynah bird?', 'An animal that laughs at its own jokes.'],
 ['What do you get if you cross a railway engine with a stick of gum?', 'A chew-chew train.'],
 ['What would you get if you crossed an elephant with a computer?', 'A big know-it-all.'],
 ['What would you get if you crossed an elephant with a skunk?', 'A big stinker.'],
 ['Why did ' + MickeyMouse + ' take a trip to outer space?', 'He wanted to find ' + Pluto + '.']]
MovieHealLaughterMisses = ('hmm',
 'heh',
 'ha',
 'Cave')
MovieHealLaughterHits1 = ('Mine',
 'Mine Shack',
 'Forest',
 'Cove')
MovieHealLaughterHits2 = ('Hidden Lake', 'Gold Mine', 'Box Dimension')
MovieSOSCallHelp = '%s HELP!'
MovieSOSWhisperHelp = '%s needs help in battle!'
MovieSOSObserverHelp = 'HELP!'
MovieNPCSOSGreeting = 'Hi %s! Glad to help!'
MovieNPCSOSGoodbye = 'Underwater Room'
MovieNPCSOSToonsHit = 'Recycling Plant'
MovieNPCSOSCogsMiss = 'Treasure Room'
MovieNPCSOSRestockGags = 'Restocking %s gags!'
MovieNPCSOSHeal = 'Heal'
MovieNPCSOSTrap = 'Trap'
MovieNPCSOSLure = 'Lure'
MovieNPCSOSSound = 'Sound'
MovieNPCSOSThrow = 'Throw'
MovieNPCSOSSquirt = 'Squirt'
MovieNPCSOSDrop = 'Drop'
MovieNPCSOSAll = 'All'
MoviePetSOSTrickFail = 'Sigh'
MoviePetSOSTrickSucceedBoy = '???'
MoviePetSOSTrickSucceedGirl = 'Penguin is online'
MovieSuitCancelled = 'Would you like to addme as your Friend?'
RewardPanelToonTasks = 'ToonTasks'
RewardPanelItems = 'Request Sent'
RewardPanelMissedItems = 'Are you sure you want to remove this friend?'
RewardPanelQuestLabel = 'Quest %s'
RewardPanelCongratsStrings = ['Yeah!',
 'Penguin has asked to be your buddy. Do you accept?',
 'Wow!',
 'Cool!',
 'Awesome!',
 'Toon-tastic!']
RewardPanelNewGag = 'New %(gagName)s gag for %(avName)s!'
RewardPanelUberGag = '%(avName)s earned the %(gagName)s gag with %(exp)s experience points!'
RewardPanelEndTrack = 'Yay! %(avName)s has reached the end of the %(gagName)s Gag Track!'
RewardPanelMeritsMaxed = 'Maxed'
RewardPanelMeritBarLabels = ['Stock Options',
 'Penguin is now your buddy!',
 'Cogbucks',
 'Merits']
RewardPanelMeritAlert = 'Loading Create Penguin'
RewardPanelCogPart = 'Loading Engine'
RewardPanelPromotion = 'Ready for promotion in %s  track!'
RewardPanelSkip = 'Skip'
CheesyEffectDescriptions = [('Loading Gridview', 'Loading Interface'),
 ('Loading Clothing', 'Loading Mail'),
 ('Loading Local Language', 'Loading Your Inventory'),
 ('Would you like to open your igloo?', 'Loading the Igloo'),
 ('Energy', 'This will add your igloo to the map.'),
 ('Rest', 'Health'),
 ('Feed your Pet', 'Play with Pet'),
 ('Walk your Pet', 'Sleep'),
 ('Stop Edit', 'Loading Your Furniture'),
 ('Transparent', 'Edit Igloo'),
 ('Loading Furniture', 'Loading Controls'),
 ('Close Igloo', 'Loading Floor')]
CheesyEffectIndefinite = 'Until you choose another effect, %(effectName)s%(whileIn)s.'
CheesyEffectMinutes = 'For the next %(time)s minutes, %(effectName)s%(whileIn)s.'
CheesyEffectHours = 'For the next %(time)s hours, %(effectName)s%(whileIn)s.'
CheesyEffectDays = 'For the next %(time)s days, %(effectName)s%(whileIn)s.'
CheesyEffectWhileYouAreIn = ' while you are in %s'
CheesyEffectExceptIn = ', except in %s'
SuitFlunky = 'Flunky'
SuitPencilPusher = 'Open Igloo'
SuitYesman = 'Yesman'
SuitMicromanager = 'View Items'
SuitDownsizer = 'Downsizer'
SuitHeadHunter = 'Buy Items'
SuitCorporateRaider = 'Upgrade Igloo'
SuitTheBigCheese = 'Play Music'
SuitColdCaller = 'Save Igloo'
SuitTelemarketer = 'All'
SuitNameDropper = 'Enter Contest'
SuitGladHander = 'View Stored Igloo'
SuitMoverShaker = 'Your Friends'
SuitTwoFace = 'Two-Face'
SuitTheMingler = 'Users in Room'
SuitMrHollywood = 'Ignore List'
SuitShortChange = 'Old news'
SuitPennyPincher = 'Aqua Grabber'
SuitTightwad = 'Tightwad'
SuitBeanCounter = 'Astro Barrier'
SuitNumberCruncher = 'Play Beans'
SuitMoneyBags = 'Cart Surfer'
SuitLoanShark = 'Go Fishing'
SuitRobberBaron = 'Play Jet Pack'
SuitBottomFeeder = 'Thin Ice'
SuitBloodsucker = 'Blood\x03sucker'
SuitDoubleTalker = 'Go Surfing'
SuitAmbulanceChaser = 'Hydro Hopper'
SuitBackStabber = 'Play Pizzatron'
SuitSpinDoctor = 'Puffle Roundup'
SuitLegalEagle = 'Play Mancala'
SuitBigWig = 'Play Find Four'
SuitFlunkyS = 'Join Sled Race'
SuitPencilPusherS = 'Mix Music'
SuitYesmanS = 'Treasure Hunt'
SuitMicromanagerS = 'Balloon Pop'
SuitDownsizerS = 'Ring The Bell'
SuitHeadHunterS = 'Feed-A-Puffle'
SuitCorporateRaiderS = 'Memory Game'
SuitTheBigCheeseS = 'Puffle Paddle'
SuitColdCallerS = 'Puffle Shuffle'
SuitTelemarketerS = 'Puffle Soaker'
SuitNameDropperS = 'Spin To Win'
SuitGladHanderS = 'Practice Card-Jitsu'
SuitMoverShakerS = 'Practice Card-Jitsu Fire'
SuitTwoFaceS = 'Practice Card-Jitsu Water'
SuitTheMinglerS = 'Dance Contest'
SuitMrHollywoodS = 'Puffle Rescue'
SuitShortChangeS = 'System Defender'
SuitPennyPincherS = 'Bits and Bolts'
SuitTightwadS = 'Find Player'
SuitBeanCounterS = 'Send Mail'
SuitNumberCruncherS = 'Free Gift'
SuitMoneyBagsS = 'Report Player'
SuitLoanSharkS = 'Ignore Player'
SuitRobberBaronS = 'Remove Ignore'
SuitBottomFeederS = 'Add Friend'
SuitBloodsuckerS = 'Remove Friend'
SuitDoubleTalkerS = 'Visit Igloo'
SuitAmbulanceChaserS = 'Ban Player'
SuitBackStabberS = 'Mute Player'
SuitSpinDoctorS = 'Kick Player'
SuitLegalEagleS = 'Clear Penguin'
SuitBigWigS = 'Town'
SuitFlunkyP = 'Flunkies'
SuitPencilPusherP = 'Coffee Shop'
SuitYesmanP = 'Yesmen'
SuitMicromanagerP = 'Micromanagers'
SuitDownsizerP = 'Downsizers'
SuitHeadHunterP = 'Book Room'
SuitCorporateRaiderP = 'Dance Club'
SuitTheBigCheeseP = 'Lounge'
SuitColdCallerP = 'Clothes Shop'
SuitTelemarketerP = 'Telemarketers'
SuitNameDropperP = 'Ski Village'
SuitGladHanderP = 'Sport Shop'
SuitMoverShakerP = 'Ski Lodge'
SuitTwoFaceP = 'Two-Faces'
SuitTheMinglerP = 'Lodge Attic'
SuitMrHollywoodP = 'Ski Hill'
SuitShortChangeP = 'The Plaza'
SuitPennyPincherP = 'Pet Shop'
SuitTightwadP = 'Tightwads'
SuitBeanCounterP = 'Dojo'
SuitNumberCruncherP = 'Dojo Courtyard'
SuitMoneyBagsP = 'Pizza Parlor'
SuitLoanSharkP = 'Stage'
SuitRobberBaronP = 'The Beach'
SuitBottomFeederP = 'Lighthouse'
SuitBloodsuckerP = 'Bloodsuckers'
SuitDoubleTalkerP = 'Beacon'
SuitAmbulanceChaserP = 'Pirate Ship'
SuitBackStabberP = 'Hold'
SuitSpinDoctorP = 'Captain\'s Quarters'
SuitLegalEagleP = 'Crow\'s Nest'
SuitBigWigP = 'The Dock'
SuitFaceoffDefaultTaunts = ['Boo!']
SuitAttackDefaultTaunts = ['Take that!', 'Take a memo on this!']
SuitAttackNames = {'Audit': 'Audit!',
 'Bite': 'Bite!',
 'BounceCheck': 'Snow Forts',
 'BrainStorm': 'Stadium',
 'BuzzWord': 'EPF Command Room',
 'Calculate': 'Calculate!',
 'Canned': 'Canned!',
 'Chomp': 'Chomp!',
 'CigarSmoke': 'Facility',
 'ClipOnTie': 'Everyday Phoning Facility',
 'Crunch': 'Crunch!',
 'Demotion': 'Demotion!',
 'Downsize': 'Downsize!',
 'DoubleTalk': 'VR Room',
 'EvictionNotice': 'Boiler Room',
 'EvilEye': 'Iceberg',
 'Filibuster': 'Filibuster!',
 'FillWithLead': 'Cave',
 'Mine Shack': "Mine",
 'FingerWag': 'Forest',
 'Fired': 'Fired!',
 'FloodTheMarket': 'Cove',
 'FountainPen': 'Box Dimension',
 'FreezeAssets': 'Cave Mine',
 'Gavel': 'Gavel!',
 'GlowerPower': 'Hidden Lake',
 'GuiltTrip': 'Underwater Room',
 'HalfWindsor': 'Recycling Plant',
 'HangUp': '???',
 'HeadShrink': 'Member Igloos',
 'HotAir': 'All Items',
 'Jargon': 'Jargon!',
 'Legalese': 'Legalese!',
 'Liquidate': 'Liquidate!',
 'MarketCrash': 'Head Items',
 'MumboJumbo': 'Face Items',
 'ParadigmShift': 'Neck Items',
 'PeckingOrder': 'Body Items',
 'PickPocket': 'Hand Items',
 'PinkSlip': 'Feet Items',
 'PlayHardball': 'Pins/Flags',
 'PoundKey': 'Other Items',
 'PowerTie': 'Backgrounds',
 'PowerTrip': 'Awards',
 'Quake': 'Quake!',
 'RazzleDazzle': 'Colors',
 'RedTape': 'Teleport',
 'ReOrg': 'Re-Org!',
 'Emotes': 'Visit HQ',
 'Rolodex': 'Rolodex!',
 'RubberStamp': 'Actions',
 'RubOut': 'Snowball',
 'Sacked': 'Sacked!',
 'SandTrap': 'Friends',
 'Schmooze': 'Schmooze!',
 'Shake': 'Shake!',
 'Shred': 'Shred!',
 'SongAndDance': 'Show Online',
 'Spin': 'Spin!',
 'Synergy': 'Synergy!',
 'Tabulate': 'Tabulate!',
 'TeeOff': 'Show Ignored',
 'ThrowBook': 'Edit Player',
 'Tremor': 'Tremor!',
 'Watercooler': 'Watercooler!',
 'Withdrawal': 'Withdrawal!',
 'WriteOff': 'Your Igloo'}
SuitAttackTaunts = {'Audit': ["I believe your books don't balance.",
           "Edit Account",
           'Send',
           'Chat',
           "Incorrect Password",
           'Too many failed login attempts. Please try again later.',
           "Joining",
           'Logging in',
           'Joining Player\'s Igloo',
           "PLEASE SELECT A SERVER"],
 'Bite': ['Would you like a bite?',
          'Penguin Name:',
          "Password:",
          'Remember me on this computer',
          'Remember my password',
          'Forgot your password?',
          "Forget my penguin",
          "Login as a different penguin",
          "Your Suggested Servers",
          'Buddies online'],
 'BounceCheck': ["Ah, too bad, you're funless.",
                 'Amount of penguins online',
                 'Ultimate safe chat',
                 'Parents',
                 "Click Here",
                 "Don't have a penguin?",
                 "Create a free account now",
                 'Start',
                 'Back',
                 "This will permanently remove all postcards. Do you want to do this?",
                 "Are you sure you want to recycle this postcard?",
                 'Are you sure you want to ?',
                 "This will remove all messages. This is not undoable."],
 'BrainStorm': ['I forecast rain.',
                'You havember postcards!',
                'You have 1 postcard!',
                'You have no postcards!',
                'From:',
                'New!',
                "message",
                'Send this postcard toforcoins?',
                'Buy and send'],
 'BuzzWord': ['Pardon me if I drone on.',
              'postcards for',
              'Send to:',
              'Failed to send Postcard.',
              'You need more coins.',
              'This penguin\'s mailbox is full. Your postcard could not be sent. Please try again later.',
              'Postcard sent',
              'Postcards',
              "Preview Postcard",
              'Select a Postcard'],
 'Calculate': ['These numbers do add up!',
               'Send To',
               "Inbox",
               'You have no postcards',
               'Would you like to play',
               "Aqua Grabber?",
               "Would you like to play",
               'Astro Barrier?',
               'Would you like to play',
               Cogs + 'Bean Counters?'],
 'Canned': ['Do you like it out of the can?',
            'Would you like to go on a',
            "Jet Pack Adventure?",
            'Would you like to go',
            "Ice Fishing?",
            'Would you like to play',
            'Hydro Hopper?',
            "Would you like to play",
            "Puffle Roundup?",
            "Would you like to join this"],
 'Chomp': ['Take a look at these chompers!',
           'Mancala game?',
           "Would you like to join this",
           'Find Four game?',
           "Would you like to go",
           "Cart Surfing?",
           'Would you like to play'],
 'ClipOnTie': ['Better dress for our meeting.',
               "Thin Ice?",
               'Pizzatron 3000?' + Cogs + 'Would you like to play',
               'Would you like to',
               'catch some waves?',
               'Would you like to join this',
               'Sled race?',
               'Would you like to read',
               "My Puffle?",
               'Would you like to read',
               "Burnt Out Bulbs?",
               "Would you like to read"],
 'Crunch': ["Looks like you're in a crunch.",
            "Lime Green Dojo Clean?",
            "Would you like to",
            'dig for treasure?',
            'Would you like to play',
            'Balloon Pop?',
            "Would you like to play",
            "Ring The Bell?",
            "Would you like to play"],
 'Demotion': ["You're moving down the corporate ladder.",
              "Feed-A-Puffle?",
              'Would you like to play',
              "Memory Card Game?",
              "Would you like to play",
              "Puffle Paddle?",
              "Would you like to play",
              "Puffle Shuffle?",
              "Would you like to play",
              'Puffle Soaker?'],
 'Downsize': ['Come on down!',
              'Would you like to play Daily Spin?',
              "Would you like to practice",
              "Card-Jitsu?",
              'Would you like to practice',
              "Card-Jitsu Fire?",
              'Would you like to practice',
              "Card-Jitsu Water?",
              'Would you like to talk',
              'to the Sensei?',
              'Would you like to talk',
              'to the Sensei?'],
 'EvictionNotice': ["It's moving time.",
                    'Would you like to talk',
                    'to the Sensei?',
                    'You need a deck of Cards to play.',
                    "Please see the Sensei first.",
                    'You need a Fire Booster Deck to play.',
                    "Please see the Sensei first.",
                    "You need a Water Booster Deck to play.",
                    "Please see the Sensei first.",
                    'Would you like to dance?',
                    "Would you like to play Puffle Rescue?"],
 'EvilEye': ["I'm giving you the evil eye.",
             'Would you like to play System Defender?',
             "Would you like to play Bits and Bolts?",
             "You have earned 0 coins.",
             'You now coins.',
             "You have earned 1 coin.",
             "You now coins.",
             'You have  coins.',
             "You now coins.",
             "Are you sure you want to quit this game?"],
 'Filibuster': ["Shall I fill 'er up?",
                'Penguin has quit the game.',
                'Loading Tutorial Prompt',
                "Your Coins:tal",
                'coins',
                'Would you like to adopt this puffle for 400 coins?',
                'Your puffle needs a name.',
                'Your new puffle is now in your igloo. Enjoy!',
                "You already own the maximum number of puffles!",
                'Would you like to buyme forst coins?'],
 'FingerWag': ['I have told you a thousand times.',
               'Would you like to buyme forst coins?',
               "Would you like to buyme forst coins?",
               "Would you like to buyme forst coins?",
               "Would you like to buy some Pet Food for 10 coins?",
               "Would you like to bathe your puffle for 5 coins?",
               'Would you like to buy some Gum for 5 coins?' + Cogs + '.',
               "Would you like to buy a Cookie for 5 coins?",
               'Penguin',
               "has been added to your inventory.",
               'Penguin has been added to your inventory.',
               "You currently havem coins."],
 'Fired': ['I hope you brought some marshmallows.',
           "You have found ame.",
           'Would you like to pick it up?',
           "Would you like to get your Medal of Excellence?",
           'Would you like to get your gift?',
           'You have found ame.',
           "Would you like to pick it up?",
           'You have found ame.',
           'Would you like to upgrade your igloo?',
           'You already have this item.',
           'Sorry, you must wear the tour guide',
           "hat to use this feature",
           "Are you sure you want to change your igloo? Your flooring will be lost. Igloo items will be saved in your inventory.",
           "You need more coins.",
           'You already have this item.',
           "You already have this flooring.",
           'White',
           "Yellow"],
 'FountainPen': ['This is going to leave a stain.',
                 "Orange",
                 'Green',
                 "Blue",
                 'Red',
                 'Purple',
                 "Brown",
                 'Black',
                 'Blue',
                 "Pink",
                 "Black"],
 'FreezeAssets': ['Your assets are mine.',
                  'Green',
                  "Purple",
                  'Red',
                  "Yellow",
                  'White',
                  'Orange',
                  'Brown',
                  "Login to Unlock Your Items",
                  'What word is on pagefrom the left on line',
                  'word',
                  "words"],
 'GlowerPower': ['You looking at me?',
                 "items remaining",
                 'item remaining',
                 "You have unlockedmber item(s)!",
                 "You still have items to unlock. Your code is only valid once, if you quit before you finish unlocking all your items your remaining choices will be lost.",
                 "Are you sure you want to quit?",
                 'Are you sure you want to redeem',
                 'emName?',
                 'Hello',
                 'Congratulations! You\'re done! Click Yes to see what has been added to your inventory.',
                 'You\'ll need to entermber more Treasure Book code(s) to unlock this page.'],
 'GuiltTrip': ["I'll lay a real guilt trip on you!",
               'Puffle',
               "Blue",
               'Pink',
               'Black',
               "Green",
               "Purple",
               "Red",
               'Yellow',
               'White',
               'Orange'],
 'HalfWindsor': ["This is the fanciest tie you'll ever see!",
                 'Brown',
                 "You now have theem!",
                 "You'll need to entermber more code(s) to unlock this page.",
                 "You can choosember more Super Exclusive item(s).",
                 "Yes",
                 'No',
                 "Ok",
                 "Start"],
 'HangUp': ["You've been disconnected.",
            'Okay',
            "Close",
            "Learn More",
            'Click!',
            'Login',
            "Sign In",
            'Visit Community Section',
            "a-z A-Z !?",
            'Loading Localized Files',
            'Loading Global Files',
            'Loading Content'],
 'HeadShrink': ["Looks like you're seeing a shrink.",
                'Loading Communication',
                "Loading Login",
                'Loading Music',
                'Rockhopper',
                "Aunt Arctic",
                'Cadence',
                'Gary',
                'Franky',
                'Petey K'],
 'HotAir': ["We're having a heated discussion.",
            "G Billy",
            "Stompin Bob",
            'Sensei',
            'Page',
            "New",
            "Empty",
            'Club Penguin',
            "am",
            'pm',
            'hour',
            'hours'],
 'Jargon': ['What nonsense.',
            'of',
            'Loading',
            "Loading Ninja Progress",
            'Cards Collected:Power Cards:ofCurrent Belt',
            "Next Belt",
            'Current Item',
            'Next Item',
            'Sunday',
            'Monday'],
 'Legalese': ['You must cease and desist.',
              'Tuesday',
              'Wednesday',
              "Thursday",
              'Friday',
              "Saturday",
              "Loading Binoculars",
              'Loading Telescope',
              'Click where you want to go.',
              'Loading Map',
              "Loading Igloo Map",
              "Loading Penguin"],
 'Liquidate': ['I like to keep things fluid.',
               'Loading Archives',
               "Loading Mancala",
               'Loading Find Four',
               "Loading Aqua Grabber",
               'Loading Astro Barrier',
               'Loading Beans',
               "Loading Cart Surfer",
               "Loading Gone Fishing",
               "Loading Jet Pack Adventure"],
 'MarketCrash': ["I'm going to crash your party.",
                 "Loading Thin Ice",
                 "Loading Catchin Waves",
                 "Loading Hydro Hopper",
                 "Loading Pizzatron 3000",
                 "Loading Puffle Round-up",
                 'Loading Sled Racing',
                 'Loading Paint by Letters',
                 'Loading Paint by Letters',
                 'Loading Paint by Letters',
                 "Loading Treasure Hunt"],
 'MumboJumbo': ['Let me make this perfectly clear.',
                "Loading Balloon Pop",
                "Loading Ring The Bell",
                'Loading Feed-A-Puffle',
                'Loading Memory Card Game',
                'Loading Puffle Paddle',
                'Loading Puffle Shuffle',
                'Loading Puffle Soaker',
                'Loading Spin To Win',
                'Loading Card-Jitsu'],
 'ParadigmShift': ["Watch out! I'm rather shifty.",
                   'Loading Card-Jitsu Fire',
                   "Loading Card-Jitsu Water",
                   "Loading the Sensei",
                   "Loading the Sensei",
                   'Loading the Sensei',
                   "Clearing the dance floor...",
                   "Loading Puffle Rescue",
                   'Loading System Defender'],
 'PeckingOrder': ["This one's for the birds.",
                  'Loading Bits and Bolts',
                  "Mancala",
                  'Find Four',
                  "Sled Racing",
                  'Treasure Hunt',
                  'Card-Jitsu',
                  "Card-Jitsu Fire",
                  'Card-Jitsu Water'],
 'PickPocket': ['Let me check your valuables.',
                "Dance Contest",
                'Settings',
                'You\'re onrvername',
                "Your penguin isold",
                'Mute Music',
                'Manage Account',
                "Friends",
                'Igloo Contest',
                "Igloo Contest",
                "Igloo Background",
                'Igloo Storage',
                "Loading Mission",
                "Loading Mission"],
 'PinkSlip': ['Try not to slip up.',
              "Loading Mission",
              'Loading Mission',
              'Loading Mission',
              "Loading Mission",
              "Loading Mission",
              "Loading Mission",
              "Loading Mission",
              "Loading Mission",
              "Loading Mission"],
 'PlayHardball': ['So you wanna play hardball?',
                  "Loading Town",
                  'Loading Coffee Shop',
                  'Loading Book Room',
                  "Loading Dance Club",
                  "Loading Dance Lounge",
                  "Loading Clothes Shop",
                  "Loading Ski Village",
                  'Loading Ski Lodge',
                  "Loading Lodge Attic",
                  "Loading Sport Shop",
                  "Loading Mountain"],
 'PoundKey': ['Time to return some calls.',
              "Loading the Plaza",
              "Loading the Pet Shop",
              "Loading the Dojo",
              'Loading the Dojo Courtyard',
              'Loading the Ninja Hideout',
              "Loading the Fire Dojo",
              'Loading Water Dojo',
              "Loading the Pizza Parlor",
              "O.K. Toon, it's the pound for you."],
 'PowerTie': ["I'll call later, you looked tied up.",
              'Loading the Stage',
              "Loading Beach",
              'Loading Lighthouse',
              "Loading Beacon",
              "Loading Pirate Ship",
              'Loading Ship Hold',
              'Loading Captain\'s Quarters',
              "Loading Crow's Nest",
              "Loading the Dock"],
 'PowerTrip': ["Pack your bags, we're taking a little trip.",
               'Loading Snow Forts',
               "Loading Stadium",
               'Loading HQ',
               'Loading EPF Command Room',
               'Loading the Facility',
               "Loading the Phoning Facility",
               'Loading the VR Room',
               "Loading Boiler Room",
               "Loading the Iceberg",
               'Loading Cave'],
 'Quake': ["Let's quake, rattle, and roll.",
           "Loading Mine",
           "Loading Mine Shack",
           "Loading Forest",
           "Loading the Cove",
           'Loading Box Dimension',
           "Loading Cave Mine",
           'Loading the Hidden Lake',
           "Loading Underwater Room"],
 'RazzleDazzle': ['Read my lips.',
                  'Loading Recycling Plant',
                  "Loading",
                  "Loading",
                  'Loading',
                  "Loading ???",
                  "Pins",
                  "Released:nthy/year.",
                  "All Stamps",
                  'Color',
                  'Highlight'],
 'RedTape': ['This should wrap things up.',
             "Pattern",
             "Icon",
             '0/1',
             'Total Stamps:',
             "Page",
             "0 ofYour Pins:",
             'Your New Stamps',
             'These are your recently earned stamps:',
             'Congratulations on earning'],
 'ReOrg': ["You don't like the way I reorganized things!",
           'stamp!',
           "Congratulations on earning",
           'stamps!',
           "Total Stamps1",
           'Penguin Stamps:',
           "Penguin:",
           'Contents',
           "Cover",
           "Stamp Book Guide"],
 'RestrainingOrder': ['You should show a little restraint.',
                      "Easy",
                      "Medium",
                      'Hard',
                      'Extreme',
                      Cogs + 'Member Stamp',
                      'New Stamp',
                      "Edit Stamp Book",
                      'Save Stamp Book',
                      "Released:nth/day/year.",
                      "Loading Stampbook"],
 'Rolodex': ["Your card's in here somewhere.",
             "Loading Stampbook",
             'You\'ve earned:',
             "num coins",
             "num x 2 =m_x2 coins",
             "1 coin",
             'Your total coins:m',
             'num oftal',
             "Congratulations, allme_name stamps earned. Double coin bonus!",
             'Congratulations, double coin bonus!',
             'Earn Stamps!'],
 'RubberStamp': ['I always make a good impression.',
                 "How to earn stamps",
                 'game_name Stamps',
                 'Stamp Earned!',
                 'Congratulations, allme_name stamps earned.',
                 "Stamp Book",
                 'Your Stamps:merator/denominator',
                 "Loading Award",
                 "Loading Award",
                 "Loading Award"],
 'RubOut': ['And now for my disappearing act.',
            "Loading Award",
            'Loading Award',
            'Loading Award',
            "Loading Forest Map",
            'Loading Award',
            'Loading Award',
            'Loading Award',
            "Loading Award",
            'Loading Thank You Card',
            "Loading Award",
            'Loading Award'],
 'Sacked': ["Looks like you're getting sacked.",
            "Loading Award",
            "Loading Award",
            'Loading Award',
            'Loading Award',
            'Loading Award',
            "Loading Award",
            "Loading Starter Deck",
            'Loading Award',
            'Loading Award'],
 'Schmooze': ["You'll never see this coming.",
              'Loading Wood EPF Badge',
              "Loading Ice EPF Badge",
              "Loading Bronze EPF Badge",
              'Loading Silver EPF Badge',
              "Loading Gold EPF Badge",
              'Loading EPF Certificate',
              "Loading Fire Booster Deck",
              'Loading Award',
              "Loading Award",
              'Loading Water Booster Deck'],
 'Shake': ["You're right on the epicenter.",
           "Loading Stowaway",
           "Loading Franky",
           'Loading Spice',
           "Loading Dare",
           "Loading Journal",
           'Loading Tales \'07',
           'Loading Tales \'08',
           'Loading Tales \'09',
           "Loading Yearbook 05/06",
           'Loading Yearbook 06/07',
           'Loading Yearbook 07/08'],
 'Shred': ['I need to get rid of some hazardous waste.',
           "Loading Yearbook 08/09",
           "Loading Yearbook 09/10",
           'Loading Rockhopper Island',
           "Loading Music Makes Magic",
           'Loading Fairy Fables',
           'Give a Tour',
           "Loading Clothing Catalog",
           "Loading Costume Catalog",
           'Loading Sport Catalog',
           "Loading Hair Catalog"],
 'Spin': ['What do you say we go for a little spin?',
          'Loading FISH Catalog',
          "Loading Puffle Catalog",
          "Loading Puffle Catalog",
          "Loading Pirate Catalog",
          'Loading Igloo Catalog',
          "Loading Furniture Catalog",
          "Loading Music Catalog",
          'Loading Merchandise Catalog'],
 'Synergy': ["I'm taking this to committee.",
             "Loading Merchandise Catalog",
             "Loading Prize Booth",
             "Loading Member Prize Booth",
             'Loading Ninja Catalog',
             'Loading Cove Catalog',
             'Loading Dock Catalog',
             "Loading Lodge Catalog",
             "Loading Ski Hill Catalog",
             'Loading Diving Catalog'],
 'Tabulate': ["This doesn't add up.",
              'Loading Dance Catalog',
              "Loading Catalog",
              "Loading Lighthouse Catalog",
              'Loading Member Prize Booth',
              'Loading Clock Tower Plaque',
              'Loading Backstage Note',
              'Loading Rockhopper\'s Note',
              'Loading Secret Lab Note',
              'Loading Ninja Belts Legend'],
 'TeeOff': ["You're not up to par.",
            'Fore!',
            "Loading Sensei's Note",
            "Loading Color Poster",
            'Loading Corkboard',
            'Swing!',
            'Take a Tour',
            "Haunted House Poster",
            'Loading Sensei\'s Note',
            'Loading Sensei\'s Note',
            'Loading Fire Clothing Poster',
            'Loading Water Clothing Poster'],
 'Tremor': ['Did you feel that?',
            'Loading Maze Map',
            'Loading Video',
            'Loading Video',
            "Loading Christmas Poster",
            'Loading Dig Poster',
            "Loading Dig Poster",
            'Loading Treasure',
            'Loading Treasure'],
 'Watercooler': ['This ought to cool you off.',
                 "Loading Treasure",
                 'Loading Treasure',
                 'Loading Note',
                 "Loading Video",
                 "Loading Video",
                 'Loading Video',
                 "Loading Video",
                 "Loading Video",
                 'Loading Video',
                 'Loading Poster',
                 "Loading Recycle Poster"],
 'Withdrawal': ["I believe you're overdrawn.",
                'Loading Recycle Note',
                'Loading Quest Poster',
                'Loading Ship Poster',
                "Loading Dragon Poster",
                "Loading Poster",
                "Loading Poster",
                'Poster',
                'Loading Note',
                "Loading Note"],
 'WriteOff': ['Let me increase your losses.',
              "Loading Note",
              'Loading Note',
              "Loading Note",
              "Loading Video",
              'Loading Moderator',
              'Loading Timer',
              "Loading Help",
              "Loading Coins For Change",
              'Loading Music Menu']}
BuildingWaitingForVictors = ('Loading Missions',)
ElevatorHopOff = 'Agent Form'
ElevatorStayOff = "Newspaper Form"
ElevatorLeaderOff = 'Tour Guide Form'
ElevatorHoppedOff = 'Report Form'
ElevatorMinLaff = 'You need %s laff points to ride this elevator.'
ElevatorHopOK = 'Okay'
ElevatorGroupMember = 'Submission Form'
KartMinLaff = 'You need %s laff points to ride this kart'
CogsIncExt = 'Loading Library'
CogsIncModifier = '%s' + CogsIncExt
CogsInc = Cogs.upper() + CogsIncExt
CogdominiumsExt = 'Loading Voting Booth'
Cogdominiums = Cog.upper() + CogdominiumsExt
DoorKnockKnock = 'Loading Art'
DoorWhosThere = "Loading Sculpture Plaque"
DoorWhoAppendix = ' who?'
DoorNametag = 'Door'
FADoorCodes_UNLOCKED = None
FADoorCodes_TALK_TO_TOM = 'Loading Sculpture Plaque'
FADoorCodes_DEFEAT_FLUNKY_HQ = 'Loading Sculpture Plaque'
FADoorCodes_TALK_TO_HQ = 'Loading Sculpture Plaque'
FADoorCodes_WRONG_DOOR_HQ = 'Loading Sculpture Plaque'
FADoorCodes_GO_TO_PLAYGROUND = 'Loading Sculpture Plaque'
FADoorCodes_DEFEAT_FLUNKY_TOM = 'Loading Sculpture Plaque'
FADoorCodes_TALK_TO_HQ_TOM = 'Loading Sculpture Plaque'
FADoorCodes_SUIT_APPROACHING = None
FADoorCodes_BUILDING_TAKEOVER = "Loading Sculpture Plaque"
FADoorCodes_SB_DISGUISE_INCOMPLETE = "Loading Sculpture Plaque"
FADoorCodes_CB_DISGUISE_INCOMPLETE = "Loading Sculpture Plaque"
FADoorCodes_LB_DISGUISE_INCOMPLETE = "Loading Sculpture Plaque"
FADoorCodes_BB_DISGUISE_INCOMPLETE = "Loading Sculpture Plaque"
KnockKnockContestJokes = {2100: ['Wally', "Wally's not looking, hit him with a pie!"],
 2200: {28: ['Biscuit', 'Biscuit out of here the Cogs are coming!'],
        41: ['Dewey', 'Dewey want to go defeat some more Cogs?'],
        40: ['Minnie', "Minnie people have asked that, and it's driving me crazy!"],
        27: ['Disguise', 'Disguise where the Cogs fly!']},
 2300: ['Justin', 'Justin other couple of Cog parts and off we go!'],
 3300: {10: ['Aladdin', 'Aladdin HQ wants a word with you.'],
        6: ['Weirdo', 'Weirdo all these Cogs come from?'],
        30: ['Bacon', 'Bacon a cake to throw at the Cogs.'],
        28: ['Isaiah', 'Isaiah we go ride the trolley.'],
        12: ['Juliet', "Juliet me in that Cog building with you and I'll give you a Toon-Up."]}}
KnockKnockJokes = [['Who', "Bad echo in here, isn't there?"],
 ['Dozen', 'Dozen anybody want to let me in?'],
 ['Freddie', 'Freddie or not, here I come.'],
 ['Dishes', 'Dishes your friend, let me in.'],
 ['Wooden shoe', 'Wooden shoe like to know.'],
 ['Betty', "Betty doesn't know who I am."],
 ['Kent', 'Kent you tell?'],
 ['Noah', "Noah don't know who either."],
 ["I don't know", 'Neither do I, I keep telling you that.'],
 ['Howard', 'Howard I know?'],
 ['Emma', 'Emma so glad you asked me that.'],
 ['Auto', "Auto know, but I've forgotten."],
 ['Jess', 'Jess me and my shadow.'],
 ['One', 'One-der why you keep asking that?'],
 ['Alma', 'Alma not going to tell you!'],
 ['Zoom', 'Zoom do you expect?'],
 ['Amy', "Amy fraid I've forgotten."],
 ['Arfur', 'Arfur got.'],
 ['Ewan', 'No, just me'],
 ['Cozy', "Cozy who's knocking will you?"],
 ['Sam', 'Sam person who knocked on the door last time.'],
 ['Fozzie', 'Fozzie hundredth time, my name is ' + Flippy + '.'],
 ['Deduct', Donald + ' Deduct.'],
 ['Max', 'Max no difference, just open the door.'],
 ['N.E.', 'N.E. body you like, let me in.'],
 ['Amos', 'Amos-quito bit me.'],
 ['Alma', "Alma candy's gone."],
 ['Bruce', "I Bruce very easily, don't hit me."],
 ['Colleen', "Colleen up your room, it's filthy."],
 ['Elsie', 'Elsie you later.'],
 ['Hugh', 'Hugh is going to let me in?'],
 ['Hugo', "Hugo first - I'm scared."],
 ['Ida', 'Ida know.  Sorry!'],
 ['Isabel', 'Isabel on a bike really necessary?'],
 ['Joan', "Joan call us, we'll call you."],
 ['Kay', 'Kay, L, M, N, O, P.'],
 ['Justin', 'Justin time for dinner.'],
 ['Liza', 'Liza wrong to tell.'],
 ['Luke', 'Luke and see who it is.'],
 ['Mandy', "Mandy the lifeboats, we're sinking."],
 ['Max', 'Max no difference - just open the door!'],
 ['Nettie', 'Nettie as a fruitcake.'],
 ['Olivia', 'Olivia me alone!'],
 ['Oscar', 'Oscar stupid question, you get a stupid answer.'],
 ['Patsy', 'Patsy dog on the head, he likes it.'],
 ['Paul', "Paul hard, the door's stuck again."],
 ['Thea', 'Thea later, alligator.'],
 ['Tyrone', "Tyrone shoelaces, you're old enough."],
 ['Stella', 'Stella no answer at the door.'],
 ['Uriah', 'Keep Uriah on the ball.'],
 ['Dwayne', "Dwayne the bathtub.  I'm drowning."],
 ['Dismay', "Dismay be a joke, but it didn't make me laugh."],
 ['Ocelot', "Ocelot of questions, don't you?"],
 ['Thermos', 'Thermos be a better knock knock joke than this.'],
 ['Sultan', 'Sultan Pepper.'],
 ['Vaughan', 'Vaughan day my prince will come.'],
 ['Donald', 'Donald come baby, cradle and all.'],
 ['Lettuce', "Lettuce in, won't you?"],
 ['Ivor', 'Ivor sore hand from knocking on your door!'],
 ['Isabel', 'Isabel broken, because I had to knock.'],
 ['Heywood, Hugh, Harry', 'Heywood Hugh Harry up and open this door.'],
 ['Juan', "Juan of this days you'll find out."],
 ['Earl', 'Earl be glad to tell you if you open this door.'],
 ['Abbot', 'Abbot time you opened this door!'],
 ['Ferdie', 'Ferdie last time, open the door!'],
 ['Don', 'Don mess around, just open the door.'],
 ['Sis', 'Sis any way to treat a friend?'],
 ['Isadore', 'Isadore open or locked?'],
 ['Harry', 'Harry up and let me in!'],
 ['Theodore', "Theodore wasn't open so I knocked-knocked."],
 ['Ken', 'Ken I come in?'],
 ['Boo', "There's no need to cry about it."],
 ['You', 'You who!  Is there anybody there?'],
 ['Ice cream', "Ice cream if you don't let me in."],
 ['Sarah', "Sarah 'nother way into this building?"],
 ['Mikey', 'Mikey dropped down the drain.'],
 ['Doris', 'Doris jammed again.'],
 ['Yelp', 'Yelp me, the door is stuck.'],
 ['Scold', 'Scold outside.'],
 ['Diana', 'Diana third, can I have a drink please?'],
 ['Doris', 'Doris slammed on my finger, open it quick!'],
 ['Lettuce', 'Lettuce tell you some knock knock jokes.'],
 ['Izzy', 'Izzy come, izzy go.'],
 ['Omar', 'Omar goodness gracious - wrong door!'],
 ['Says', "Says me, that's who!"],
 ['Duck', "Just duck, they're throwing things at us."],
 ['Tank', "You're welcome."],
 ['Eyes', 'Eyes got loads more knock knock jokes for you.'],
 ['Pizza', 'Pizza cake would be great right now.'],
 ['Closure', 'Closure mouth when you eat.'],
 ['Harriet', "Harriet all my lunch, I'm starving."],
 ['Wooden', 'Wooden you like to know?'],
 ['Punch', 'Not me, please.'],
 ['Gorilla', 'Gorilla me a hamburger.'],
 ['Jupiter', "Jupiter hurry, or you'll miss the trolley."],
 ['Bertha', 'Happy Bertha to you!'],
 ['Cows', 'Cows go "moo" not "who."'],
 ['Tuna fish', "You can tune a piano, but you can't tuna fish."],
 ['Consumption', 'Consumption be done about all these knock knock jokes?'],
 ['Banana', 'Banana spilt so ice creamed.'],
 ['X', 'X-tremely pleased to meet you.'],
 ['Haydn', 'Haydn seek is fun to play.'],
 ['Rhoda', 'Rhoda boat as fast as you can.'],
 ['Quacker', "Quacker 'nother bad joke and I'm off!"],
 ['Nana', 'Nana your business.'],
 ['Ether', 'Ether bunny.'],
 ['Little old lady', "My, you're good at yodelling!"],
 ['Beets', 'Beets me, I forgot the joke.'],
 ['Hal', 'Halloo to you too!'],
 ['Sarah', 'Sarah doctor in the house?'],
 ['Aileen', 'Aileen Dover and fell down.'],
 ['Atomic', 'Atomic ache'],
 ['Agatha', 'Agatha headache.  Got an aspirin?'],
 ['Stan', "Stan back, I'm going to sneeze."],
 ['Hatch', 'Bless you.'],
 ['Ida', "It's not Ida who, it's Idaho."],
 ['Zippy', 'Mrs. Zippy.'],
 ['Yukon', 'Yukon go away and come back another time.']]
SharedChatterGreetings = ['Hi, %!',
 'Loading Sculpture Plaque',
 "Loading Sculpture Plaque",
 'Loading Treasure Hunt Instructions']
SharedChatterComments = ["That's a great name, %.",
 'Loading Mancala Instructions',
 'Loading Card-Jitsu Instructions' + Cogs + '.',
 'Loading Card-Jitsu Fire Instructions',
 'Loading Instructions',
 'Loading Membership',
 'Loading Membership' + Cogs + 'Loading Membership',
 'Loading Membership' + Cogs + 'Loading Membership',
 "Loading Membership",
 "Loading Membership",
 "Loading Membership",
 "Loading Membership",
 'Loading Membership',
 'Loading Membership',
 "Loading Membership",
 'Loading Membership',
 'Loading Membership',
 'Loading Membership' + Cogs + 'Loading Membership',
 'Loading Membership',
 'Loading Membership',
 'Loading Membership',
 "Loading Membership",
 "Loading Membership",
 'Loading Membership' + Cogs + "Loading Membership",
 'Loading Membership' + Daisy + 'Loading Membership',
 'Loading Membership',
 'Loading Membership',
 'Loading Membership',
 'Loading Membership']
SharedChatterGoodbyes = ['I have to go now, bye!',
 "Loading Membership",
 "Loading Membership",
 "Loading Membership" + Cogs + '.',
 "Loading Membership",
 'Loading Membership',
 'Good-bye.',
 'Loading Membership',
 "Loading Membership",
 "Loading Membership" + Cogs + '.',
 'Loading Membership',
 "Loading Membership"]
MickeyChatter = (['Welcome to ' + lToontownCentral + '.', 'Hi, my name is ' + Mickey + ". What's yours?"], ['Hey, have you seen ' + Donald + '?',
  "Loading Membership" + lDonaldsDock + '.',
  'Loading Membership' + Goofy + 'Loading Membership',
  'I hear ' + Daisy + ' has planted some new flowers in her garden.'], ["I'm going to MelodyLand to see " + Minnie + '!',
  "Loading Membership" + Minnie + '!',
  "Loading Membership" + Pluto + "Loading Membership",
  "Loading Membership" + lDonaldsDock + '.',
  "Loading Membership"])
WinterMickeyCChatter = (["Hi, I'm Merry Mickey!",
  'January',
  'February',
  'Happy Winter Holiday, %'], ['Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  'March',
  'April',
  'May',
  'June',
  'July',
  'August',
  'September',
  'October',
  "November",
  'December',
  'day',
  'days',
  'Loading Newspaper',
  'Loading Last Week\'s Issue',
  "I think I'll trade my gloves for mittens!"], ['Have a happy Winter Holiday!',
  'Loading Old Issue',
  'Loading Old Issue',
  "Loading Old Issue"])
ValentinesMickeyChatter = (["Hi, I'm Mickey!",
  'Loading Old Issue',
  "Loading Old Issue",
  "Happy ValenToon's Day, %"], ['Love is in the air! And butterflies!',
  'Loading Recycle Hunt',
  'Loading Recycle Hunt',
  "Loading Recycle Hunt",
  "Loading Recycle Hunt",
  'Loading Scavenger Hunt',
  "Loading",
  'Will Minnie want chocolates or flowers?'], ['I loved having you visit!', "Tell Minnie I'll pick her up soon!"])
WinterMickeyDChatter = (["Hi, I'm Merry Mickey!",
  'SILLY SCAVENGER HUNT',
  'You have found',
  'Happy Winter Holiday, %'], ['Golly, these halls sure are decked!',
  'You have foundm piece',
  'You have foundm eggs',
  'Claim Prize',
  "Continue",
  'Elite Gear',
  'Field-Ops',
  "I think I'll trade my gloves for mittens!"], ['Have a happy Winter Holiday!',
  'Field-Ops',
  'Elite Puffle',
  "Recruit"])
VampireMickeyChatter = (['Welcome to ' + lToontownCentral + '.',
  'Objective' + Mickey + "Coming Soon",
  'EPF Message',
  'Congratulations',
  'Welcome to Tombtown... I mean Toontown!'], ['If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  "Puffle Whistle Message",
  'Field Op Complete',
  'Medal Earned!',
  'Messages',
  'WAIT!',
  'Do other people use this computer?',
  "If you save your password here, anyone who uses this computer could access your account.",
  'Save Password',
  'Don\'t Save Password',
  'Learn More',
  'They could spend your coins!',
  'They could change your igloo!',
  'They could get your penguin banned!',
  'You can\'t store more than 99 of these items.',
  "percentage",
  'Puffle Launch',
  "Loading Christmas Carol",
  'Penguin is playing Puffle Launch',
  "Would you like to play Puffle Launch?",
  'Loading Puffle Launch',
  'Vampires are really popular this year!'], ["I'm going to check out the cool Halloween decorations.",
  "You'll need to entermber more Treasure Book code(s) to unlock this page." + Minnie + '!',
  "Best Speed",
  "Normal",
  'Best Graphics'])
FieldOfficeMickeyChatter = ['Have you heard about the new Mover & Shaker Field Offices?']
MinnieChatter = (['Welcome to Melodyland.', 'Hi, my name is ' + Minnie + ". What's yours?"], ['The hills are alive with the sound of music!',
  'Please confirm your parent\'s email address. Club Penguin will send your parent an email with an activation code.',
  'Use this email' + Mickey + '?',
  'Please enter your parent\'s valid email address. Club Penguin will send your parent an email with an activation code.' + Goofy + 'Change this email',
  'There are too many accounts assigned to this email address to add a new one.' + Cogs + ' near ' + Donald + "The email address is not entered correctly.  Please try again.",
  "The given domain name is part of our banned email list. Please contact Club Penguin support if you have questions." + lDonaldsDock + '.',
  'Email is not properly formatted. Please try again.' + lDaisyGardens + '.',
  "An email address cannot contain a '+'. Please try again.",
  'Before you can login, your penguin account must be activated. Ask your parents to check their email.',
  'An email has been sent to with the next steps to activate your penguin.',
  "Penguin is on Santa's Sled",
  'Loading Membership',
  'Loading Catalogue',
  'Loading Catalogue',
  'Loading Catalog',
  'Is that a jellybean on the ground?'], ["Gosh, I'm late for my date with %s!" % Mickey, "Looks like it's time for %s's dinner." % Pluto, "It's time for a nap. I'm going to Dreamland."])
WinterMinnieCChatter = (["Hi, I'm Merry Minnie!",
  'Loading Catalog',
  'Club Penguin',
  'Happy Winter Holiday, %!'], ["You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  'Loading Club Penguin',
  "Penguin is in Club Penguin",
  'Club Penguin',
  "Games",
  'Places',
  "Shops",
  'Pets',
  "Ice Fishing",
  "Sled Racing",
  "Jet Pack Adventure",
  "Hydro Hopper",
  "Bean Counters",
  'Everything looks better with a wreath!'], ['Have a fun Winter Holiday!', 'Happy Trails!', 'Mickey is taking me caroling!'])
WinterMinnieDChatter = (["Hi, I'm Merry Minnie!",
  'Arcade',
  'Dance Contest',
  'Happy Winter Holiday, %!'], ['Belt out a tune, Toon!',
  'SoundStudio',
  'Puffle Roundup',
  'Pizzatron 3000',
  "Puffle Launch",
  "Cart Surfer",
  "Puffle Rescue",
  'Everything looks better with a wreath!'], ['Have a fun Winter Holiday!', 'Happy Trails!', 'Mickey is taking me caroling!'])
ValentinesMinnieChatter = (["Hello, I'm Minnie!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %"], ['I hope Mickey got me chocolates or flowers!',
  'Catchin\' Waves',
  'Aqua Grabber',
  'Card-Jitsu',
  'Penguin Style',
  'Costume Trunk',
  "Mickey has never missed a ValenToon's Day!"], ['It was sweet having you visit!'])
WitchMinnieChatter = (['Welcome to Magicland... I mean Melodyland!',
  "Pet Furniture",
  "Game Upgrade",
  'Music Catalog',
  'Happy Halloween, %!'], ['I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  "Game Upgrade",
  'Game Upgrade',
  'Game Upgrade',
  'Snow and Sports',
  'Abra-Cadabra!',
  'Game Upgrade',
  'Puffle Adoption',
  'Town',
  'The Plaza',
  'The Dock',
  'Snow Forts',
  'The Beach',
  'Ski Village',
  'Ski Hill',
  'Stadium',
  'Dojo Courtyard',
  'I hope you are enjoying our Halloween fun!'], ["I'm going to disappear now!", 'Time for me to vanish!', 'Mickey is taking me Trick-or-Treating!'])
FieldOfficeMinnieChatter = ['Everyone is talking about the new Mover & Shaker Field Offices!']
DaisyChatter = (['Welcome to my garden!', "Hello, I'm " + Daisy + ". What's your name?", "It's so nice to see you %!"], ['My prize winning flower is at the center of the garden maze.',
  'Mine',
  "Cove" + Goofy + 'Forest',
  'Iceberg' + Goofy + ' is.',
  'Open Igloos' + Donald + "Igloos",
  'Exclusive Bonus Items' + Minnie + '0 is not a valid email provider.  Please check the spelling and try again.',
  'Congratulations!',
  'You\'ve entered codes and unlocked the Super Exclusives page, and bonus items of your choice.' + Cogs + ' near ' + lDonaldsDock + '.',
  'I\'ve got a Code',
  'I\'ve got a Book',
  'Unlock your items. Choose an option.',
  'If you see sand under a plant it needs water or it will wilt!'], ["I'm going to Melody Land to see %s!" % Minnie,
  "I'm late for my picnic with %s!" % Donald,
  "Enter your code!" + lDonaldsDock + '.',
  "Make sure you enter it exactly as it appears."])
ValentinesDaisyChatter = (["Hi, I'm Daisy!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %"], ["I hope Donald doesn't get me another Amore Eel!",
  'Choose your book from the list below',
  'Hint: First line starts with the title!',
  'I\'ve got a code',
  "View Toys",
  'Exclusive Treasure Book',
  "Exclusive Bonus Items",
  'Maybe Donald and I can double-date with Mickey and Minnie!'], ["Tell Donald I'll be waiting for him!", "Have a nice ValenToon's Day!"])
WinterDaisyCChatter = (['Welcome to the only garden that grows in the winter!', 'Happy Winter Holiday!', 'Happy Winter Holiday, %!'], ['Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'You\'ve unlocked:',
  'Play now!',
  'Enter another code',
  'To unlock your toy code, you will be logged out of the game.',
  "Do you want to continue?",
  'To look at toys, you will be logged out of the game.',
  'Do you want to continue?',
  'Congratulations!',
  'These items have been added to your inventory!',
  'Bonus item unlocked!',
  'Because you already have [item name], you can now access a bonus Treasure Book item!',
  'Unlock Bonus Items',
  '0 added to your inventory. You already have the max number of puffles, so you get a bonus item!',
  'You already have the max number of hats, so you get a bonus item!',
  'I grew all these lights myself!'], ['Have a jolly Winter Holiday!',
  'You already have the max number of puffles and hats, so you get 2 bonus items!',
  'Your and its exclusive have been added to your igloo.',
  'Give your new puffle a name.'])
WinterDaisyDChatter = (['Welcome to the only garden that grows in the winter!', 'Happy Winter Holiday!', 'Happy Winter Holiday, %!'], ['My garden needs more mistletoe!',
  'Enter Penguin Name',
  "Enter Password",
  'Next',
  'Exclusive Bonus Items',
  'Congratulations!',
  'You\'ve entered codes and unlocked the Super Exclusives page, and bonus items of your choice.',
  'I grew all these lights myself!'], ['Have a jolly Winter Holiday!',
  'I\'ve got a Code',
  'I\'ve got a Book',
  'Unlock your items. Choose an option.'])
HalloweenDaisyChatter = (['Welcome to Daisy Ghosts... I mean Gardens!', 'Happy Halloween!', 'Happy Halloween, %!'], ['Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'Enter your code!',
  'Make sure you enter it exactly as it appears.',
  "Choose your book from the list below",
  'Hint: First line starts with the title!',
  'I\'ve got a code',
  'View Toys',
  'Trick-or-Tree!',
  'Exclusive Treasure Book',
  'You can\'t store more than 75 of this item.',
  'Drag here to remove',
  'Loading Treasure Book',
  'Please name your puffle.',
  'Congratulations! Your puffle has been added to your igloo.',
  'needs to eat.',
  'needs to sleep.',
  'wants to play.',
  'Twig-or-Treat!',
  'needs a bath.',
  "Hide Games",
  'Different colored puffles play different games.',
  'I hope you are enjoying our Halloween fun!'], ['Donald is taking me Trick-or-Treating!', "I'm going to check out the fun Halloween decorations."])
FieldOfficeDaisyChatter = ['Those Mover & Shaker Field Offices are popping up like weeds!']
ChipChatter = (['Welcome to %s!' % lOutdoorZone,
  "Show Games" + Chip + "Puffle Care",
  "Walk your puffle to its favorite game to play it." + Chip + '.',
  "Buy more food from",
  'We are Chip and Dale!'], ['I like golf.', 'We have the best acorns in Toontown.', 'The golf holes with volcanoes are the most challenging for me.'], ["We're going to the " + lTheBrrrgh + ' and play with %s.' % Pluto,
  "We'll visit %s and fix him." % Donald,
  "next" + lDonaldsDock + '.',
  "G'Day!"])
ValentinesChipChatter = (["I'm Chip!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ["What did you get me for ValenToon's Day, Dale?",
  'I\'m here to show you how to care for your puffles!',
  'Click these tabs to:',
  "feed",
  "I love ValenToon's Day!"], ['Come back any time!'])
WinterChipChatter = (['Happy Winter Holiday!', 'Dressed as chipmunks!', 'Happy Winter Holiday, %!'], ['Happy Winter Holiday, Dale!',
  'play',
  'clean',
  'rest',
  'When you run out of food,',
  'Did you get the Cogs a present?'], ['Go nuts this Winter Holiday!', 'Have a joyful winter Holiday!'])
HalloweenChipChatter = (['Play some MiniGhoul... I mean Golf!', 'Happy Halloween!', 'Happy Halloween, %!'], ["We're nuts about Halloween!",
  "click this catalog to buy more.",
  "Have fun,",
  "and good luck!",
  'and dress your puffle.',
  'done',
  'Walk your puffle to its favorite game to play it.',
  'I hope you are enjoying our Halloween fun!'], ['%, watch out for Bloodsucker Cogs!'])
DaleChatter = (["It's so nice to see you %!",
  "Your puffle's stats tell you when it is happy, sad, hungry, tired or messy." + Dale + "YOUR COINS",
  "Give them snacks, toys, baths, and sleep to fill their stats." + Chip + '.',
  'Welcome to %s!' % lOutdoorZone,
  'We are Chip and Dale!'], ['I like picnics.', 'Acorns are tasty, try some.', 'Those windmills can be hard too.'], ['Hihihi ' + Pluto + ' is fun to play with.',
  "Yeah, let's fix %s." % Donald,
  'Go to Pet Papers to view',
  "your Adoption Certificates."])
ValentinesDaleChatter = (["I'm Dale!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ['Same thing as last year. Nothing!',
  'Take your puffle for a walk and care for it at the Puffle Hotel!',
  'Care',
  'Adoption Certificate',
  "Yeah, it's all right."], ['Come back any time!'])
WinterDaleChatter = (['Merry chipmunks!',
  "Feed",
  'Puffle Handbook',
  'Happy Winter Holiday, %!'], ['Happy Winter Holiday, Chip!',
  'Play',
  'Pet Papers',
  'Care',
  'Groom',
  'Yes, a cream pie!'], ['And bring some back for us!', 'Have a joyful Winter Holiday!'])
HalloweenDaleChatter = (['Happy Halloween, %!', 'Play some MiniGhoul... I mean Golf!', 'Happy Halloween!'], ["We're nuts about Halloween!",
  'Sleep',
  'Dress Up',
  'Pet Stats',
  'Play',
  'needs to eat.',
  'I hope you are enjoying our Halloween fun!'], ['%, watch out for Bloodsucker Cogs!'])
GoofyChatter = (['Welcome to ' + lDaisyGardens + '.', 'Hi, my name is ' + Goofy + ". What's yours?", "Gawrsh, it's nice to see you %!"], ['Boy it sure is easy to get lost in the garden maze!',
  'needs to sleep.',
  "needs a bath." + Daisy + 'wants to play.',
  'Hide Games' + Daisy + ' is.',
  'Different colored puffles play different games' + Donald + '?',
  'Show Games' + Mickey + 'Puffle Care',
  "Buy more food from" + Mickey + "Walk your puffle to its favorite game to play it.",
  'next' + Cogs + ' near ' + lDonaldsDock + '.',
  'Im here to show you how to care for your puffles!' + Daisy + 'G\'Day',
  'Click these tabs to:',
  "feed",
  "At Goofy's Gag Shops, every pie in the face is guaranteed to make a laugh or you get your jellybeans back!"], ["I'm going to Melody Land to see %s!" % Mickey,
  "Gosh, I'm late for my game with %s!" % Donald,
  "play" + lDonaldsDock + '.',
  "clean"])
WinterGoofyChatter = (["I'm Goofy about the holidays!",
  'rest',
  'When you run out of food,',
  'Happy Winter Holiday, %!'], ['Who needs reindeer when you have a fast kart?',
  'click this catalog to buy more.',
  'Have fun,',
  "and good luck!",
  "Loading Yearbook 10/11",
  'and dress your puffle.',
  'done',
  'These karts are better than any old sleigh!'], ['Have a cheery Winter Holiday!', 'Drive safe, now!', 'Watch out for flying reindeer!'])
ValentinesGoofyChatter = (["I'm Goofy about ValenToon's Day!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ["Gawrsh! Is it ValenToon's Day already?",
  'Easter Egg Scavenger Hunt',
  'Claim Prize',
  'Continue',
  'num ghosts caught',
  'Make some new friends on the track!'], ['Drive safe, now!', 'Show some love out there!'])
GoofySpeedwayChatter = (['Welcome to ' + lGoofySpeedway + '.', 'Hi, my name is ' + Goofy + ". What's yours?", "Gawrsh, it's nice to see you %!"], ['Boy, I saw a terrific race earlier.',
  'num eggs found',
  'The first egg\'s hid near shining gold, Somewhere deep and dark and cold.',
  'The next egg\'s found near works of art, Plus lots of books to make you smart!',
  'This next egg\'s near a snowy shore. It\'s hidden well. You must explore.' + Donald + '?',
  'Search now near a tall white chair, For watching waves. The egg is there.' + Mickey + 'Now head towards a wooden shack. You\'re doing well, you\'re right on track!',
  "The next egg's near a chair that lifts. You're getting close, you must be swift!" + Mickey + "The next one's sure to make you smile. Just like you, this egg's got style.",
  'The last egg\'s near a big, bright light. You\'re almost done, the end\'s in sight.' + Cogs + ' near ' + lDonaldsDock + '.',
  'Go to settings to remove players on your ignore list.',
  "Would you like to addme",
  "At Goofy's Gag Shops, every pie in the face is guaranteed to make a laugh or you get your jellybeans back!"], ["I'm going to Melody Land to see %s!" % Mickey,
  "Gosh, I'm late for my game with %s!" % Donald,
  "to your Friends list?" + lDonaldsDock + '.',
  "Would you like to removeme from your Friends list?"])
SuperGoofyChatter = (['Welcome to my Super Speedway!',
  "Add Friend",
  'Remove Friend',
  'Happy Halloween, %!'], ['I am feeling kind of batty today!',
  'Show Friends',
  "Remove Friend",
  'Loading Pufflescape',
  "Penguin is playing Pufflescape",
  "Pufflescape",
  "Would you like to play Pufflescape?",
  "Loading Membership",
  'I hope you are enjoying our Halloween fun!'], ['Gotta fly!',
  'Sorry, you may only have four Card-Jitsu Mat igloo items.',
  "Card-Jitsu All Access ends Dec. 6. A membership will be required to play.",
  'Would you like to play'])
DonaldChatter = (['Welcome to Dreamland.', "Hi, my name is %s. What's yours?" % Donald], ['Sometimes this place gives me the creeps.',
  'Card-Jitsu Fire?' + lDaisyGardens + '.',
  "Would you like to play",
  'Card-Jitsu Water?' + Mickey + '?',
  'Card-Jitsu?' + Goofy + 'Would you like to play',
  "Earn Your Fire Suit",
  'Earn Your Water Suit' + Cogs + ' at ' + lDonaldsDock + '.',
  "Earn Your Belts" + lDonaldsDock + '?',
  "Loading the Ninja Hideout" + Daisy + 'Penguin is now offline',
  '100 coins were added to your account' + Daisy + 'Loading the Dojo Courtyard',
  'Quack.'], ["I'm going to Melody Land to see %s!" % Minnie,
  "Gosh, I'm late for my date with %s!" % Daisy,
  "250 coins were added to your account",
  "500 coins were added to your account"])
WinterDreamlandCChatter = (["Hi, I'm Dozing Donald!",
  'Mom and Dad',
  'Dad',
  'Happy Winter Holiday, %!'], ['Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  'Mom',
  'Pufflescape',
  "Ok",
  'Cancel',
  'Please enter your parent\'s valid email address. Club Penguin will send your parent an email with an activation code.',
  'Loading Poster',
  'Club Penguin Rules',
  'Loading CFC Poster',
  "CFC Poster",
  'Loading Advent Note',
  "Loading Advent Note",
  'Loading Advent Note',
  'The trees on the streets are covered in night lights!'], ['To all, a good night!', 'Sweet dreams!', 'When I wake up I am going caroling!'])
WinterDreamlandDChatter = (["Hi, I'm Dozing Donald!",
  'Loading Advent Note',
  'Loading Advent Note',
  'Happy Winter Holiday, %!'], ['I wish I was nestled all snug in my bed!',
  "Loading Advent Note",
  'Loading Advent Note',
  'Loading Advent Note',
  "Loading Advent Note",
  "Loading Advent Note",
  'The trees on the streets are covered in night lights!'], ['To all, a good night!', 'Sweet dreams!', 'When I wake up I am going caroling!'])
HalloweenDreamlandChatter = (['Happy Halloween!', 'Happy Halloween, %!', "Hi, I'm FrankenDonald!"], ['If you can play a trick on my friend Max, then you can Relax To The Max with a treat!',
  'Loading Advent Note',
  'Loading Advent Note',
  "Party 1",
  'Loading Poster',
  'Loading Note',
  'Loading Catalog',
  "You already have the max number of puffles, so you get a bonus item!",
  'Attempted Game Manipulation',
  "You've used up your time to play on Club Penguin for today. Your parent has set your play time to,.",
  'You have left to play Club Penguin today. Your parent has set your play time to,.',
  'I hope you are enjoying our Halloween fun!'], ['Sleep with the lights on tonight!', 'When I wake up, I am going Trick-or-Treating!'])
ValentinesDreamlandChatter = (["Hello, I'm (yawn) Donald!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ["I hope I don't sleep through ValenToon's Day!",
  "minute",
  "minutes",
  'hour',
  "hours",
  'Choose Your',
  "Puffle",
  'I love sleeping!'], ['Nite-nite!', "Wake me when it's ValenToon's Day!"])
FieldOfficeDreamlandChatter = ['I dreamed about something called a Field Office...']
HalloweenDonaldChatter = (['Welcome to my Halloween harbor!',
  'PH',
  'Your parent has changed your play time on Club Penguin to  ,.',
  'Happy Halloween, %!'], ['If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  "Sorry, you can only buy this item 99 times.",
  'Party 5',
  'Party 6',
  'Party 7',
  "Party 8",
  'You\'ve Been Hit!',
  "by from the Club Penguin App",
  'Would you like to throw one back?',
  'You\'ve thrown a snowball back at',
  'You\'ve Been Hit!',
  "Throw snowballs back?",
  'Snowballs thrown at!',
  'Your parent has changed your play time on Club Penguin to  ,.',
  'Are you prepared for battle?',
  'Your current igloo',
  'Edit',
  'I hope you are enjoying our Halloween fun!'], ['Set sail for scares!', 'Happy haunting!', "I'm going to check out the spooky Halloween decorations."])
ValentinesDonaldChatter = (["Ahoy, I'm Donald!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ["Was I supposed to take Daisy somewhere for ValenToon's Day?",
  "Igloo Visitors",
  "Friends",
  'Everyone',
  "Are you sure that you want to delete this igloo?",
  'Music',
  "I'll have to catch an Amore Eel for Daisy!"], ['Aloha!', 'Give the Cogs my best!'])
WinterDonaldCChatter = (["Welcome to Donald's Boat and Sleigh Dock!",
  'Hide',
  'Show',
  'Happy Winter Holiday, %!'], ['I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  'My Saved Tracks',
  'Igloo Music',
  'Go to DJ3K!',
  'Song Not Playing',
  'Go There!',
  'Record and save your',
  'own music mixes in DJ3K.',
  'Use arrow keys to change this item.',
  'Are you sure you want to add an igloo? Your flooring and igloo furniture will be saved in your inventory.',
  'Are you sure you want to move your igloo? Your flooring and igloo furniture will be saved in your inventory.',
  "Are you sure you want to remove your igloo? Your flooring and igloo furniture will be saved in your inventory.",
  'Popular',
  "Friends",
  'Everyone',
  'Likes',
  'You will lose all your LIKES for this igloo.',
  "OK",
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!'], ['All ashore for holiday fun!', 'Remember to tip your boat driver on the way out!', 'Enjoy your holiday!'])
WinterDonaldDChatter = (["Welcome to Donald's Boat and Sleigh Dock!",
  'OK',
  'OK',
  'Happy Winter Holiday, %!'], ['How do you like my duck-orations?',
  'Calling all heroes! Super Villains have been spotted at the Bank!',
  'Fires reported downtown! The city needs a hero!',
  'The police could use some back-up! Go to the Jail!',
  'Heroes - gather forces at the Super Hero HQ. For great justice!',
  "It's time to defeat evil once and for all! To the Super Villain Lair!",
  "Press Conference at the Coffee Shop. The city wants answers!",
  'Giant monsters spotted at the Iceberg! Move out!',
  "I hope I don't get a lump of coal again!"], ['All ashore for holiday fun!', 'Remember to tip your boat driver on the way out!', 'Enjoy your holiday!'])
WesternPlutoChatter = (["Boo! Don't be scared, it's just me ... Pluto!", 'Happy Halloween, pardner!', 'Happy Halloween, %!'], ["Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  'Defend the Club Penguin Times at any cost!',
  "The Bank vault is defenseless! You know what to do...",
  "Villains - join forces downtown. Nothing can stop us!",
  "All Super Villains, go to the Jail! Cause trouble, but don't get caught!",
  'The Super Heroes think their HQ is safe...',
  "Attention Villains! Meet up at the Lair for an evil planning session!",
  "No Super Villains allowed at the Coffee Shop. Wear a disguise. They'll never know it's you!",
  "Giant monsters, your time has come... to the Iceberg!",
  'Shut down the presses at the Club Penguin Times! First the newspaper... then the world!',
  "Super powered penguins spotted at the Bank! Also pizza!",
  'Fires reported downtown. Please expect traffic delays.',
  "Watch out for villains escaping the Jail! They ALWAYS do that!",
  "There's a snake in my boot!"], ["I'm going to go dig up a treat!", "I'm going to see if Mickey has some treats!", "I'm going to scare Donald!"])
WinterPlutoCChatter = (["Hi, I'm Pluto!",
  "Super Villains have been spotted heading to the Super Hero HQ!",
  'Super Heroes reported heading to the Super Villain Lair!',
  'Happy Winter Holiday, %'], ["Eddie could use a good tune, because Snowman's Land is a lonely place for a Yeti!",
  'Fresh coffee reported at the Coffee Shop! Also Super Heroes and Super Villains!',
  "Giant monsters spotted at the Iceberg! Run!",
  'Super Heroes and Villains spotted at the Club Penguin Times!',
  "Non-member trying to enter fort",
  'Grand Total Likes:',
  "Buy more wall items from the Furniture Catalog",
  'Buy more pet furniture from the Puffle Catalog in the Pet Shop',
  "Martial Artworks",
  "At least my nose isn't red and glowing!"], ['Have a fun Winter Holiday!', 'Come back any time you want snow!', 'Mickey is taking me caroling!'])
WinterPlutoDChatter = (["Hi, I'm Pluto!",
  "Buy more furniture from the Furniture Catalog",
  'Buy more flooring from the Furniture Catalog',
  'Happy Winter Holiday, %'], ['I chewed on an icicle and got frost-bite!',
  'Buy more igloos from the Igloo Catalog',
  'Feb',
  'Mar',
  "At least my nose isn't red and glowing!"], ['Have a fun Winter Holiday!', 'Come back any time you want snow!', 'Mickey is taking me caroling!'])
AFMickeyChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Welcome to the Gardens! I'm " + Daisy + '!',
  "I'm " + Daisy + 'Apr',
  "May",
  "Jun",
  "Aug" + Daisy + 'Jul',
  "Sept",
  "Oct",
  'Nov',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'Tell Mickey I said hi!'])
AFMinnieChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ['Welcome to ' + lTheBrrrgh + "! I'm " + Pluto + '!',
  "Jan" + Pluto + "Dec",
  "OK!",
  "OK!",
  "OK!",
  'Calling all heroes! Super Villains have been spotted at the Bank!' + Pluto + '!',
  "Fires reported downtown! The city needs a hero!",
  "The police could use some back-up! Go to the Jail!",
  "Heroes - gather forces at the Super Hero HQ. For great justice!",
  'It\'s time to defeat evil once and for all! To the Super Villain Lair!',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'I have to go chase cars now!  Bye!'])
AFDaisyChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ['Welcome to ' + lToontownCentral + "! I'm " + Mickey + ' Mouse!',
  "Giant monsters spotted at the Iceberg! Move out!" + Mickey + 'Press Conference at the Coffee Shop. The city wants answers!',
  'Villains - join forces downtown. Nothing can stop us!' + Daisy + 'The Bank vault is defenseless! You know what to do...' + Mickey + 'Defend the Club Penguin Times at any cost!',
  "All Super Villains, go to the Jail! Cause trouble, but don't get caught!",
  "The Super Heroes think their HQ is safe...",
  "Attention Villains! Meet up at the Lair for an evil planning session!",
  "No Super Villains allowed at the Coffee Shop. Wear a disguise. They'll never know it's you!",
  'Giant monsters, your time has come... to the Iceberg!',
  'Gravity has taken a holiday at the Estates!'], ['Bye! Tell them ' + Mickey + ' sent you!', 'If you go to ' + lDaisyGardens + ', say hi to her for me!'])
AFGoofySpeedwayChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Welcome to Dreamland! I'm " + Donald + '!',
  "Super powered penguins spotted at the Bank! Also pizza!" + Donald + 'Shut down the presses at the Club Penguin Times! First the newspaper... then the world!',
  'Fires reported downtown. Please expect traffic delays.',
  "Watch out for villains escaping the Jail! They ALWAYS do that!",
  'Super Villains have been spotted heading to the Super Hero HQ!',
  'Super Heroes reported heading to the Super Villain Lair!',
  "Fresh coffee reported at the Coffee Shop! Also Super Heroes and Super Villains!",
  "Giant monsters spotted at the Iceberg! Run!",
  'Super Heroes and Villains spotted at the Club Penguin Times!',
  'Gravity has taken a holiday at the Estates!'], ['If you see ' + Goofy + ', tell him ' + Donald + ' says hi!', 'Bye, and good night!'])
AFDonaldChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Welcome to the Speedway! I'm " + Goofy + '!',
  "I'm " + Goofy + "You already have this location." + Donald + '!',
  "Grand Total Likes",
  'Anonymous' + Goofy + '!',
  'Create a Penguin',
  'Learn more about Membership',
  "Scorn Battle",
  "Penguin is in an epic battle!",
  'Smoothie Smash',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'I need to work on my karts!  Bye!'])
AFDonaldDockChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Everybody gets April Toons' Week off but me!",
  "Would you like to play Smoothie Smash?",
  'Penguin is making smoothies.',
  'You\'ve unlocked items!',
  'We\'ve added them to your inventory.',
  'There are fruit items left to unlock.',
  "You've unlocked all the fruit items.",
  'Unlock your bonus item now!',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'Play a joke on the Cogs for me!'])
AFPlutoChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Welcome to Melodyland!  I'm " + Minnie + '!',
  'Pineapple Igloo Unlocked!' + Minnie + ' Mouse!',
  "You've unlocked all fruit items and earned the bonus Pineapple Igloo!",
  "You've unlocked more items!",
  'Unlock Bonus Item' + Mickey + 'We\'ve added them to your inventory.',
  'Make Smoothies',
  "Party 3",
  'Party 4',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'If you see ' + Pluto + ', tell him ' + Minnie + ' says hi!'])
AFChipChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Hi, I'm " + Dale + '!',
  'Access Security Terminal?' + Chip + '?',
  'Login to play!' + Dale + ', ' + Chip + '.',
  "Create" + Chip + 'OR' + Dale + ', ' + Chip + '?',
  "April Toons' Week is the silliest week of the year!"], ['Bye from ' + Chip + ' and ' + Dale + '!'])
AFDaleChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Hi, I'm " + Chip + '!',
  'Penguin is in the Cloud Forest' + Dale + 'Cloud Forest',
  "Hotel Lobby" + Chip + ', ' + Dale + '.',
  'Yes, ' + Dale + "Hotel Spa" + Chip + 'Penguin is in the Hotel Lobby' + Dale + '.',
  'It sure is, ' + Chip + '! I mean, ' + Dale + '.'], ['Or ' + Dale + ' and ' + Chip + '!'])
CLGoofySpeedwayChatter = (['Welcome to ' + lGoofySpeedway + '.',
  'Hotel Rooftop' + Goofy + "Penguin is in the Hotel Spa",
  "Penguin is in the Hotel Rooftop",
  "Hi there!  Pardon my dusty clothes I've been busy fixin' that broken Leaderboard."], ['We better get this Leaderboard working soon, Grand Prix Weekend is coming up!',
  "This rainbow puffle has chosen you!",
  'Choose a name',
  'Adopt',
  "Rainbow",
  'These majestic puffles enjoy the',
  'fantastical. They may be the only',
  'creature to have seen a real unicorn.',
  'Confident, regal',
  'Cloud',
  'Cloud surfing and riding down rainbows' + Donald + '?',
  'Farts sparkles' + Mickey + 'Rainbow lollipop',
  "10 coins were added to your account" + Mickey + "Rainbow Quest",
  '1000 coins were added to your account' + Cogs + ' near ' + lDonaldsDock + '.',
  '20 coins were added to your account',
  "50 coins were added to your account",
  "At Goofy's Gag Shops, every pie in the face is guaranteed to make a laugh or you get your jellybeans back!"], ['I better go get my kart a new paint job for the upcoming Grand Prix Weekend.',
  "Penguin is in the Hotel Spa",
  "Penguin is on the Hotel Roof",
  "Hotel Lobby"])
GPGoofySpeedwayChatter = (['Welcome to ' + lGoofySpeedway + '.',
  'Hotel Spa',
  'Mute All Sounds' + Goofy + "Hotel Rooftop",
  "Gawrsh, it's nice to see you %!"], ['Are you excited about the Grand Prix Weekend?',
  'You already have the max number of puffles. All other items have been added to your inventory.',
  'Would you like to buy 3 Power Cards forst coins?',
  "My Progress",
  'My progress',
  'Go back',
  'Next Reward',
  'Talk to Sensei to begin your Ninja journey.',
  'Become a Water Ninja. Discover the power of the wave.' + Donald + 'Become a Fire Ninja. Discover the power of the flame.',
  'Well done! Challenge Sensei to earn your Ninja Mask!' + Mickey + "Become a Snow Ninja. Discover the power of the flurry.",
  "Impressive skills! Challenge Sensei to become a Water Ninja!" + Mickey + "Excellent! Challenge Sensei to become a Fire Ninja!",
  'Ninja!' + Cogs + ' near ' + lDonaldsDock + '.',
  'Fire Ninja!',
  "Water Ninja!",
  "At Goofy's Gag Shops, every pie in the face is guaranteed to make a laugh or you get your jellybeans back!"], ['Good luck in the Grand Prix!',
  "Snow Ninja!",
  'My Cards',
  'I\'ve got a Code'])
SillyPhase1Chatter = ["If you haven't seen the Silly Meter, head to Toon Hall!",
 'Card-Jitsu Saga',
 "Unite with ninjas in Card-Jitsu Snow battle to unlock",
 'Long, Long Ago�',
 'Training Begins']
SillyPhase2Chatter = ['Silly levels are still rising!',
 'Snow Match',
 'Counter Strike',
 'Battle Snow Minions',
 'Blasted Back',
 'The Earth Quivered�',
 'A Broken Tusk']
SillyPhase3Chatter = ['The Cogs hated how silly Toontown was becoming!',
 'Challenge Tusk',
 'Tusk\'s Vow',
 'Tusk Defeated',
 'Redeeming Codes',
 'To unlock a card code, you will be logged out of the game. Do you want to continue?']
SillyPhase4Chatter = ['Fire hydrants make your Squirt Gags squirtier!',
 'Not�now',
 'Log out to redeem',
 'Spy Drills',
 "Would you like to play Spy Drills?",
 'Loading Spy Drills']
for chatter in [MickeyChatter,
 DonaldChatter,
 MinnieChatter,
 GoofyChatter]:
    chatter[0].extend(SharedChatterGreetings)
    chatter[1].extend(SharedChatterComments)
    chatter[2].extend(SharedChatterGoodbyes)

BoringTopic = 'Boring'
EmceeDialoguePhase1Topic = 'Penguin is in the Robot Factory'
EmceeDialoguePhase2Topic = 'These 3 Power Cards have been added to your inventory.'
EmceeDialoguePhase3Topic = 'Penguin is in the Snow Dojo'
EmceeDialoguePhase3_5Topic = 'EmceeDialoguePhase3.5'
EmceeDialoguePhase4Topic = 'Snow Dojo'
EmceeDialoguePhase5Topic = 'Would you like to play'
EmceeDialoguePhase6Topic = 'Card-Jitsu Snow?'
AprilToonsPhasePreTopTopic = 'Snow Gem'
AprilToonsPhaseTopTopic = 'Your coins:'
AprilToonsExtPhaseTopTopic = '0'
AprilToonsPhasePostTopTopic = 'Your puffles:'
toontownDialogues = {BoringTopic: {(1, 2018): ['Hello Albert', 'It looks like the sillyness levels are rising', 'Yes and dont forget April Toons!'],
               (2, 2019): ['Hello Newton', 'Yes I wonder how much the parties are contributing to all this'],
               (3, 2020): ['Why hello there Albert and Newton', 'Halloween was pretty silly too!']},
 AprilToonsPhasePreTopTopic: {(1, 2020): ['Gadzooks! The Silly Meter has come back to life!',
                                          "Puffles for everyone",
                                          'Quest for a Rainbow Puffle',
                                          'Go to the Puffle Hotel']},
 AprilToonsPhaseTopTopic: {(1, 2020): ['The Silly Meter has hit the top!',
                                       'Complete all four tasks in the Puffle Care Quest',
                                       "Launch into the Cloud Forest to meet their new pet!",
                                       'Learn More About Membership']},
 AprilToonsExtPhaseTopTopic: {(1, 2020): ['The Silly Meter has hit the top!', 'Doodles are talking, Estates are bouncy!']},
 AprilToonsPhasePostTopTopic: {(1, 2020): ['April Toons is over!',
                                           "Go to Puffle Hotel",
                                           'pufflename found',
                                           'Everyone\'s puffles can dig up coins!']},
 EmceeDialoguePhase1Topic: {(1, 2020): ['Fellow Toons, this is the Silly Meter!',
                                        "0 found coins!",
                                        '0 was added to your inventory!',
                                        'Send your puffle back to the wilds',
                                        'Treasure',
                                        'Games',
                                        "Taking some puffles into games can help you earn more coins!",
                                        "Click your puffle's leash to take it for a walk."]},
 EmceeDialoguePhase2Topic: {(1, 2020): ['Good Gag work, Toons!',
                                        "To send it back to your igloo, open your player card and click your puffle.",
                                        'Penguin is playing Card-Jitsu Snow',
                                        'Puffle Treasure',
                                        'Members can walk puffles for the chance to find rare items.',
                                        "Penguin is learning how to scare",
                                        'Penguin is in the University']},
 EmceeDialoguePhase3Topic: {(1, 2020): ['Gadzooks! The Silly Meter is even crazier than expected!',
                                        'About Membership',
                                        'Clear Igloo',
                                        'Are you sure you want to clear this player\'s igloo?',
                                        'A Moderator has cleared your igloo because it was inappropriate.',
                                        "Please remember to follow the Club Penguin rules.",
                                        'Oops! You used a rude or inappropriate word.']},
 EmceeDialoguePhase3_5Topic: {(1, 2020): ['YOU DID IT TOONS!',
                                          'If you break a Club Penguin rule again, you may be banned.',
                                          'A Moderator removed you from this server.',
                                          'Please remember to follow the Club Penguin rules.',
                                          'You used a rude or inappropriate word.']},
 EmceeDialoguePhase4Topic: {(1, 2020): ['Attention all Toons!',
                                        'This penguin account has been banned for hours.',
                                        'You were caught cheating.',
                                        'BANNED',
                                        'Club Penguin Rules',
                                        "Respect others",
                                        'No bullying or being mean to others']},
 EmceeDialoguePhase5Topic: {(1, 2020): ['Attention all Toons!',
                                        'Chat nicely',
                                        'No rude or inappropriate language',
                                        'Stay safe online',
                                        'No sharing personal information',
                                        'Play fair',
                                        'No cheating or use of third party programs']},
 EmceeDialoguePhase6Topic: {(1, 2020): ['Congratulations Toons!',
                                        'Rules',
                                        'Population',
                                        'Buy Power Cards',
                                        'Members Only',
                                        '(0 ban)',
                                        '(0 bans)']}}
FriendsListPanelNewFriend = 'Ban for saying'
FriendsListPanelSecrets = 'Bullying'
FriendsListPanelOnlineFriends = 'Inappropriate words'
FriendsListPanelAllFriends = 'Shared personal info'
FriendsListPanelIgnoredFriends = 'IGNORED\nTOONS'
FriendsListPanelPets = 'NEARBY\nPETS'
FriendsListPanelPlayers = 'Cheating'
FriendsListPanelOnlinePlayers = 'Warning only'
FriendInviterClickToon = 'Click on the toon you would like to make friends with.\n\n(You have %s friends)'
FriendInviterToon = 'Toon'
FriendInviterThatToon = '24 hrs'
FriendInviterPlayer = 'Player'
FriendInviterThatPlayer = '72 hrs'
FriendInviterBegin = 'Permanently'
FriendInviterToonFriendInfo = 'BAN!'
FriendInviterPlayerFriendInfo = 'Notes:'
FriendInviterToonTooMany = 'You have too many toon friends to add another one now. You will have to remove some toon friends if you want to make friends with %s. You could also try making player friends them.'
FriendInviterPlayerTooMany = 'You have too many player friends to add another one now. You will have to remove some player friends if you want to make friends with %s. You could also try making toon friends with them.'
FriendInviterToonAlready = '%s is already your toon friend.'
FriendInviterPlayerAlready = '%s is already your player friend.'
FriendInviterStopBeingToonFriends = 'Comments are saved on player\'s record'
FriendInviterStopBeingPlayerFriends = 'WARNED'
FriendInviterEndFriendshipToon = 'Are you sure you want to stop being toon friends with %s?'
FriendInviterEndFriendshipPlayer = 'Are you sure you want to stop being player friends with %s?'
FriendInviterRemainToon = '\n(You will still be toon friends with %s)'
FriendInviterRemainPlayer = '\n(You will still be player friends with %s)'
DownloadForceAcknowledgeVerbList = ['painted',
 'unpacked',
 'unfolded',
 'drawn',
 'inflated',
 'built']
DownloadForceAcknowledgeMsg = 'Sorry, the %(phase)s area is still being %(verb)s, and will be ready for you in a minute.'
TeaserTop = ''
TeaserBottom = ''
TeaserDefault = 'Warn again'
TeaserOtherHoods = 'You were disrespectful to others.'
TeaserTypeAName = 'You shared personal information.'
TeaserSixToons = 'This penguin has been permanently banned for repeatedly not following the Club Penguin rules.'
TeaserClothing = 'You�ve used up your time to play today. Your parent has set your play time to -'
TeaserCogHQ = 'You have left to play on Club Penguin today. Your parent has set your play time to -'
TeaserSecretChat = '0, the island needs you.'
TeaserSpecies = 'Become an agent and help protect Club Penguin.'
TeaserFishing = 'Will you take up the challenge?'
TeaserGolf = 'Welcome to the Elite Penguin Force Agent (0).'
TeaserParties = 'Here\'s your spy phone - your most important tool.'
TeaserSubscribe = 'Subscribe'
TeaserContinue = 'Keep it on you to receive your orders.'
TeaserEmotions = 'Very well. Carry on.'
TeaserKarting = 'If you change your mind, give us a call.'
TeaserKartingAccessories = 'Add phone'
TeaserGardening = 'The Director'
TeaserHaveFun = 'We look forward to working with you, agent.'
TeaserJoinUs = 'Enter the Command Room to hone your skills.'
TeaserPlantGags = 'And good luck.'
TeaserPickGags = 'OK'
TeaserRestockGags = 'Favorite Foods'
TeaserGetGags = 'Members can walk their puffles for the chance to find their favorite food.'
TeaserUseGags = 'Feed your puffle their favorite snack and their stats will go up to 100!'
TeaserMinigames = TeaserOtherHoods
TeaserQuests = TeaserOtherHoods
TeaserOtherGags = TeaserOtherHoods
TeaserTricks = TeaserOtherHoods
LauncherPhaseNames = {0: 'Initialization',
 1: 'Panda',
 2: 'Engine',
 3: 'Make-A-Toon',
 3.5: 'Toontorial',
 4: 'Playground',
 5: 'Streets',
 5.5: 'Estates',
 6: 'Fish Burger',
 7: Cog + ' Buildings',
 8: 'Pretzels',
 9: Sellbot + ' HQ',
 10: Cashbot + ' HQ',
 11: Lawbot + ' HQ',
 12: Bossbot + ' HQ',
 13: 'Parties'}
LauncherProgress = '%(name)s (%(current)s of %(total)s)'
LauncherStartingMessage = "Astronaut"
LauncherDownloadFile = 'Ice Cream' + LauncherProgress + '...'
LauncherDownloadFileBytes = 'Tacos' + LauncherProgress + ': %(bytes)s'
LauncherDownloadFilePercent = 'Socks' + LauncherProgress + ': %(percent)s%%'
LauncherDecompressingFile = 'Watermelon' + LauncherProgress + '...'
LauncherDecompressingPercent = 'Hummus' + LauncherProgress + ': %(percent)s%%'
LauncherExtractingFile = 'and Pita' + LauncherProgress + '...'
LauncherExtractingPercent = 'Rainbow' + LauncherProgress + ': %(percent)s%%'
LauncherPatchingFile = 'Lollipop' + LauncherProgress + '...'
LauncherPatchingPercent = 'Stinky' + LauncherProgress + ': %(percent)s%%'
LauncherConnectProxyAttempt = 'Connecting to Toontown: %s (proxy: %s) attempt: %s'
LauncherConnectAttempt = 'Connecting to Toontown: %s attempt %s'
LauncherDownloadServerFileList = 'Cheese'
LauncherCreatingDownloadDb = 'Yogurt Parfait'
LauncherDownloadClientFileList = 'Popcorn'
LauncherFinishedDownloadDb = 'Puffle Treasure Hunting'
LauncherStartingGame = 'Take good care'
LauncherRecoverFiles = 'of your pet!'
LauncherCheckUpdates = 'Healthy puffles can' + LauncherProgress
LauncherVerifyPhase = 'dig up more coins.'
LoadingDownloadWatcherUpdate = 'Loading %s'
AvatarChoiceMakeAToon = 'Take a break'
AvatarChoicePlayThisToon = 'while walking.'
AvatarChoiceSubscribersOnly = 'Subscribe'
AvatarChoiceDelete = 'Delete'
AvatarChoiceDeleteConfirm = 'This will delete %s forever.'
AvatarChoiceNameRejected = 'Name\nRejected'
AvatarChoiceNameApproved = 'Name\nApproved!'
AvatarChoiceNameReview = 'Under\nReview'
AvatarChoiceNameYourToon = 'Puffles can hunt for'
AvatarChoiceDeletePasswordText = 'Careful! This will delete %s forever.  To delete this Toon, enter your password.'
AvatarChoiceDeleteConfirmText = 'Careful! This will delete %(name)s forever.  If you are sure you want to do this, type "%(confirm)s" and click OK.'
AvatarChoiceDeleteConfirmUserTypes = 'delete'
AvatarChoiceDeletePasswordTitle = 'treasure when you stop.'
AvatarChoicePassword = 'Password'
AvatarChoiceDeletePasswordOK = lOK
AvatarChoiceDeletePasswordCancel = lCancel
AvatarChoiceDeleteWrongPassword = 'If your puffle finds'
AvatarChoiceDeleteWrongConfirm = 'You did not type the right thing.  To delete %(name)s, type "%(confirm)s" and click OK.  Do not type the quotation marks.  Click Cancel if you have changed your mind.'
AvatarChooserPickAToon = 'treasure, it\'ll start digging.'
AvatarChooserQuit = lQuit
DateOfBirthEntryMonths = ['Jan',
 'Feb',
 'Mar',
 'Apr',
 'May',
 'Jun',
 'Jul',
 'Aug',
 'Sep',
 'Oct',
 'Nov',
 'Dec']
DateOfBirthEntryDefaultLabel = 'If not, try another spot.'
AchievePageTitle = 'OK'
PhotoPageTitle = 'on'
BuildingPageTitle = 'the'
InventoryPageTitle = 'Gags'
InventoryPageDeleteTitle = 'MENU'
InventoryPageTrackFull = 'You have all the gags in the %s track.'
InventoryPagePluralPoints = 'You will get a new\n%(trackName)s gag when you\nget %(numPoints)s more %(trackName)s points.'
InventoryPageSinglePoint = 'You will get a new\n%(trackName)s gag when you\nget %(numPoints)s more %(trackName)s point.'
InventoryPageNoAccess = 'You do not have access to the %s track yet.'
NPCFriendPageTitle = 'Walk your puffle to feed it at the'
PartyDateFormat = '%(mm)s %(dd)d, %(yyyy).4d'
PartyTimeFormat = '%d:%.2d %s'
PartyTimeFormatMeridiemAM = 'am'
PartyTimeFormatMeridiemPM = 'pm'
PartyCanStart = "Snack Stations!"
PartyHasStartedAcceptedInvite = '%s party has started!  Click the host then "Go To Party" in the Shticker Book Invites page.'
PartyHasStartedNotAcceptedInvite = '%s party has started! You can still go to it by teleporting to the host.'
EventsPageName = 'Events'
EventsPageCalendarTabName = 'Calendar'
EventsPageCalendarTabParty = 'Party'
EventsPageToontownTimeIs = 'Uh-oh!'
EventsPageConfirmCancel = 'If you cancel, you will get a %d%% refund. Are you sure you want to cancel your party?'
EventsPageCancelPartyResultOk = 'Your party was cancelled and you got %d jellybeans back!'
EventsPageCancelPartyResultError = 'You\'ll need more coins'
EventsPageCancelPartyAlreadyRefunded = 'to get this item.'
EventsPageTooLateToStart = 'Earn more coins by'
EventsPagePublicPrivateChange = "Playing games"
EventsPagePublicPrivateNoGo = "Walking your puffle"
EventsPagePublicPrivateAlreadyStarted = "Go There!"
EventsPageHostTabName = 'Hosting'
EventsPageHostTabTitle = 'OK'
EventsPageHostTabTitleNoParties = 'You\'ll need more coins'
EventsPageHostTabDateTimeLabel = 'You are having a party on %s at %s Toontown Time.'
EventsPageHostingTabNoParty = 'to send this postcard.'
EventsPageHostTabPublicPrivateLabel = 'Gold'
EventsPageHostTabToggleToPrivate = 'Private'
EventsPageHostTabToggleToPublic = 'Public'
EventsPageHostingTabGuestListTitle = 'Guests'
EventsPageHostingTabActivityListTitle = 'Activities'
EventsPageHostingTabDecorationsListTitle = 'Decorations'
EventsPageHostingTabPartiesListTitle = 'Hosts'
EventsPageHostTabCancelButton = 'The legendary gold puffles live near'
EventsPageGoButton = 'Start\nParty!'
EventsPageGoBackButton = 'Party\nNow!'
EventsPageInviteGoButton = 'gold deposits in the earth\'s crust. They'
EventsPageUnknownToon = 'are known to dig up rare golden items.'
EventsPageInvitedTabName = 'Invitations'
EventsPageInvitedTabTitle = 'Lucky, energetic'
EventsPageInvitedTabInvitationListTitle = 'Invitations'
EventsPageInvitedTabActivityListTitle = 'Activities'
EventsPageInvitedTabTime = '%s %s Toontown Time'
EventsPageNewsTabName = 'News'
EventsPageNewsTabTitle = 'News'
EventsPageNewsDownloading = 'Jackhammer'
EventsPageNewsUnavailable = 'Distracted by golden objects'
EventsPageNewsPaperTitle = 'Chocolate coins'
EventsPageNewsLeftSubtitle = 'Hide-and-Seek'
EventsPageNewsRightSubtitle = 'Champion'
NewsPageName = 'News'
NewsPageImportError = 'Chocolate'
NewsPageDownloadingNewsSubstr = 'Coins'
NewsPageDownloadingNews0 = NewsPageDownloadingNewsSubstr + ' %s%% Complete.'
NewsPageDownloadingNews1 = NewsPageDownloadingNewsSubstr + ' %s%% Complete..'
NewsPageDownloadingNews2 = NewsPageDownloadingNewsSubstr + ' %s%% Complete...'
NewsPageErrorDownloadingFile = 'Whoops! Page %s is missing from "Toon News ... for the Amused!" Please check back later.'
NewsPageErrorDownloadingFileCanStillRead = 'Whoops! Page %s \nis missing from the "Toon News ... for the Amused!" \nTurn the page to continue, while we work to get this page back.'
NewsPageNoIssues = 'Oops!'
IssueFrameThisWeek = 'left to activate your account. Unactivated accounts will be deleted.'
IssueFrameLastWeek = 'Your parent needs to activate your account so you can keep playing. Ask them to check their email for the activation link.'
IssueFrameWeeksAgo = '%d weeks ago'
SelectedInvitationInformation = '%s is having a party on %s at %s Toontown Time.'
PartyPlannerNextButton = 'Continue'
PartyPlannerPreviousButton = 'Back'
PartyPlannerWelcomeTitle = 'Didn\'t get an email?'
PartyPlannerInstructions = 'OK'
PartyPlannerDateTitle = 'Welcome to Club Penguin!'
PartyPlannerTimeTitle = 'You can waddle around without activating for'
PartyPlannerGuestTitle = 'Ask your parent to check their email.'
PartyPlannerEditorTitle = 'after the trial period, unactivated accounts will be deleted.'
PartyPlannerConfirmTitle = 'Welcome back!'
PartyPlannerConfirmTitleNoFriends = 'You can waddle around without activating for'
PartyPlannerTimeToontown = 'Toontown'
PartyPlannerTimeTime = 'Time'
PartyPlannerTimeRecap = 'Activate account to enable chat.'
PartyPlannerPartyNow = 'Dig up gold nuggets!'
PartyPlannerTimeToontownTime = 'You can dig for gold nuggets until you log off. Any gold nuggets you collect will be saved.'
PartyPlannerTimeLocalTime = 'Take the gold nuggets to the Gold Mine to activate the jackhammer.'
PartyPlannerPublicPrivateLabel = 'Go There!'
PartyPlannerPublicDescription = 'Insert coins below to feed'
PartyPlannerPrivateDescription = 'your puffle a gold O\'berry'
PartyPlannerPublic = 'Public'
PartyPlannerPrivate = 'Private'
PartyPlannerCheckAll = 'Check\nAll'
PartyPlannerUncheckAll = 'Uncheck\nAll'
PartyPlannerDateText = 'Date'
PartyPlannerTimeText = 'Time'
PartyPlannerTTTimeText = 'Walk your puffle anywhere to dig up gold nuggets.'
PartyPlannerEditorInstructionsIdle = 'Bring the gold nuggets to the Gold Mine'
PartyPlannerEditorInstructionsClickedElementActivity = 'to activate the jackhammer!'
PartyPlannerEditorInstructionsClickedElementDecoration = 'You already have the'
PartyPlannerEditorInstructionsDraggingActivity = 'max number of puffles.'
PartyPlannerEditorInstructionsDraggingDecoration = 'Walk your puffle here'
PartyPlannerEditorInstructionsPartyGrounds = 'to feed it a gold O\'berry!'
PartyPlannerEditorInstructionsTrash = 'Your Coins:'
PartyPlannerEditorInstructionsNoRoom = 'INSERT'
PartyPlannerEditorInstructionsRemoved = '%(removed)s removed since %(added)s was added.'
PartyPlannerBeans = 'beans'
PartyPlannerTotalCost = 'Total Cost:\n%d beans'
PartyPlannerSoldOut = '0 found 1 gold nugget!'
PartyPlannerBuy = 'BUY'
PartyPlannerPaidOnly = '0 found gold nuggets!'
PartyPlannerPartyGrounds = 'Gold Puffle Quest'
PartyPlannerOkWithGroundsLayout = 'You need more gold nuggets'
PartyPlannerChooseFutureTime = 'to activate the jackhammer.'
PartyPlannerInviteButton = 'Go to the Pet Shop with'
PartyPlannerInviteButtonNoFriends = 'a puffle to start your quest.'
PartyPlannerBirthdayTheme = 'Birthday'
PartyPlannerGenericMaleTheme = 'Star'
PartyPlannerGenericFemaleTheme = 'Flower'
PartyPlannerRacingTheme = 'Racing'
PartyPlannerValentoonsTheme = 'ValenToons'
PartyPlannerVictoryPartyTheme = 'Victory'
PartyPlannerWinterPartyTheme = 'Winter'
PartyPlannerGuestName = 'You already own the maximum'
PartyPlannerClosePlanner = 'number of puffles!'
PartyPlannerConfirmationAllOkTitle = 'You found'
PartyPlannerConfirmationAllOkText = 'a gold puffle!'
PartyPlannerConfirmationAllOkTextNoFriends = 'Congratulations!'
PartyPlannerConfirmationErrorTitle = 'Oops.'
PartyPlannerConfirmationValidationErrorText = 'Your new puffle comes with its very own'
PartyPlannerConfirmationDatabaseErrorText = "adoption certificate and exclusive toy."
PartyPlannerConfirmationTooManyText = 'Adoption'
PartyPlannerInvitationThemeWhatSentence = 'You are invited to my %s party! %s!'
PartyPlannerInvitationThemeWhatSentenceNoFriends = 'I am hosting a %s party! %s!'
PartyPlannerInvitationThemeWhatActivitiesBeginning = 'Certificate'
PartyPlannerInvitationWhoseSentence = '%s Party'
PartyPlannerInvitationTheme = 'Theme'
PartyPlannerInvitationWhenSentence = 'It will be on %s,\nat %s Toontown Time.\nHope you can make it!'
PartyPlannerInvitationWhenSentenceNoFriends = 'It will be on %s,\nat %s Toontown Time.\nToontastic!'
PartyPlannerComingSoon = 'Toy'
PartyPlannerCantBuy = "Members can:"
PartyPlannerGenericName = 'Feed your puffle a gold'
PartyJukeboxOccupied = 'O\'berry to begin your quest.'
PartyJukeboxNowPlaying = 'Learn More'
MusicEncntrGeneralBg = 'About Membership'
MusicTcSzActivity = 'OK'
MusicTcSz = 'Resend activation email to'
MusicCreateAToon = 'Parent email address'
MusicTtTheme = 'Send Email'
MusicMinigameRace = 'Re-send email'
MusicMgPairing = 'Change email'
MusicTcNbrhood = 'You can waddle around without activating for more hours.'
MusicMgDiving = 'You have one more hour to play without activating.'
MusicMgCannonGame = 'By activating your account you can keep exploring, chatting, adding friends, and more!'
MusicMgTwodgame = 'You have less than one hour to activate your account. Unactivated accounts will be deleted.'
MusicMgCogthief = '0'
MusicMgTravel = 'days'
MusicMgTugOWar = 'Tug-of-War'
MusicMgVine = '0'
MusicMgIcegame = 'hour(s)'
MusicMgToontag = 'An activation link was sent to'
MusicMMatchBg2 = 'Resend activation email to'
MusicMgTarget = "Adding an igloo requires"
MusicFfSafezone = 'a paid membership'
MusicDdSz = 'Members can:'
MusicMmNbrhood = "Save more unique igloo designs"
MusicGzPlaygolf = "Decorate their perfect igloo with the latest furniture"
MusicGsSz = 'Unlock their igloos and throw parties for their friends'
MusicOzSz = "About Membership"
MusicGsRaceCc = 'Adopting more than two puffles'
MusicGsRaceSs = 'requires a paid membership'
MusicGsRaceRr = 'Members can:'
MusicGzSz = 'Adopt a pet puffle in every color'
MusicMmSz = 'Care for up to 75 puffles'
MusicMmSzActivity = 'Buy special toys and furnitur items for their pets'
MusicDdNbrhood = "About Membership"
MusicGsKartshop = 'This requires a paid membership'
MusicDdSzActivity = 'Members can:'
MusicEncntrGeneralBgIndoor = 'Buy new clothing styles every month'
MusicTtElevator = 'Design their own clothes'
MusicEncntrToonWinningIndoor = 'Wear the latest party outfits'
MusicEncntrGeneralSuitWinningIndoor = 'Cog-tastrophe!'
MusicTbNbrhood = 'About Membership'
MusicDlNbrhood = "Stage Costumes require"
MusicDlSzActivity = 'a paid membership'
MusicDgSz = 'Members can:'
MusicDlSz = 'Sleepwalking'
MusicTbSzActivity = 'Purchase costumes to wear everywhere'
MusicTbSz = 'Dress up and act on the Stage'
MusicDgNbrhood = "Change their looks with the latest styles"
MusicEncntrHallOfFame = 'About Membership'
MusicEncntrSuitHqNbrhood = 'Igloo Upgrades require a'
MusicChqFactBg = 'paid membership'
MusicCoghqFinale = 'Members can:'
MusicEncntrToonWinning = 'Upgrade to the latest igloos'
MusicEncntrSuitWinning = 'Customize the flooring in their igloo'
MusicEncntrHeadSuitTheme = 'Decorate their igloo with furniture items'
MusicLbJurybg = 'About Membership'
MusicLbCourtyard = 'Igloo Furniture and Items'
MusicBossbotCeoV2 = 'require a paid membership'
MusicBossbotFactoryV1 = 'Members can:'
MusicBossbotCeoV1 = 'Purchase furniture for their igloo'
MusicPartyOriginalTheme = 'Design custom furniture for their igloo'
MusicPartyPolkaDance = 'Decorate their igloo any way they want'
MusicPartySwingDance = 'About Membership'
MusicPartyWaltzDance = 'Instruments from the Music Catalog'
MusicPartyGenericThemeJazzy = 'require a paid membership'
MusicPartyGenericTheme = 'About Membership'
JukeboxAddSong = 'Add\nSong'
JukeboxReplaceSong = 'Replace\nSong'
JukeboxQueueLabel = 'Ninja items require'
JukeboxSongsLabel = 'a paid membership'
JukeboxClose = 'Done'
JukeboxCurrentlyPlaying = 'Members can:'
JukeboxCurrentlyPlayingNothing = 'Design igloos with exclusive ninja furniture'
JukeboxCurrentSongNothing = 'Wear ninja outfits to unlock special moves'
PartyOverWarningNoName = 'Train in their igloos with Card-Jitsu mats'
PartyOverWarningWithName = '%s party has ended! Thanks for coming!'
PartyCountdownClockText = 'Time\n\nLeft'
PartyTitleText = '%s Party'
PartyActivityConjunction = 'Earn rewards faster with more Power Cards'
PartyActivityNameDict = {0: {'generic': 'About Membership',
     'invite': 'Puffle furniture and items',
     'editor': 'require a paid membership',
     'description': 'Members can:'},
 1: {'generic': 'Buy furniture for puffles to play with',
     'invite': 'Get the latest hats for their pets to wear',
     'editor': 'Cannons',
     'description': 'Adopt up to 75 different pet puffles'},
 2: {'generic': 'Trampoline',
     'invite': 'Trampoline',
     'editor': 'Trampoline',
     'description': 'About Membership'},
 3: {'generic': 'Rockhopper\'s rare items',
     'invite': 'require a paid membership',
     'editor': 'About Membership',
     'description': 'Additional sleds require'},
 4: {'generic': 'a paid membership',
     'invite': 'Members can:',
     'editor': 'About Membership',
     'description': 'Snow & Sports gear requires'},
 5: {'generic': 'a paid membership',
     'invite': 'About Membership',
     'editor': 'Tug-of-War',
     'description': 'Snow & Sports gear requires'},
 6: {'generic': 'a paid membership',
     'invite': 'Members can:',
     'editor': 'Fireworks',
     'description': 'Shop for snow and sports gear'},
 7: {'generic': 'Purchase special sport igloo items',
     'invite': 'Buy sporty backgrounds',
     'editor': 'About Membership',
     'description': 'Additional surfboards for Catchin\''},
 8: {'generic': 'Waves require a paid membership',
     'invite': 'Members can:',
     'editor': 'Buy the Daisy Surfboard to take into the game',
     'description': 'Buy the Flame Surfboard to take into the game'},
 9: {'generic': 'About Membership',
     'invite': 'Equipping this Elite Gear',
     'editor': 'requires a paid membership.',
     'description': 'About Membership'},
 10: {'generic': 'Cog-O-War',
      'invite': 'Cog-O-War',
      'editor': 'Cog-O-War',
      'description': 'EPF gear requires'},
 11: {'generic': 'a paid membership',
      'invite': 'Members can:',
      'editor': 'Access and wear their Elite Gear',
      'description': "Customize their secret agent looks"},
 12: {'generic': 'About Membership',
      'invite': 'Unlocking the Elite Puffle Whistle',
      'editor': 'requires a paid membership',
      'description': 'Members can:'},
 13: {'generic': 'Enter a code from Club Penguin Elite Penguin',
      'invite': 'Force: Herbert\'s Revenge Nintendo DS game to',
      'editor': 'call Flare, the elite black puffle.',
      'description': 'About Membership'},
 14: {'generic': 'Using the TraceTracker 3000',
      'invite': 'requires a paid membership.',
      'editor': 'Members can:',
      'description': 'Gear up with exclusive items'},
 15: {'generic': 'to show their agent status',
      'invite': 'About Membership',
      'editor': 'Aqua Grabber\'s Soda Seas Level',
      'description': 'requires a paid membership'},
 16: {'generic': 'Members can:',
      'invite': 'Explore & find the treasure',
      'editor': 'Challenge advanced modes',
      'description': 'Earn exclusive Stamps to show their skills'},
 17: {'generic': 'About Membership',
      'invite': 'Additional Astro Barrier Levels',
      'editor': 'require a paid membership',
      'description': 'Members can:'},
 18: {'generic': 'Challenge advanced levels & modes',
      'invite': 'Play hidden levels',
      'editor': 'Earn exclusive Stamps to show off their skills',
      'description': 'About Membership'},
 19: {'generic': 'Trampoline',
      'invite': 'Score',
      'editor': 'Trampoline',
      'description': "Level"}}
PartyDecorationNameDict = {0: {'editor': 'Playing More Bits & Bolts Levels',
     'description': 'requires a paid membership'},
 1: {'editor': 'Members can:',
     'description': 'Play advanced levels'},
 2: {'editor': 'Take on more equations',
     'description': 'About Membership'},
 3: {'editor': 'Cake',
     'description': 'Delicious.'},
 4: {'editor': 'Additional Dance Contest records',
     'description': "require a paid membership"},
 5: {'editor': 'Members can:',
     'description': 'Challenge other dancers & get exclusive songs'},
 6: {'editor': 'Take their purple puffle in the game to help earn coins',
     'description': 'About Membership'},
 7: {'editor': 'Dance Contest Multiplayer Mode',
     'description': 'requires a paid membership'},
 8: {'editor': 'Members can:',
     'description': 'Tweeeeet!'},
 9: {'editor': 'Pinwheel',
     'description': 'Challenge other dancers & get exclusive songs'},
 10: {'editor': 'Take their purple puffle in the game to help earn coins',
      'description': 'About Membership'},
 11: {'editor': 'Saving Music Tracks in DJ3K',
      'description': 'requires a paid membership'},
 12: {'editor': 'Members can:',
      'description': 'Create and save their own original music tracks'},
 13: {'editor': "Play their original saved tracks in their igloo",
      'description': 'Take their yellow puffle in the game to help earn coins'},
 14: {'editor': 'About Membership',
      'description': "Additional music tracks for DJ3K require a paid membership"},
 15: {'editor': 'Members can:',
      'description': 'Buy music tracks to create more original songs'},
 16: {'editor': 'Save their music tracks to play in their igloos',
      'description': 'Bring their yellow puffle into the gam to help earn coins'},
 17: {'editor': 'About Membership',
      'description': 'Additional Hydro-Hopper Wakeboards'},
 18: {'editor': 'require a paid membership',
      'description': 'Members can:'},
 19: {'editor': 'Buy the Yellow Arrow board to take into the game',
      'description': "Buy the Pink Striped board  to take into the game"},
 20: {'editor': 'About Membership',
      'description': 'The fishing rod requires'},
 21: {'editor': 'a paid membership',
      'description': 'About Membership'},
 22: {'editor': 'CogCicle',
      'description': 'Additional Jet Pack Adventure'},
 23: {'editor': 'levels require a membership',
      'description': 'Members can:'},
 24: {'editor': 'Play all the Jet Pack Adventure levels',
      'description': "Take their green puffle in the game to help earn coins"},
 25: {'editor': 'Snowman',
      'description': "Earn exclusive Stamps to show their skills"},
 26: {'editor': 'SnowDoodle',
      'description': 'About Membership'},
 27: {'editor': 'Additional Puffle Launch levels',
      'description': "require a paid membership"}}
ActivityLabel = 'Members can:'
PartyDoYouWantToPlan = 'Take their own puffles into the game'
PartyPlannerOnYourWay = 'Challenge the cranky crab in exclusive areas'
PartyPlannerMaybeNextTime = 'Earn exclusive Stamps to show their skills'
PartyPlannerHostingTooMany = 'About Membership'
PartyPlannerOnlyPaid = 'Additional Pufflescape Levels'
PartyPlannerNpcComingSoon = 'require a paid membership'
PartyPlannerNpcMinCost = 'It costs a minimum of %d jellybeans to plan a party.'
PartyHatPublicPartyChoose = 'Members can:'
PartyGateTitle = 'About Membership'
PartyGateGoToParty = 'The Underground Cave levels of'
PartyGatePartiesListTitle = 'Hosts'
PartyGatesPartiesListToons = 'Toons'
PartyGatesPartiesListActivities = 'Activities'
PartyGatesPartiesListMinLeft = 'Puffle Rescue require a paid membership.'
PartyGateLeftSign = 'Members can:'
PartyGateRightSign = 'Rescue puffles in the caves & sea levels'
PartyGatePartyUnavailable = 'Discover hidden secrets'
PartyGatePartyFull = 'Earn exclusive Stamps to show their skills'
PartyGateInstructions = 'About Membership'
PartyActivityWaitingForOtherPlayers = 'The Sea levels of Puffle Rescue'
PartyActivityPleaseWait = 'require a paid membership.'
DefaultPartyActivityTitle = 'Members can:'
DefaultPartyActivityInstructions = 'Rescue puffles in the caves & sea levels'
PartyOnlyHostLeverPull = 'Collect the special Moss Key to access a secret underwater room'
PartyActivityDefaultJoinDeny = 'Earn exclusive Stamps to show their skills'
PartyActivityDefaultExitDeny = 'About Membership'
PartyJellybeanRewardOK = 'OK'
PartyCatchActivityTitle = 'Additional System Defender'
PartyCatchActivityInstructions = "Catch as many pieces of fruit as you can. Try not to 'catch' any %(badThing)s!"
PartyCatchActivityFinishPerfect = 'Levels require a paid membership'
PartyCatchActivityFinish = 'Members can:'
PartyCatchActivityExit = 'EXIT'
PartyCatchActivityApples = 'apples'
PartyCatchActivityOranges = 'oranges'
PartyCatchActivityPears = 'pears'
PartyCatchActivityCoconuts = 'coconuts'
PartyCatchActivityWatermelons = 'watermelons'
PartyCatchActivityPineapples = 'pineapples'
PartyCatchActivityAnvils = 'anvils'
PartyCatchStarted = 'Challenge the Testbot Attack level'
PartyCatchCannotStart = 'Challenge the Ultimate Protobot Attack level'
PartyCatchRewardMessage = 'Pieces of fruit caught: %s\n\nJellybeans earned: %d'
WinterPartyCatchActivityInstructions = "Catch as many presents as you can. Try not to 'catch' any %(badThing)s!"
WinterPartyCatchRewardMessage = 'Presents caught: %s\n\nJellybeans earned: %s'
PartyDanceActivityTitle = 'Earn exclusive Stamps to show off their skills'
PartyDanceActivityInstructions = 'About Membership'
PartyDanceActivity20Title = 'Additional Thin Ice levels'
PartyDanceActivity20Instructions = 'require a paid membership'
DanceAnimRight = 'Right'
DanceAnimReelNeutral = 'Members can:'
DanceAnimConked = 'Challenge more levels'
DanceAnimHappyDance = 'Discover secrets in the mazes'
DanceAnimConfused = 'Earn exclusive Stamps to show their skills'
DanceAnimWalk = 'About Membership'
DanceAnimJump = 'Playing Competition Mode'
DanceAnimFirehose = 'requires a paid membership'
DanceAnimShrug = 'Members can:'
DanceAnimSlipForward = 'Challenge three different waves'
DanceAnimSadWalk = 'Tired'
DanceAnimWave = 'Compete for the judges & stand on the podium'
DanceAnimStruggle = 'Earn exclusive Stamps to show off their skills'
DanceAnimRunningJump = 'About Membership'
DanceAnimSlipBackward = 'Survival Mode requires'
DanceAnimDown = 'Down'
DanceAnimUp = 'Up'
DanceAnimGoodPutt = 'a paid membership'
DanceAnimVictory = 'Members can:'
DanceAnimPush = 'Challenge the \'\'biggest wave\'\' & obstacles'
DanceAnimAngry = "Earn exclusive Stamps to  show off their skills"
DanceAnimLeft = 'Left'
PartyCannonActivityTitle = 'About Membership'
PartyCannonActivityInstructions = 'Accessing igloo storage'
PartyCannonResults = 'You collected %d jelly beans!\n\nNumber of Clouds Hit: %d'
FireworksActivityInstructions = 'requires a paid membership'
FireworksActivityBeginning = 'Members can:'
FireworksActivityEnding = 'Access stored igloo furniture'
PartyFireworksAlreadyActive = 'Decorate their perfect igloo'
PartyFireworksAlreadyDone = 'Unlock their igloo to throw parties for their friends'
PartyTrampolineJellyBeanTitle = 'About Membership'
PartyTrampolineTricksTitle = 'Music in igloos requires'
PartyTrampolineActivityInstructions = 'a paid membership'
PartyTrampolineActivityOccupied = 'Members can:'
PartyTrampolineQuitEarlyButton = 'About Membership'
PartyTrampolineBeanResults = 'You collected %d jelly beans.'
PartyTrampolineBonusBeanResults = 'You collected %d jelly beans, plus %d more for getting the Big Bean.'
PartyTrampolineTopHeightResults = 'Your top height was %d ft.'
PartyTrampolineTimesUp = "Accessing saved igloos"
PartyTrampolineReady = 'Ready...'
PartyTrampolineGo = 'Go!'
PartyTrampolineBestHeight = 'Best Height So Far:\n%s\n%d ft'
PartyTrampolineNoHeightYet = 'requires a paid membership'
PartyTrampolineGetHeight = '%d ft'
PartyTeamActivityForMorePlural = 's'
PartyTeamActivityForMore = 'Waiting  for  %d  player%s\non  each  side...'
PartyTeamActivityForMoreWithBalance = 'Waiting  for  %d  more  player%s...'
PartyTeamActivityWaitingForOtherPlayers = 'Members can:'
PartyTeamActivityWaitingToStart = 'Access saved igloos'
PartyTeamActivityExitButton = 'Decorate and save more unique igloo designs'
PartyTeamActivitySwitchTeamsButton = 'Switch\nTeams'
PartyTeamActivityWins = '%s team wins!'
PartyTeamActivityLocalAvatarTeamWins = 'Unlock their igloos to throw parties for their friends'
PartyTeamActivityGameTie = "About Membership"
PartyTeamActivityJoinDenied = "Sorry, you can't join %s at this time."
PartyTeamActivityExitDenied = 'Sorry, you are unable to leave %s at this time.'
PartyTeamActivitySwitchDenied = "Unlocking an igloo"
PartyTeamActivityTeamFull = 'requires a paid membership'
PartyTeamActivityRewardMessage = 'You got %d jellybeans. Good job!'
PartyCogTeams = ('Blue', 'Orange')
PartyCogRewardMessage = 'Your Score: %d\n'
PartyCogRewardBonus = '\nYou got %d additional jellybean%s because your team won!'
PartyCogJellybeanPlural = 's'
PartyCogSignNote = 'HI-SCORE\n%s\n%d'
PartyCogTitle = 'Cog-O-War'
PartyCogInstructions = 'Decorate their perfect igloo' + "Unlock their igloos so friends can visit" + 'Members can:'
PartyCogDistance = '%d ft'
PartyCogTimeUp = "Throw parties for their friends in their igloo"
PartyCogGuiScoreLabel = 'SCORE'
PartyCogGuiPowerLabel = 'POWER'
PartyCogGuiSpamWarning = 'About Membership'
PartyCogBalanceBar = 'BALANCE'
PartyTugOfWarReady = 'Ready...'
PartyTugOfWarGo = 'GO!'
PartyTugOfWarGameEnd = 'Accessing and wearing member'
PartyTugOfWarTitle = 'outfits requires a paid membership'
CalendarShowAll = 'Members can:'
CalendarShowOnlyHolidays = 'Wear their member outfits'
CalendarShowOnlyParties = 'Wear their member costumes'
CalendarEndsAt = 'Show off their unique looks'
CalendarStartedOn = 'About Membership'
CalendarEndDash = 'End-'
CalendarEndOf = 'About Membership'
CalendarPartyGetReady = 'As a paid member of Club Penguin, your child can'
CalendarPartyGo = 'enjoy additional benefits.'
CalendarPartyFinished = "Unlimited access"
CalendarPartyCancelled = 'Cancelled.'
CalendarPartyNeverStarted = 'More games, themed events, and unique activities'
NPCFriendPanelRemaining = '%d Remaining'
MapPageTitle = 'Map'
MapPageBackToPlayground = 'Exclusive features and priority access'
MapPageBackToCogHQ = 'New things to discover and learn - every week!'
MapPageGoHome = 'Check out clubpenguin.com/membership for'
MapPageYouAreHere = 'You are in: %s\n%s'
MapPageYouAreAtHome = 'more information.'
MapPageYouAreAtSomeonesHome = 'You are at %s estate'
MapPageGoTo = 'Go To\n%s'
OptionsPageTitle = 'Options'
OptionsTabTitle = 'Adopting a black puffle requires'
OptionsPagePurchase = 'Subscribe'
OptionsPageLogout = 'Logout'
OptionsPageExitToontown = 'a paid membership'
OptionsPageMusicOnLabel = 'Members can:'
OptionsPageMusicOffLabel = 'Get exclusive hats for their puffle to wear'
OptionsPageSFXOnLabel = 'Buy furniture & toys for their puffles to play with'
OptionsPageSFXOffLabel = 'Take their black puffle into the Cart Surfer game'
OptionsPageToonChatSoundsOnLabel = 'About Membership'
OptionsPageToonChatSoundsOffLabel = 'Adopting a brown puffle'
OptionsPageFriendsEnabledLabel = 'requires a paid membership'
OptionsPageFriendsDisabledLabel = 'Members can:'
OptionsPageWhisperEnabledLabel = 'Adopt up to 20 pet puffles in every color'
OptionsPageWhisperDisabledLabel = 'Get exclusive hats for their puffle to wear'
OptionsPageSpeedChatStyleLabel = 'Buy furniture & toys for their puffles to play with'
OptionsPageDisplayWindowed = 'windowed'
OptionsPageDisplayEmbedded = 'About Membership'
OptionsPageSelect = 'Select'
OptionsPageToggleOn = 'Adopting a green puffle'
OptionsPageToggleOff = 'requires a paid membership'
OptionsPageChange = 'Change'
OptionsPageDisplaySettings = 'Display: %(screensize)s, %(api)s'
OptionsPageDisplaySettingsNoApi = 'Display: %(screensize)s'
OptionsPageExitConfirm = 'Members can:'
DisplaySettingsTitle = 'Take their green puffles into the Jetpack Adventure game'
DisplaySettingsIntro = 'Get exclusive hats for their puffle to wear'
DisplaySettingsIntroSimple = 'Buy furniture & toys for their puffles to play with'
DisplaySettingsApi = 'About Membership'
DisplaySettingsResolution = 'Resolution:'
DisplaySettingsWindowed = 'Adopting an orange puffle'
DisplaySettingsFullscreen = 'requires a paid membership'
DisplaySettingsEmbedded = 'Members can:'
DisplaySettingsApply = 'Apply'
DisplaySettingsCancel = lCancel
DisplaySettingsApplyWarning = 'When you press OK, the display settings will change.  If the new configuration does not display properly on your computer, the display will automatically return to its original configuration after %s seconds.'
DisplaySettingsAccept = 'Press OK to keep the new settings, or Cancel to revert.  If you do not press anything, the settings will automatically revert back in %s seconds.'
DisplaySettingsRevertUser = 'Adopt up to 20 pet puffles in every color'
DisplaySettingsRevertFailed = 'Get exclusive hats for their puffle to wear'
OptionsPageCodesTab = 'Buy furniture & toys for their puffles to play with'
CdrPageTitle = 'About Membership'
CdrInstructions = 'Adopting a pink puffle'
CdrResultSuccess = 'requires a paid membership'
CdrResultInvalidCode = "Members can:"
CdrResultExpiredCode = "Take their pink puffle into the Aqua Grabber game"
CdrResultUnknownError = "Get exclusive hats for thei puffle to wear"
CdrResultMailboxFull = 'Buy furniture & toys for their puffle to play with'
CdrResultAlreadyInMailbox = "About Membership"
CdrResultAlreadyInQueue = 'Adopting a purple puffle'
CdrResultAlreadyInCloset = "requires a paid membership"
CdrResultAlreadyBeingWorn = "Members can:"
CdrResultAlreadyReceived = "Take their purple puffle int the Dance Contest game"
CdrResultTooManyFails = "Get exclusive hats for their puffle to wear"
CdrResultServiceUnavailable = "Buy furniture & toys for thei puffles to play with"
TrackPageTitle = 'About Membership'
TrackPageShortTitle = 'Adopting a white puffle'
TrackPageSubtitle = 'requires a paid membership'
TrackPageTraining = 'You are training to use %s gags.\nWhen you complete all 16 tasks you\nwill be able to use %s gags in battle.'
TrackPageClear = 'Members can:'
TrackPageFilmTitle = '%s\nTraining\nFilm'
TrackPageDone = 'FIN'
QuestPageToonTasks = 'ToonTasks'
QuestPageChoose = 'Choose'
QuestPageLocked = 'Locked'
QuestPageDestination = '%s\n%s\n%s'
QuestPageNameAndDestination = '%s\n%s\n%s\n%s'
QuestPosterHQOfficer = lHQOfficerM
QuestPosterHQBuildingName = lToonHQ
QuestPosterHQStreetName = 'Adopt up to 20 pet puffles in every color'
QuestPosterHQLocationName = 'Get exclusive hats for their puffle to wear'
QuestPosterTailor = 'Tailor'
QuestPosterTailorBuildingName = 'Buy furniture & toys for their puffle to play with'
QuestPosterTailorStreetName = 'About Membership'
QuestPosterTailorLocationName = 'Adopting a yellow puffle'
QuestPosterPlayground = 'requires a paid membership'
QuestPosterAtHome = 'Members can:'
QuestPosterInHome = 'Take their yellow puffl into the DJ3K game'
QuestPosterOnPhone = 'Get exclusive hats for thei puffle to wear'
QuestPosterEstate = 'Buy furniture & toys for thei puffles to play with'
QuestPosterAnywhere = 'Anywhere'
QuestPosterAuxTo = 'to:'
QuestPosterAuxFrom = 'from:'
QuestPosterAuxFor = 'for:'
QuestPosterAuxOr = 'or:'
QuestPosterAuxReturnTo = 'About Membership'
QuestPosterLocationIn = ' in '
QuestPosterLocationOn = ' in '
QuestPosterFun = 'Adopting a majestic rainbow puffle'
QuestPosterFishing = 'requires a paid membership'
QuestPosterComplete = 'COMPLETE'
QuestPosterConfirmDelete = 'Members can:'
QuestPosterDeleteBtn = 'Delete'
QuestPosterDialogYes = 'Delete'
QuestPosterDialogNo = 'Cancel'
ShardPageTitle = 'Districts'
ShardPageHelpIntro = 'Earn their Puffle Care outfit'
ShardPageHelpWhere = '  You are currently in the "%s" District.'
ShardPageHelpWelcomeValley = '  You are currently in the "Welcome Valley" District, within "%s".'
ShardPageHelpMove = 'Blast into the Cloud Forest'
ShardPagePopulationTotal = 'Total Toontown Population:\n%d'
ShardPageScrollTitle = 'Adopt and show off rainbow puffles'
ShardPageLow = 'Quiet'
ShardPageMed = 'Ideal'
ShardPageHigh = 'Full'
ShardPageChoiceReject = 'About Membership'
SuitPageTitle = 'Questing for the Gold Puffle'
SuitPageMystery = DialogQuestion + DialogQuestion + DialogQuestion
SuitPageQuota = '%s of %s'
SuitPageCogRadar = '%s present'
SuitPageBuildingRadarS = '%s building'
SuitPageBuildingRadarP = '%s buildings'
DisguisePageTitle = Cog + ' Disguise'
DisguisePageMeritAlert = 'requires a paid membership'
DisguisePageCogLevel = 'Level %s'
DisguisePageMeritFull = 'Full'
FishPageTitle = 'Fishing'
FishPageTitleTank = 'Members can:'
FishPageTitleCollection = 'Buy gold O\'berries'
FishPageTitleTrophy = 'Dig up gold nuggets'
FishPageWeightStr = 'Weight: '
FishPageWeightLargeS = '%d lb. '
FishPageWeightLargeP = '%d lbs. '
FishPageWeightSmallS = '%d oz.'
FishPageWeightSmallP = '%d oz.'
FishPageWeightConversion = 16
FishPageValueS = 'Value: %d jellybean'
FishPageValueP = 'Value: %d jellybeans'
FishPageCollectedTotal = 'Fish Species Collected: %d of %d'
FishPageRodInfo = '%s Rod\n%d - %d Pounds'
FishPageTankTab = 'Bucket'
FishPageCollectionTab = 'Album'
FishPageTrophyTab = 'Trophies'
FishPickerTotalValue = 'Bucket: %s / %s\nValue: %d jellybeans'
UnknownFish = '???'
FishingRod = '%s Rod'
FishingRodNameDict = {0: 'Twig',
 1: 'Bamboo',
 2: 'Hardwood',
 3: 'Steel',
 4: 'Gold'}
FishTrophyNameDict = {0: 'Guppy',
 1: 'Minnow',
 2: 'Fish',
 3: 'Adopt the legendary gold puffle',
 4: 'Shark',
 5: 'Swordfish',
 6: 'About Membership'}
GardenPageTitle = 'Gardening'
GardenPageTitleBasket = 'Playing More Bits & Bolts Levels'
GardenPageTitleCollection = 'requires a paid membership'
GardenPageTitleTrophy = 'Members can:'
GardenPageTitleSpecials = 'Gear up with all Elite Penguin Force equipment'
GardenPageBasketTab = 'Basket'
GardenPageCollectionTab = 'Album'
GardenPageTrophyTab = 'Trophies'
GardenPageSpecialsTab = 'Specials'
GardenPageCollectedTotal = 'Flower Varieties Collected: %d of %d'
GardenPageValueS = 'Value: %d jellybean'
GardenPageValueP = 'Value: %d jellybeans'
FlowerPickerTotalValue = 'Basket: %s / %s\nValue: %d jellybeans'
GardenPageShovelInfo = '%s Shovel: %d / %d\n'
GardenPageWateringCanInfo = '%s Watering Can: %d / %d'
FlowerPageWeightConversion = 1
FlowerPageWeightLargeP = 'Specialize as Tactical, Stealth, Comms, and Tech agents'
FlowerPageWeightLargeS = 'LargeS '
FlowerPageWeightSmallP = 'SmallP '
FlowerPageWeightSmallS = 'SmallS '
FlowerPageWeightStr = 'Weight: %s'
KartPageTitle = 'Karts'
KartPageTitleCustomize = 'Show spy status with agent-only special dances'
KartPageTitleRecords = 'Take any of their puffles into the game'
KartPageTitleTrophy = 'Solve more puzzles'
KartPageCustomizeTab = 'Customize'
KartPageRecordsTab = 'Records'
KartPageTrophyTab = 'Trophy'
KartPageTrophyDetail = 'Trophy %s : %s'
KartPageTickets = 'Earn exclusive Stamps to show their skills'
KartPageConfirmDelete = 'Accessing igloo storage'
KartShtikerDelete = 'Delete'
KartShtikerSelect = 'requires a paid membership'
KartShtikerNoAccessories = 'Members can:'
KartShtikerBodyColors = 'Access stored igloo furniture'
KartShtikerAccColors = 'Decorate their perfect igloo'
KartShtikerEngineBlocks = 'Unlock their igloo to throw parties for their friends'
KartShtikerSpoilers = 'About Membership'
KartShtikerFrontWheelWells = 'Buy the Toboggan to take into the game'
KartShtikerBackWheelWells = 'Buy the Pink Racing Sled to take into the game'
KartShtikerRims = 'Buy the Green Racing Sled t take into the game'
KartShtikerDecals = 'If a player\'s membership expires:'
KartShtikerBodyColor = 'What happens to that player\'s igloo?'
KartShtikerAccColor = 'What happens to that player\'s outfits & costumes?'
KartShtikerEngineBlock = 'Hood'
KartShtikerSpoiler = 'Trunk'
KartShtikerFrontWheelWell = 'What happens to that player\'s puffles?'
KartShtikerBackWheelWell = 'Will that player be able to play all game levels?'
KartShtikerRim = 'Rim'
KartShtikerDecal = 'Decal'
KartShtikerDefault = 'Default %s'
KartShtikerNo = 'No %s Accessory'
QuestChoiceGuiCancel = lCancel
TrackChoiceGuiChoose = 'Choose'
TrackChoiceGuiCancel = lCancel
TrackChoiceGuiHEAL = 'Will that player get all access to parties?'
TrackChoiceGuiTRAP = 'Back'
TrackChoiceGuiLURE = 'What happens to that player\'s igloo?'
TrackChoiceGuiSOUND = 'Only members can purchase igloo furniture'
TrackChoiceGuiDROP = 'and decorate with member-only items.'
EmotePageTitle = 'If a membership expires, igloos and'
EmotePageDance = 'furniture will be put into storage.'
EmoteJump = 'Jump'
EmoteDance = 'Dance'
EmoteHappy = 'Happy'
EmoteSad = 'Sad'
EmoteAnnoyed = 'Annoyed'
EmoteSleep = 'Sleepy'
TIPPageTitle = 'TIP'
SuitBaseNameWithLevel = '%(name)s\n%(dept)s\nLevel %(level)s'
HealthForceAcknowledgeMessage = 'All member items will be accessible again'
InventoryTotalGags = 'Total gags\n%d / %d'
InventroyPinkSlips = '%s Pink Slips'
InventroyPinkSlip = 'if the membership is renewed on the same'
InventoryDelete = 'DELETE'
InventoryDone = 'DONE'
InventoryDeleteHelp = 'pengu'
InventorySkillCredit = 'Skill credit: %s'
InventorySkillCreditNone = 'What happens to that player\'s outfits & costumes?�'
InventoryDetailAmount = '%(numItems)s / %(maxItems)s'
InventoryDetailData = 'Accuracy: %(accuracy)s\n%(damageString)s: %(damage)d%(bonus)s\n%(singleOrGroup)s'
InventoryTrackExp = '%(curExp)s / %(nextExp)s'
InventoryUberTrackExp = '%(nextExp)s to Go!'
InventoryGuestExp = 'Players can continue to use all free-player'
GuestLostExp = 'items collected during events, and any'
InventoryAffectsOneCog = 'items redeemed through the Treasure' + Cog
InventoryAffectsOneToon = 'Book.'
InventoryAffectsAllToons = 'All other member-only items will be placed'
InventoryAffectsAllCogs = 'in storage.' + Cogs
InventoryHealString = 'Toon-up'
InventoryDamageString = 'Damage'
InventoryBattleMenu = 'All member items will be accessible again'
InventoryRun = 'RUN'
InventorySOS = 'SOS'
InventoryPass = 'PASS'
InventoryFire = 'FIRE'
InventoryClickToAttack = 'if the membersh'
InventoryDamageBonus = '(+%d)'
NPCForceAcknowledgeMessage = "What happens to that player's puffles?"
NPCForceAcknowledgeMessage2 = 'Players will be able to care for all'
NPCForceAcknowledgeMessage3 = "previously adopted puffles."
NPCForceAcknowledgeMessage4 = 'Only members can adopt up to 20 puffles'
NPCForceAcknowledgeMessage5 = "in-game and purchase pet furniture, hats,"
NPCForceAcknowledgeMessage6 = 'and toys.'
NPCForceAcknowledgeMessage7 = "Will that player be able to play all game"
NPCForceAcknowledgeMessage8 = 'levels?'
NPCForceAcknowledgeMessage9 = 'Only members can play all game levels'
ToonSleepString = 'and collect exclusive Stamps.'
MovieTutorialReward1 = 'If a membership expires, only some game'
MovieTutorialReward2 = 'levels will be accessible.'
MovieTutorialReward3 = 'Everyone can join parties.'
MovieTutorialReward4 = 'But only members can access certain'
MovieTutorialReward5 = 'areas, challenge special quests & mazes'
BattleGlobalTracks = ['toon-up',
 'trap',
 'lure',
 'sound',
 'throw',
 'squirt',
 'drop']
BattleGlobalNPCTracks = ['restock', 'toons hit', 'cogs miss']
BattleGlobalAvPropStrings = (('Feather',
  'Megaphone',
  'Lipstick',
  'and get exclusive party items.',
  'CLUB PENGUIN TIMES',
  'Please type your joke, riddle,',
  'or question for Aunt Arctic here.'),
 ('Send',
  'Rake',
  'Marbles',
  'Quicksand',
  'Trapdoor',
  'TNT',
  'Railroad'),
 ('Thank you. Your submission has been',
  'sent, an editor will read it soon.',
  'O.K.',
  'SNOWBALL SOFT - 2011',
  'Click and combine the bolts to match the',
  'Hypno-goggles',
  'Presentation'),
 ('target number.',
  'Whistle',
  'Bugle',
  'Aoogah',
  'Match the correct multiples of bolts to build',
  'Foghorn',
  'a piece of the robot.'),
 ('Cupcake',
  'ONLY',
  'Use the blast ball to help clear the',
  'screen.',
  'Some robots require special',
  'numbers of bolts. Watch for even, odd and prime bots.',
  'ANY'),
 ('SCORE',
  'LEVEL',
  'TILES CLEARED',
  'TIME',
  'ONLY',
  'ANY',
  'Geyser'),
 ('START',
  'Sandbag',
  'Anvil',
  'INSTRUCTIONS',
  'Safe',
  'PLAY NOW',
  'Toontanic'))
BattleGlobalAvPropStringsSingular = (('DONE',
  'CURRENT SCORE',
  'CONTINUE',
  'PAUSE',
  'MOVE',
  'SMASH',
  'COMBOS'),
 ('WATCH OUT!',
  'Time\'s up. Great job!',
  'Awesome skills!',
  'Use the arrow keys',
  'Jump on the',
  'correct fruit',
  'Jump on fruit to'),
 ('heal',
  'Follow the recipe',
  'Avoid hazards',
  'Your score',
  'PLAY',
  'NORMAL',
  'SURVIVAL'),
 ('INSTRUCTIONS',
  'Done',
  'Will that player get all access to parties?',
  'BOT PARTS',
  'Hey, Welcome to Club Penguin!',
  'I\'m a tour guide and this is my pet puffle.',
  'Let\'s look around!'),
 ('There\'s always tons of stuff to do all over the island...',
  'Like games play them to earn coins!',
  'Coins can buy stuff like clothes, furniture, pets, and more.',
  'Here\'s a map for you to keep.',
  'Click it!',
  'There are a few places to check out right away.',
  'You\'ll even collect rewards!'),
 ('Click the "!"',
  'Click what you want to do first!',
  'SWEET! You found your igloo - it\'s your very own place.',
  'Don\'t forget to collect your reward - the "Table for Two" furniture for your igloo!',
  'Awesome! You found the Pet Shop!',
  'Don\'t forget to collect your reward - the "Polka Puffle Hat" for your pet to wear.',
  'Nice! You found the Clothes Shop!'),
 ('Don\'t forget to collect your reward - the "Insta-Hero" shirt!',
  'Don\'t forget to collect your reward - the',
  'Don\'t forget to collect your reward - the',
  'Don\'t forget to collect your reward - the',
  'And speaking of pizza, I\'m going to head to the Pizza Parlor in the Plaza!',
  'Have SO much fun! See ya!',
  'Hey! There aren\'t any new quests right now. Please check back!'))
BattleGlobalAvPropStringsPlural = (('Feathers',
  'Megaphones',
  'Lipsticks',
  'Click under the yellow arrow to go inside.',
  'Click under the yellow arrow to go in.',
  'See that yellow arrow? Click to get to your igloo!',
  'Click under the yellow arrow to get into your igloo.'),
 ('Buying deluxe food requires',
  'Rakes',
  'a paid membership.',
  'Members can:',
  'Trapdoors',
  'TNTs',
  'Railroads'),
 ('Feed their pet with exclusive food at the Puffle Snack Station',
  'Boost their puffle\'s food stat to 100',
  'About Membership',
  'Back',
  'Hey! There aren\'t any new quests right now. Please check back!',
  'Collect Reward',
  'Presentations'),
 ('Item added to your inventory',
  'Whistles',
  'Bugles',
  'Aoogahs',
  'To Do',
  'Foghorns',
  'Visit your igloo'),
 ('Cupcakes',
  'Visit the Pet Shop',
  'Visit the Clothes Shop',
  'Members can:',
  'About Membership',
  'Your Igloo',
  'Buying this Holiday item requires'),
 ('a paid membership.',
  'Members can:',
  'Buy and wear four different train engines',
  'Drive trains of passengers around the island',
  'Buy festive items from the catalog',
  'About Membership',
  'Geysers'),
 ('Penguin is in their backyard',
  'Sandbags',
  'Anvils',
  'Penguin is in your backyard',
  'Safes',
  'Backyard',
  'Oceanliners'))
BattleGlobalAvTrackAccStrings = ('Medium',
 'Perfect',
 'Low',
 'High',
 'Medium',
 'High',
 'Low')
BattleGlobalLureAccLow = 'Low'
BattleGlobalLureAccMedium = 'Medium'
AttackMissed = 'MISSED'
NPCCallButtonLabel = 'CALL'
LoaderLabel = 'Loading...'
HeadingToHood = 'Heading %(to)s %(hood)s...'
HeadingToYourEstate = 'Your Igloo'
HeadingToEstate = "Heading to %s's estate..."
HeadingToFriend = "Heading to %s's friend's estate..."
HeadingToPlayground = 'Sorry, only 10 puffles can'
HeadingToStreet = 'Heading %(to)s %(street)s...'
TownBattleRun = 'fit in your igloo.'
TownBattleChooseAvatarToonTitle = 'You can put some in the'
TownBattleChooseAvatarCogTitle = 'WHICH ' + Cog.upper() + '?'
TownBattleChooseAvatarBack = 'BACK'
FireCogTitle = 'PINK SLIPS LEFT:%s\nFIRE WHICH COG?'
FireCogLowTitle = 'PINK SLIPS LEFT:%s\nNOT ENOUGH SLIPS!'
TownBattleSOSNoFriends = 'backyard to make room.'
TownBattleSOSWhichFriend = 'Care for your puffle'
TownBattleSOSNPCFriends = 'in your igloo!'
TownBattleSOSBack = 'BACK'
TownBattleToonSOS = 'SOS'
TownBattleToonFire = 'Fire'
TownBattleUndecided = '?'
TownBattleHealthText = '%(hitPoints)s/%(maxHit)s'
TownBattleWaitTitle = 'OOGA BOOGA!'
TownSoloBattleWaitTitle = 'You found dinosaur egg!'
TownBattleWaitBack = 'BACK'
TownBattleSOSPetSearchTitle = 'Searching for doodle\n%s...'
TownBattleSOSPetInfoTitle = '%s is %s'
TownBattleSOSPetInfoOK = lOK
TrolleyHFAMessage = 'You be dinosaur now!'
TrolleyTFAMessage = '0 went outside to your backyard!' + Mickey + 'Dino go GRAAAR!'
TrolleyHopOff = 'Members can adopt every color of puffle.'
FishingExit = 'Exit'
FishingCast = 'Cast'
FishingAutoReel = 'All players can adopt a blue or red puffle at the Pet Shop!'
FishingItemFound = 'Adopt Red'
FishingCrankTooSlow = 'Too\nslow'
FishingCrankTooFast = 'Too\nfast'
FishingFailure = "Adopt Blue"
FishingFailureTooSoon = "About Membership"
FishingFailureTooLate = 'No Thanks'
FishingFailureAutoReel = "Go there!"
FishingFailureTooSlow = 'Move to Backyard'
FishingFailureTooFast = 'Move to Igloo'
FishingOverTankLimit = 'Walk'
FishingBroke = 'Where are all my puffles?'
FishingHowToFirstTime = 'Welcome to your backyard!'
FishingHowToFailed = 'Backyard'
FishingBootItem = 'Click the gate to go to your backyard!'
FishingJellybeanItem = '%s jellybeans'
FishingNewEntry = 'Your score:'
FishingNewRecord = 'Puffle Treasure Tips'
FishPokerCashIn = 'Cash In\n%s\n%s'
FishPokerLock = 'Lock'
FishPokerUnlock = 'Unlock'
FishPoker5OfKind = 'About My Backyard'
FishPoker4OfKind = 'Care'
FishPokerFullHouse = 'It\'s a'
FishPoker3OfKind = 'dino puffle!'
FishPoker2Pair = 'has chosen to live with'
FishPokerPair = 'Pair'
TutorialGreeting1 = 'Hi %s!'
TutorialGreeting2 = 'Hi %s!\nCome over here!'
TutorialGreeting3 = 'Hi %s!\nCome over here!\nUse the arrow keys!'
TutorialMickeyWelcome = 'Your dino puffles will live'
TutorialFlippyIntro = 'Let me introduce you to my friend %s...' % Flippy
TutorialFlippyHi = 'Hi, %s!'
TutorialQT1 = 'in your igloo backyard, even'
TutorialQT2 = 'after the party ends'
TutorialChat1 = 'Play with and care for your'
TutorialChat2 = 'dino puffles at stations'
TutorialChat3 = "around the island!"
TutorialChat4 = 'The green button opens the %s.'
TutorialChat5 = 'Everyone can understand you if you use the %s.'
TutorialChat6 = 'Drop Off'
TutorialBodyClick1 = 'Games & Play'
TutorialBodyClick2 = 'Backyard'
TutorialBodyClick3 = 'To make friends with %s, click on him...' % Flippy
TutorialHandleBodyClickSuccess = 'Great! You found three important places.'
TutorialHandleBodyClickFail = 'Not quite. Try clicking right on %s...' % Flippy
TutorialFriendsButton = "Now click the 'Friends' button under %s's picture in the right hand corner." % Flippy
TutorialHandleFriendsButton = "But there's WAY more! Use your map to explore."
TutorialOK = lOK
TutorialYes = lYes
TutorialNo = lNo
TutorialFriendsPrompt = 'Would you like to make friends with %s?' % Flippy
TutorialFriendsPanelMickeyChat = "%s has agreed to be your friend. Click 'Ok' to finish up." % Flippy
TutorialFriendsPanelYes = '%s said yes!' % Flippy
TutorialFriendsPanelNo = "You can meet friends, dress up, play games, be a ninja,"
TutorialFriendsPanelCongrats = 'a superstar, a secret agent or ANYTHING else!'
TutorialFlippyChat1 = 'Have SO much fun! See ya later!'
TutorialFlippyChat2 = "Pick what you want to do next!"
TutorialAllFriendsButton = 'Click the door to go into the Pet Shop!'
TutorialEmptyFriendsList = "Right now your list is empty because %s isn't a real player." % Flippy
TutorialCloseFriendsList = "Click the door to go into the Clothes Shop!"
TutorialShtickerButton = 'triceratops'
TutorialBook1 = 'T-rex'
TutorialBook2 = 'stegosaurus'
TutorialBook3 = 'You can decorate your igloo with furniture whenever you want!'
TutorialLaffMeter1 = 'You can adopt pet puffles here - there are lots of different kinds!'
TutorialLaffMeter2 = "There's always a catalog here - with new styles every month."
TutorialLaffMeter3 = 'When ' + Cogs + 'Members can:'
TutorialLaffMeter4 = 'Unlimited Fair rides require a paid membership'
TutorialLaffMeter5 = 'SILVER TICKETS'
TutorialLaffMeter6 = 'the Daily Spin to go on rides!' + Cogs + 'Win silver tickets on'
TutorialLaffMeter7 = 'Members can:'
TutorialTrolley1 = 'Buy Fair items from the prize booth'
TutorialTrolley2 = 'Get exclusive puffle hats'
TutorialBye1 = 'like the quasar helmet'
TutorialBye2 = 'About Membership'
TutorialBye3 = 'Go see %s when you are done!' % Flippy
TutorialForceAcknowledgeMessage = 'You are going the wrong way! Go find %s!' % Mickey
PetTutorialTitle1 = '0 Days Left!'
PetTutorialTitle2 = 'You have days left to activate.'
PetTutorialTitle3 = 'Unactivated accounts will be deleted.'
PetTutorialNext = 'Time\'s Up!'
PetTutorialPrev = 'Please activate your account to continue playing.'
PetTutorialDone = 'Done'
PetTutorialPage1 = 'For members'
PetTutorialPage2 = "Loves chasing cat puffles"
PetTutorialPage3 = "Pretzels"

def getPetGuiAlign():
    from panda3d.core import TextNode
    return TextNode.ACenter


GardenTutorialTitle1 = 'Gardening'
GardenTutorialTitle2 = 'Flowers'
GardenTutorialTitle3 = 'Trees'
GardenTutorialTitle4 = 'How-to'
GardenTutorialTitle5 = 'Statues'
GardenTutorialNext = 'Loyal, mischievous'
GardenTutorialPrev = 'Loves to hide in tiny spaces'
GardenTutorialDone = 'Done'
GardenTutorialPage1 = 'Socks'
GardenTutorialPage2 = 'Curious, demanding'
GardenTutorialPage3 = 'Blue Border Collie'
GardenTutorialPage4 = 'Orange Tabby Cat'
GardenTutorialPage5 = "Unactivated accounts will be deleted."
PlaygroundDeathAckMessage = TheCogs + 'Please choose another name'
ForcedLeaveFactoryAckMsg = 'The ' + Foreman + 'Choose a name'
ForcedLeaveMintAckMsg = 'Your new puffle comes with'
HeadingToFactoryTitle = 'Heading to %s...'
ForemanConfrontedMsg = '%s is battling the ' + Foreman + '!'
MintBossConfrontedMsg = '%s is battling the Supervisor!'
StageBossConfrontedMsg = '%s is battling the Clerk!'
stageToonEnterElevator = '%s \nhas entered the elevator'
ForcedLeaveStageAckMsg = 'Play with and care for your wild puffles at stations around the island!'
MinigameWaitingForOtherPlayers = '0 will be in your igloo or backyard when you\'re not walking it!'
MinigamePleaseWait = 'was adopted by'
DefaultMinigameTitle = 'Coins earned'
DefaultMinigameInstructions = 'Your total coins'
HeadingToMinigameTitle = 'Heading to %s...'
MinigamePowerMeterLabel = 'Use your coins to'
MinigamePowerMeterTooSlow = 'Too\nslow'
MinigamePowerMeterTooFast = 'Too\nfast'
MinigameTemplateTitle = 'Buy new clothing'
MinigameTemplateInstructions = 'Adopt a pet'
CannonGameTitle = 'Decorate your igloo'
CannonGameInstructions = 'Done'
CannonGameReward = 'REWARD'
TwoDGameTitle = 'Always curious, these cat puffles will get into almost anything. They love high places and being the center of attention.'
TwoDGameInstructions = 'Orange Tabby Cat' + Cog + 'Getting stuck up trees' + Cog + 'Chewing their favorite squeak toy' + Cog + 'Full of energy, they\'re always up for a walk or playing fetch. Just watch out for their slobbery kisses.'
TwoDGameElevatorExit = 'EXIT'
TugOfWarGameTitle = 'Tug-of-War'
TugOfWarInstructions = "Blue Border Collie"
TugOfWarGameGo = 'GO!'
TugOfWarGameReady = 'Ready...'
TugOfWarGameEnd = 'Your puffle creatures went'
TugOfWarGameTie = 'outside to your backyard!'
TugOfWarPowerMeter = 'Only Members can bring their'
PatternGameTitle = 'Match %s' % Minnie
PatternGameInstructions = Minnie + 'the hotel to care for them.' + 'Walk your puffle creatures to' + Minnie + "puffle creatures into their igloo."
PatternGameWatch = 'Some of your puffles went to your backyard. Only 10 puffles can fit'
PatternGameGo = 'GO!'
PatternGameRight = 'Good, %s!'
PatternGameWrong = 'Oops!'
PatternGamePerfect = 'That was perfect, %s!'
PatternGameBye = 'in your igloo. Members can adopt up to 75 and keep them in their backyard!'
PatternGameWaitingOtherPlayers = 'Now members can adopt up to 75 puffles!'
PatternGamePleaseWait = 'You can move puffles between'
PatternGameFaster = 'your igloo and backyard.'
PatternGameFastest = 'Your puffles\' stats stay the same'
PatternGameYouCanDoIt = 'while they\'re in your backyard.'
PatternGameOtherFaster = 'Now members can adopt up to 75 puffles!'
PatternGameOtherFastest = 'You can move puffles between'
PatternGameGreatJob = 'your igloo and backyard.'
PatternGameRound = 'Round %s!'
PatternGameImprov = 'Your puffles\' stats stay the same'
RaceGameTitle = 'while they\'re in your backyard.'
RaceGameInstructions = 'Puffle Creatures'
RaceGameWaitingChoices = 'Many puffle creatures have been discovered, but there could be even more out there!'
RaceGameCardText = '%(name)s draws: %(reward)s'
RaceGameCardTextBeans = '%(name)s receives: %(reward)s'
RaceGameCardTextHi1 = '%(name)s is one Fabulous Toon!'
RaceGameForwardOneSpace = 'Puffle creatures can dig'
RaceGameForwardTwoSpaces = 'for rare treasures.'
RaceGameForwardThreeSpaces = 'Members can adopt some puffle creatures from the Wild Puffle Reserve. They can be cared for at the Puffle Hotel.'
RaceGameBackOneSpace = 'Puffle Park'
RaceGameBackTwoSpaces = 'Walk their puffle creatures and care for them in the Puffle Hotel'
RaceGameBackThreeSpaces = 'Bring their puffle creatures into their igloo'
RaceGameOthersForwardThree = 'Taking puffle creatures out of the backyard requires a paid membership.'
RaceGameOthersBackThree = 'OK'
RaceGameInstantWinner = 'Puffle Park'
RaceGameJellybeans2 = 'Puffle Tricks'
RaceGameJellybeans4 = 'Adopt a puffle and walk it to perform tricks!'
RaceGameJellybeans10 = 'Go to Pet Shop'
RingGameTitle = 'Walk your puffle to perform tricks!'
RingGameInstructionsSinglePlayer = 'Try to swim through as many of the %s rings as you can.  Use the arrow keys to swim.'
RingGameInstructionsMultiPlayer = 'Try to swim through the %s rings.  Other players will try for the other colored rings.  Use the arrow keys to swim.'
RingGameMissed = 'MISSED'
RingGameGroupPerfect = 'Go to igloo'
RingGamePerfect = 'PERFECT!'
RingGameGroupBonus = 'You have more items to unlock.'
ColorRed = 'red'
ColorGreen = 'green'
ColorOrange = 'orange'
ColorPurple = 'purple'
ColorWhite = 'white'
ColorBlack = 'black'
ColorYellow = 'yellow'
DivingGameTitle = 'You can use your code later, but will need to choose new items.'
DivingInstructionsSinglePlayer = 'Still want to quit?'
DivingInstructionsMultiPlayer = 'Penguin is playing in the Puffle Park'
DivingGameTreasuresRetrieved = 'Puffle Park'
TargetGameTitle = 'Puffle Tricks'
TargetGameInstructionsSinglePlayer = 'Take your pet for a walk and click the puffle icon to perform tricks!'
TargetGameInstructionsMultiPlayer = 'Nuzzle'
TargetGameBoard = 'Round %s - Keeping Best Score'
TargetGameCountdown = 'Forced launch in %s seconds'
TargetGameCountHelp = 'Speak'
TargetGameFlyHelp = 'Jump'
TargetGameFallHelp = 'Stand on head'
TargetGameBounceHelp = 'Rollover'
PhotoGameScoreTaken = '%s: %s\nYou: %s'
PhotoGameScoreBlank = 'Score: %s'
PhotoGameScoreOther = '\n%s'
PhotoGameScoreYou = 'Spin'
TagGameTitle = 'Dig'
TagGameInstructions = 'How to Adopt'
TagGameYouAreIt = 'You and your puffle can now do tricks. Congrats!'
TagGameSomeoneElseIsIt = '%s is IT!'
MazeGameTitle = 'They\'re a great way to bond with your puffles!'
MazeGameInstructions = 'Click on the Puffle Trick icon and choose one.' + Cogs + '!'
CatchGameTitle = 'Coins earned:'
CatchGameInstructions = 'Catch as many %(fruit)s as you can. Watch out for the ' + Cogs + ", and try not to 'catch' any %(badThing)s!"
CatchGamePerfect = 'PERFECT!'
CatchGameApples = 'apples'
CatchGameOranges = 'oranges'
CatchGamePears = 'pears'
CatchGameCoconuts = 'coconuts'
CatchGameWatermelons = 'watermelons'
CatchGamePineapples = 'pineapples'
CatchGameAnvils = 'anvils'
PieTossGameTitle = 'Your total coins:'
PieTossGameInstructions = 'Use your coins to:'
PhotoGameInstructions = 'Penguin is in a soccer shootout!'
PhotoGameTitle = 'Penguin is in the Stadium'
PhotoGameFilm = 'FILM'
PhotoGameScore = 'Team Score: %s\n\nBest Photos: %s\n\nTotal Score: %s'
CogThiefGameTitle = Cog + ' Thief'
CogThiefGameInstructions = 'Up Next' + Cogs + 'Now playing'
CogThiefBarrelsSaved = '%(num)d Barrels\nSaved!'
CogThiefBarrelSaved = '%(num)d Barrel\nSaved!'
CogThiefNoBarrelsSaved = 'You are #number in the playlist.'
CogThiefPerfect = 'PERFECT!'
MinigameRulesPanelPlay = 'PLAY'
GagShopName = "You are not sharing any tracks."
GagShopPlayAgain = 'PLAY\nAGAIN'
GagShopBackToPlayground = 'Loading SoundStudio'
GagShopYouHave = 'You have %s jellybeans to spend'
GagShopYouHaveOne = 'Would you like to start SoundStudio?'
GagShopTooManyProps = 'Go to SoundStudio'
GagShopDoneShopping = 'DONE\nSHOPPING'
GagShopTooManyOfThatGag = 'Sorry, you have enough %s already'
GagShopInsufficientSkill = 'DJ3K Tracks'
GagShopYouPurchased = 'You purchased %s'
GagShopOutOfJellybeans = 'Members can record and share tracks in SoundStudio!'
GagShopWaitingOtherPlayers = 'Make Music'
GagShopPlayerDisconnected = '%s has disconnected'
GagShopPlayerExited = '%s has exited'
GagShopPlayerPlayAgain = 'Instructions'
GagShopPlayerBuying = 'Buying'
GenderShopQuestionMickey = 'Saved Tracks'
GenderShopQuestionMinnie = 'Shared Tracks'
GenderShopFollow = 'Members can share music from their Saved Tracks'
GenderShopSeeYou = 'Not Sharing'
GenderShopBoyButtonText = 'Boy'
GenderShopGirlButtonText = 'Girl'
BodyShopHead = 'Head'
BodyShopBody = 'Body'
BodyShopLegs = 'Legs'
ColorShopToon = 'a Track'
ColorShopHead = 'Head'
ColorShopBody = 'Body'
ColorShopLegs = 'Legs'
ColorShopParts = 'Members can share a track and visit the Dance Club to hear it play.'
ColorShopAll = 'Other players can listen and Like it!'
ClothesShopShorts = 'Shorts'
ClothesShopShirt = 'Shirts'
ClothesShopBottoms = 'Bottoms'
PromptTutorial = "Currently Sharing"
MakeAToonSkipTutorial = 'Oops, something\'s wrong.  Please try again later.'
MakeAToonEnterTutorial = 'Come back tomorrow to like this again!'
MakeAToonDone = 'Done'
MakeAToonCancel = lCancel
MakeAToonNext = lNext
MakeAToonLast = 'Back'
CreateYourToon = 'Go to the Dance Club to hear your song play!'
CreateYourToonTitle = 'On'
ShapeYourToonTitle = 'Off'
PaintYourToonTitle = 'Sharing!'
PickClothesTitle = 'Likes:'
NameToonTitle = 'Your track list is full.'
CreateYourToonHead = "Delete a song to make some room."
MakeAToonClickForNextScreen = 'You don\'t have any saved tracks.'
PickClothes = 'Use SoundStudio to make a song.'
PaintYourToon = 'Start SoundStudio'
MakeAToonYouCanGoBack = 'Recording and sharing  SoundStudio tracks requires  a paid membership.'
MakeAFunnyName = 'Create New Track'
MustHaveAFirstOrLast1 = "This song and all its Likes will be deleted."
MustHaveAFirstOrLast2 = "yes"
ApprovalForName1 = "no"
ApprovalForName2 = 'Choose a set of sounds.'
MakeAToonLastStep = 'Each button plays a sound. Loops repeat,  while one-shots play once each time you press them...'
PickANameYouLike = 'Members can hit Record to save and share songs'
TitleCheckBox = 'Title'
FirstCheckBox = 'First'
LastCheckBox = 'Last'
RandomButton = 'Random'
ShuffleButton = 'Shuffle'
NameShopSubmitButton = 'Submit'
TypeANameButton = 'Type-A-Name'
TypeAName = "Members can view and share songs in Saved Tracks."
PickAName = 'Shared tracks play in the Dance Club and your igloo.  Other players listening in the Dance Club can Like your song!'
PickANameButton = 'Pick-A-Name'
RejectNameText = 'Pop'
WaitingForNameSubmission = 'Rock'
PetNameMaster = 'PetNameMasterEnglish.txt'
PetNameIndexMAX = 2713
PetshopUnknownName = 'Dance'
PetshopDescGender = 'Gender:\t%s'
PetshopDescCost = 'Cost:\t%s jellybeans'
PetshopDescTrait = 'Traits:\t%s'
PetshopDescStandard = 'Standard'
PetshopCancel = lCancel
PetshopSell = 'Dubstep'
PetshopAdoptAPet = 'Save'
PetshopReturnPet = 'Cancel'
PetshopAdoptConfirm = 'Adopt %s for %d jellybeans?'
PetshopGoBack = 'Name Your Track'
PetshopAdopt = 'Adopt'
PetshopReturnConfirm = 'Return %s?'
PetshopReturn = 'Return'
PetshopChooserTitle = "LOOPS"
PetshopGoHomeText = 'ONE-SHOTS'
NameShopNameMaster = 'NameMasterEnglish.txt'
NameShopPay = 'Subscribe'
NameShopPlay = 'Record'
NameShopOnlyPaid = 'Stop'
NameShopContinueSubmission = 'Shared Tracks'
NameShopChooseAnother = 'Members can share music from their Saved Tracks'
NameShopToonCouncil = 'Recording and sharing SoundStudio tracks requires a paid membership' + 'Please choose another name'
PleaseTypeName = 'Would you like to play SoundStudio?'
AllNewNames = 'Penguin is Mixing Music'
NameMessages = 'Soundstudio'
NameShopNameRejected = 'Skatepark'
NameShopNameAccepted = 'Penguin is at the Skatepark'
NoPunctuation = "day"
PeriodOnlyAfterLetter = 'Spooky'
ApostropheOnlyAfterLetter = 'New spooky sounds available for  your tracks!'
NoNumbersInTheMiddle = 'Haunt the  Dance Club with spooky sounds!'
ThreeWordsOrLess = 'Holiday Giveaway'
CopyrightedNames = ('mickey',
 'Wear',
 'mickeymouse',
 'minnie',
 'Are you ready to adopt a blue crystal puffle?',
 'minniemouse',
 'donald',
 'Choose a name',
 'donaldduck',
 'pluto',
 'goofy')
NumToColor = ['White',
 'Peach',
 'Penguin is in the Mystery Attic',
 'Red',
 'Maroon',
 'Sienna',
 'Brown',
 'Tan',
 'Coral',
 'Orange',
 'Yellow',
 'Cream',
 'Citrine',
 'Lime',
 'Penguin is in the Puffle Lodge',
 'Green',
 'Penguin is visiting the Wild Puffle Reserve',
 'Aqua',
 'Blue',
 'Periwinkle',
 'Wild puffles require a paid membership.',
 'Members can:',
 'Purple',
 'Lavender',
 'Pink',
 'Plum',
 'Black']
AnimalToSpecies = {'dog': 'Dog',
 'cat': 'Cat',
 'mouse': 'Mouse',
 'horse': 'Horse',
 'rabbit': 'Rabbit',
 'duck': 'Duck',
 'monkey': 'Monkey',
 'bear': 'Bear',
 'pig': 'Pig'}
NameTooLong = 'Adopt all the wild puffle creatures available'
ToonAlreadyExists = 'You already have a toon named %s!'
NameAlreadyInUse = 'Go on walks with them and dig for treasures'
EmptyNameError = 'Bring them to their igloo or into their backyard'
NameError = 'Choose a color'
NCTooShort = 'Puffle Wild'
NCNoDigits = 'Access and play music in their igloos'
NCNeedLetters = 'Use SoundStudio to record and play music in their igloos'
NCNeedVowels = 'Penguin is at the Mall'
NCAllCaps = 'Training Missions'
NCMixedCase = 'From the archives of the island\'s first defenders, the Penguin Secret Agency.'
NCBadCharacter = "Your name cannot contain the character '%s'"
NCGeneric = 'These missions are in English.'
NCTooManyWords = 'Unlocks on June 18'
NCDashUsage = "Unlocks on June 25"
NCCommaEdge = 'Launch Mission'
NCCommaAfterWord = 'Play Again'
NCCommaUsage = '1. Case of the Missing Puffles'
NCPeriodUsage = '2. G\'s Secret Mission'
NCApostrophes = '3. Case of the Missing Coins'
RemoveTrophy = lToonHQ + ': ' + TheCogs + '4. Avalanche Rescue'
STOREOWNER_TOOKTOOLONG = '5. Secret of the Fur'
STOREOWNER_GOODBYE = '6. Questions for a Crab'
STOREOWNER_NEEDJELLYBEANS = '7. Clockwork Repairs'
STOREOWNER_GREETING = '8. Mysterious Tremors'
STOREOWNER_BROWSING = '9. Operation: Spy & Seek'
STOREOWNER_NOCLOTHINGTICKET = '10. Waddle Squad'
STOREOWNER_NOFISH = '11. The Veggie Villain'
STOREOWNER_THANKSFISH = 'Agent: Progress will not save during your mission. Make sure you have around 40 minutes to complete it.'
STOREOWNER_THANKSFISH_PETSHOP = 'Mall'
STOREOWNER_PETRETURNED = "The Mall"
STOREOWNER_PETADOPTED = 'Mall'
STOREOWNER_PETCANCELED = 'The Mall'
STOREOWNER_NOROOM = 'Agent. Training missions complete. You are now ready for anything. Be resourceful, be remarkable, be ready!'
STOREOWNER_CONFIRM_LOSS = 'Earn medals by completing Training Missions or doing Spy Drills.'
STOREOWNER_OK = lOK
STOREOWNER_CANCEL = lCancel
STOREOWNER_TROPHY = 'Wow! You collected %s of %s fish. That deserves a trophy and a Laff boost!'
SuitInvasionBegin1 = lToonHQ + 'Collect'
SuitInvasionBegin2 = lToonHQ + ': %s have taken over Toontown!!!'
SuitInvasionEnd1 = lToonHQ + ': The %s Invasion has ended!!!'
SuitInvasionEnd2 = lToonHQ + 'Mission Accomplished'
SuitInvasionUpdate1 = lToonHQ + ': The Cog Invasion is now at %s Cogs!!!'
SuitInvasionUpdate2 = lToonHQ + ': We must defeat those %s!!!'
SuitInvasionBulletin1 = lToonHQ + 'Excellent work, agent.'
SuitInvasionBulletin2 = lToonHQ + ': %s have taken over Toontown!!!'
LeaderboardTitle = 'Missions Menu'
QuestScriptTutorialMickey_1 = 'Spy Gear Catalog'
QuestScriptTutorialMickey_2 = 'Sure, %s!'
QuestScriptTutorialMickey_3 = 'PSA Missions'
QuestScriptTutorialMickey_4 = 'Club Penguin Music'
QuestScriptTutorialMinnie_1 = 'SoundStudio'
QuestScriptTutorialMinnie_2 = 'Sure, %s!'
QuestScriptTutorialMinnie_3 = 'Your Coins'
QuestScript101_1 = 'Agent. Train to hone your EPF skills. Be resourceful, be remarkable, be ready!'
QuestScript101_2 = 'Go to the Town to learn about Club Penguin Island, a whole new experience.'
QuestScript101_3 = 'This requires a paid membership'
QuestScript101_4 = 'Like'
QuestScript101_5 = "Challenge Tickets"
QuestScript101_6 = 'Change'
QuestScript101_7 = 'Submit'
QuestScript101_8 = 'Your votes'
QuestScript101_9 = "Members can:"
QuestScript101_10 = 'Transform!'
QuestScript101_11 = "Adopting this puffle requires a paid membership"
QuestScript101_12 = 'Members can:'
QuestScript101_13 = 'Adopt all the alien puffles while they are available'
QuestScript101_14 = 'Penguin is having an alien encounter'
QuestScript110_1 = 'Hello. You can collect free gifts from this calendar. New ones unlock every day until Dec. 25. Happy holidays!'
QuestScript110_2 = 'Adopt'
QuestScript110_3 = "Members can adopt dino puffles and transform into dinosaurs"
QuestScript110_4 = "Go There"
QuestScript110_5 = 'Go There'
QuestScript110_6 = 'Go There'
QuestScript110_7 = 'This item requires a paid membership.'
QuestScript110_8 = 'Members can:'
QuestScript110_9 = 'Collect'
QuestScript110_10 = 'Wanna wear your new item? Click the penguin icon!'
QuestScript110_11 = 'https://web.archive.org/web/20170329041509/https://www.clubpenguinisland.com/pre-registration/'
QuestScriptTutorialBlocker_1 = 'Welcome to the Waddle On party, everyone. It�s our celebration of the years of fun we�ve had on the island.'
QuestScriptTutorialBlocker_2 = 'Hello?'
QuestScriptTutorialBlocker_3 = "Test your knowledge with trivia questions and fill out your memories page. And thank you for making the Club Penguin community so amazing!"
QuestScriptTutorialBlocker_4 = 'It�s time for puffle questions in the Forest. I�ve written a couple that might even stump PH herself!'
QuestScriptTutorialBlocker_5 = 'Looks like you enjoy the fuzzy furballs as much as I do! Well done.'
QuestScriptTutorialBlocker_6 = "There are new trivia questions. But they�re in a secret location!"
QuestScriptTutorialBlocker_7 = "I suppose I should be concerned about EPF knowledge going public, but I�m impressed!"
QuestScriptTutorialBlocker_8 = 'If you�re a history buff, then check out the Cove for new trivia questions.'
QuestScriptGagShop_1 = 'Good job with the trivia. You could be a Club Penguin Times reporter.'
QuestScriptGagShop_1a = 'Visit the Dock and test your knowledge about items and igloos.'
QuestScriptGagShop_3 = 'Excellent job. You sound like an avid collector of items.'
QuestScriptGagShop_4 = 'Are you a black belt? Then you�ll score high on the Ninja trivia in the Dojo.'
QuestScriptGagShop_5 = "What does Sensei say? Something about �rocking the house�? I�m sure that applies to you here."
QuestScriptGagShop_6 = "The Stadium is hosting the next big trivia match!"
QuestScriptGagShop_7 = 'GOAL! What a performance! I enjoyed that as much as any soccer match'
QuestScriptGagShop_8 = "The island has transformed a lot over the years. Test your memory of rooms in the Plaza."
QuestScript120_1 = "You�ve paid close attention to the island over the years. Well done."
QuestScript120_2 = 'Together, we can build an island, create a community, change the world... and even tip an iceberg. Waddle on.'
QuestScript121_1 = "You've proven to be a trivia master and collected every pin for your memory book. Well done!"
QuestScript130_1 = 'Amazing! I never thought I�d witness the iceberg tipping! Congratulations on your discovery.'
QuestScript131_1 = 'View Memory Pages'
QuestScript140_1 = 'Trivia topic for the Forest' + lDonaldsDock + 'Visit the Iceberg'
QuestScript141_1 = 'PUFFLES'
QuestScript145_1 = 'Get 3 right to unlock items!'
QuestScript145_2 = "Earn coins by answering more trivia"
QuestScript150_1 = 'Visit the Forest'
QuestScript150_2 = 'Unlocks on Feb. 3'
QuestScript150_3 = 'Trivia topic for the HQ'
QuestScript150_4 = 'SPIES'
MissingKeySanityCheck = 'Get 3 right to unlock items!'
SellbotBossName = 'Earn coins by answering more trivia.'
CashbotBossName = 'Visit the HQ'
LawbotBossName = 'Unlocks on Feb. 4'
BossCogNameWithDept = '%(name)s\n%(dept)s'
BossCogPromoteDoobers = 'You are hereby promoted to full-fledged %s.  Congratulations!'
BossCogDoobersAway = {'s': 'Trivia topic for the Cove'}
BossCogWelcomeToons = 'PARTIES'
BossCogPromoteToons = 'You are hereby promoted to full-fledged %s.  Congratu--'
CagedToonInterruptBoss = 'Get 3 right to unlock items!'
CagedToonRescueQuery = 'Earn coins by answering more trivia.'
BossCogDiscoverToons = 'Visit the Cove'
BossCogAttackToons = 'Attack!!'
CagedToonDrop = ["Great job!  You're wearing him down!",
 "Unlocks on Feb. 6",
 'Trivia topic for the Dock',
 "Items & Igloos"]
CagedToonPrepareBattleTwo = "Get 3 right to unlock items!"
CagedToonPrepareBattleThree = "Earn coins by answering more trivia"
BossBattleNeedMorePies = 'Visit the Dock'
BossBattleHowToGetPies = 'Unlocks on Feb. 8'
BossBattleHowToThrowPies = 'Trivia topic for the Dojo'
CagedToonYippee = 'Yippee!'
CagedToonThankYou = "NINJAS"
CagedToonPromotion = "Get 3 right to unlock items!"
CagedToonLastPromotion = "\x07Wow, you've reached level %s on your Cog suit!\x07Cogs don't get promoted higher than that.\x07You can't upgrade your Cog suit anymore, but you can certainly keep rescuing Toons!"
CagedToonHPBoost = "Earn coins by answering more trivia"
CagedToonMaxed = '\x07I see that you have a level %s Cog suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to rescue more Toons!'
CagedToonGoodbye = 'Visit the Dojo'
CagedToonBattleThree = {10: 'Nice jump, %(toon)s.  Here are some pies!',
 11: 'Hi, %(toon)s!  Have some pies!',
 12: "Hey there, %(toon)s!  You've got some pies now!",
 20: 'Hey, %(toon)s!  Jump up to my cage and get some pies to throw!',
 21: 'Hi, %(toon)s!  Use the Ctrl key to jump up and touch my cage!',
 100: 'Unlocks on Feb. 10',
 101: 'Trivia topic for the Stadium',
 102: 'MINIGAMES',
 103: 'Get 3 right to unlock items!',
 104: "Earn coins by answering more trivia",
 105: "Visit the Stadium",
 106: 'Unlocks on Feb. 11'}
CagedToonBattleThreeMaxGivePies = 12
CagedToonBattleThreeMaxTouchCage = 21
CagedToonBattleThreeMaxAdvice = 106
CashbotBossHadEnough = "Trivia topic for the Plaza"
CashbotBossOuttaHere = "ISLAND HISTORY"
ResistanceToonName = 'Get 3 right to unlock items!'
ResistanceToonCongratulations = "You did it!  Congratulations!\x07You're an asset to the Resistance!\x07Here's a special phrase you can use in a tight spot:\x07%s\x07When you say it, %s.\x07But you can only use it once, so choose that time well!"
ResistanceToonToonupInstructions = 'all the Toons near you will gain %s Laff points'
ResistanceToonToonupAllInstructions = 'Earn coins by answering more trivia'
ResistanceToonMoneyInstructions = 'all the Toons near you will gain %s jellybeans'
ResistanceToonMoneyAllInstructions = 'Visit the Plaza'
ResistanceToonRestockInstructions = 'all the Toons near you will restock their "%s" gags'
ResistanceToonRestockAllInstructions = 'Members can collect the Alumni Jacket.'
ResistanceToonLastPromotion = "\x07Wow, you've reached level %s on your Cog suit!\x07Cogs don't get promoted higher than that.\x07You can't upgrade your Cog suit anymore, but you can certainly keep working for the Resistance!"
ResistanceToonHPBoost = "Visit the Town"
ResistanceToonMaxed = '\x07I see that you have a level %s Cog suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to rescue more Toons!'
CashbotBossCogAttack = 'Celebrate at the Waddle On party until Mar. 29'
ResistanceToonWelcome = 'Learn about the new Club Penguin Island'
ResistanceToonTooLate = "https://web.archive.org/web/20170329041509/https://www.clubpenguinisland.com/"
CashbotBossDiscoverToons1 = 'Ah-HAH!'
CashbotBossDiscoverToons2 = 'Wear the alumni jacket that shows how old their penguin is.'
ResistanceToonKeepHimBusy = "Club Penguin Island is the place for adventure, friends, fashion, and stinky cheese."
ResistanceToonWatchThis = 'Penguins new and old work to make it a welcoming, wonderful community.'
CashbotBossGetAwayFromThat = 'Club Penguin Island is the place for adventure, friends, fashion, and stinky cheese. Penguins new and old work to make it a welcoming, wonderful community.'
ResistanceToonCraneInstructions1 = 'Thank you for making Club Penguin so incredibly inspiring. Waddle on, everyone!'
ResistanceToonCraneInstructions2 = 'THE BAND IS BACK!'
ResistanceToonCraneInstructions3 = "HOW TO WRITE A HIT"
ResistanceToonCraneInstructions4 = 'HOLIDAY TRADITION RETURNS'
ResistanceToonGetaway = 'COINS COMING IN!'
CashbotCraneLeave = 'NEW YEAR, NEW HORIZON!'
CashbotCraneAdvice = 'WADDLING ON'
CashbotMagnetAdvice = 'LETTER FROM THE EDITORAction news live!'
CashbotCraneLeaving = 'Tell us what\'s happening!'
MintElevatorRejectMessage = 'You cannot enter the Mints until you have completed your %s Cog Suit.'
BossElevatorRejectMessage = 'There\'s a giant monster!'
NotYetAvailable = 'No! Two of them!!!'
SellbotRentalSuitMessage = "GRAWL! I HUNGRY!"
SellbotCogSuitNoMeritsMessage = "'GASP!' They'll eat the entire city!"
SellbotCogSuitHasMeritsMessage = "Who will save us now?"
FurnitureTypeName = 'Furniture'
PaintingTypeName = 'Painting'
ClothingTypeName = 'Clothing'
ChatTypeName = 'The city needs our help!'
EmoteTypeName = 'Super costume mega transform!'
BeanTypeName = 'Jellybeans'
PoleTypeName = 'Hooray! The heroes have arrived!'
WindowViewTypeName = 'Of course. Who else could save the day?'
PetTrickTypeName = 'Freeze Squidzoid and Melmonst!'
GardenTypeName = 'You\'ve both eaten enough!'
RentalTypeName = 'BLARRG! YOU CAN\'T STOP US!'
GardenStarterTypeName = 'Oh yeah? PLASMA GLOW WAVE!'
NametagTypeName = 'RROOOOAAAARR!'
AccessoryTypeName = 'Accessory'
CatalogItemTypeNames = {0: 'INVALID_ITEM',
 1: FurnitureTypeName,
 2: ChatTypeName,
 3: ClothingTypeName,
 4: EmoteTypeName,
 5: 'WALLPAPER',
 6: 'The superheroes are using their powers!',
 7: 'FLOORING',
 8: 'MOULDING',
 9: 'WAINSCOTING',
 10: PoleTypeName,
 11: PetTrickTypeName,
 12: BeanTypeName,
 13: GardenTypeName,
 14: RentalTypeName,
 15: GardenStarterTypeName,
 16: NametagTypeName,
 17: 'TOON_STATUE',
 18: 'Hooray heroes! Nice going!',
 19: AccessoryTypeName}
HatStylesDescriptions = {'hbb1': 'PUNY HEROES!',
 'hbb2': 'YOU\'RE NO MATCH FOR US!',
 'hbb3': 'Try this on for size! SHADOW WAVE!',
 'hsf1': 'GLEEGRRAUWLL!',
 'hsf2': 'Wait! Squidzoid\'s running.',
 'hsf3': 'But Melmonst is staying!',
 'hrb1': 'Not the most reliable sidekick.',
 'hrb2': 'You\'re right. And he doesn\'t say a lot.',
 'hrb3': 'We can\'t have monsters all over the city!',
 'hht1': 'Quick! With our powers combined!',
 'hht2': 'For great justice!',
 'htp1': 'For freedom!!',
 'htp2': 'For the love of pizza with extra olives!',
 'hav1': 'NO! THIS IS IMPOSSIBLE! GRRAAA!',
 'hfp1': 'It\'s turning into a penguin!',
 'hsg1': 'Hey, I\'m a penguin again.',
 'hwt1': 'What happened?',
 'hfz1': 'You turned into Squidzoid!',
 'hgf1': 'And started eating the city!',
 'hpt1': 'Oh! I had a monster appetite!',
 'hpt2': 'But there\'s still Melmonst!',
 'hpb1': 'Hmm... looks kind of stuck up there.',
 'hcr1': 'Crown',
 'hcw1': 'Not a danger at all!',
 'hpr1': 'It makes a nice ornament.',
 'hpp1': 'Looks like our work here is done!',
 'hfs1': 'Let\'s go get a fish pizza.',
 'hsb1': 'Extra olives, please!',
 'hst1': 'The city is saved!',
 'hsu1': 'This reporter is signing off.',
 'hrb4': 'ACTION!',
 'hrb5': 'From the top.',
 'hrb6': 'Places please!',
 'hrb7': 'Special effects please!',
 'hat1': 'Bravo! Fantastic acting!',
 'hhd1': 'CART SURFER',
 'hbw1': 'COFFEE SHOP',
 'hch1': 'ASTRO-BARRIER',
 'hdt1': 'HOT CHOCOLATE',
 'hft1': 'LANDING PAD',
 'hfd1': 'Fedora',
 'hmk1': "PIZZA CHEF",
 'hft2': 'PAINT BY LETTERS',
 'hhd2': 'MINE',
 'hpc1': 'CONSTRUCTION WORKER',
 'hrh1': 'JET PACK ADVENTURE',
 'hhm1': 'GIFT SHOP',
 'hat2': 'HIKING IN THE FOREST',
 'htr1': 'Tiara',
 'hhm2': 'RESCUE SQUAD',
 'hwz1': 'PET SHOP',
 'hwz2': 'SKI VILLAGE',
 'hhm3': 'ICE HOCKEY',
 'hhm4': 'SKI HILL',
 'hfp2': 'SNOWBALL FIGHT',
 'hhm5': 'SNOW FORTS',
 'hnp1': 'SOCCER',
 'hpc2': 'BEACH',
 'hph1': 'FOOTBALL',
 'hwg1': 'BASEBALL',
 'hbb4': 'EMERALD PRINCESS',
 'hbb5': 'BEAN COUNTERS',
 'hbb6': 'MANHOLE COVER',
 'hsl1': 'NEWSPAPER ARCHIVES',
 'hfr1': 'UNDERGROUND POOL',
 'hby1': 'SCUBA DIVING',
 'hrb8': 'ICE FISHING',
 'hjh1': 'CASE OF THE MISSING COINS',
 'hbb7': 'CRATES AND BOXES',
 'hrb9': 'ANVIL SMITH',
 'hwt2': 'HALLOWEEN',
 'hhw1': 'Bandana',
 'hhw2': 'KNIGHT',
 'hob1': 'BLACK PUFFLE',
 'hbn1': 'MEDIEVAL PARTY'}
GlassesStylesDescriptions = {'grd1': 'BLUE PUFFLE',
 'gmb1': 'PINK PUFFLE',
 'gnr1': 'GREEN PUFFLE',
 'gst1': 'PUFFLE FURNITURE',
 'g3d1': 'PURPLE PUFFLE',
 'gav1': 'Aviator',
 'gce1': 'RED PUFFLE',
 'gdk1': 'YELLOW PUFFLE',
 'gjo1': 'SUMMER PARTY',
 'gsb1': 'GRAY FISH',
 'ggl1': 'Goggles',
 'ggm1': 'O BERRY',
 'ghg1': 'LIFE RING',
 'gie1': 'JOLLY ROGER FLAG',
 'gmt1': 'COINS',
 'gmt2': 'GARY THE GADGET GUY',
 'gmt3': 'BUOYS',
 'gmt4': 'YARR',
 'gmt5': 'KLUTZY',
 'gmn1': 'Monocle',
 'gmo1': 'HERBERT P. BEAR',
 'gsr1': 'HOT SAUCE',
 'ghw1': 'SNOW CASTLE',
 'ghw2': 'AUNT ARCTIC',
 'gag1': 'CHRISTMAS CAROLS'}
BackpackStylesDescriptions = {'bpb1': 'BETA PARTY',
 'bpb2': 'HIDDEN ITEMS',
 'bpb3': 'SECRET AGENT',
 'bpd1': 'SNOW SHOVEL',
 'bpd2': 'THE MIGRATOR',
 'bwg1': 'CAPTAIN ROCKHOPPER',
 'bwg2': 'ICE CREAM',
 'bwg3': 'MULLET',
 'bst1': 'UNDERGROUND FLOOD',
 'bfn1': 'FLUFFY THE FISH',
 'baw1': 'SHARK',
 'baw2': 'FLOORING UPGRADE',
 'bwt1': 'GADGET ROOM',
 'bwg4': 'JACKHAMMER',
 'bwg5': 'JET PACK',
 'bwg6': 'THIN ICE',
 'bjp1': 'NIGHT VISION GOGGLES',
 'blg1': 'MIGHTY PLUNGER',
 'bsa1': 'DRAGON',
 'bwg7': 'SPACE ADVENTURE',
 'bsa2': 'TOUR GUIDE',
 'bsa3': 'SLED RACING',
 'bap1': 'PUFFLE ROUND-UP',
 'bhw1': 'AC3000',
 'bhw2': 'SNOW GLOBE IGLOO',
 'bhw3': 'SHADOW GUY & GAMMA GAL',
 'bhw4': 'AVALANCHE',
 'bob1': 'WATER PARTY',
 'bfg1': 'CATCHIN\' WAVES',
 'bfl1': 'FIREFIGHTER'}
ShoesStylesDescriptions = {'sat1': 'AQUA GRABBER',
 'sat2': 'OCTOPUS',
 'smb1': 'CACTUS',
 'scs1': 'TIPPING THE ICEBERG',
 'swt1': 'Wingtips',
 'smj1': 'NINJA',
 'sdk1': 'WHITE PUFFLE',
 'sat3': 'Yarr',
 'scs2': 'KEEPER OF THE BOILER ROOM',
 'scs3': 'BLAST',
 'scs4': 'FLARE',
 'scb1': 'CHIRP',
 'sfb1': 'POP',
 'sht1': 'LOOP',
 'smj2': 'FLIT',
 'smj3': 'BOUNCER',
 'ssb1': 'ED MCCOOL AND DESTRUCTO',
 'sts1': 'NIBLET',
 'sts2': 'SNOWY NIGHT',
 'scs5': 'PUFFLES ON THE LOOSE',
 'smb2': 'CADENCE AND THE KEEPER',
 'smb3': 'GOLDEN PUFFLE',
 'smb4': 'METEOR PUFFLE',
 'sfb2': 'RAINBOW PUFFLE',
 'sfb3': 'ABOMINABLE SNOW PUFFLE',
 'sfb4': 'Club Penguin Times',
 'sfb5': 'Can of Worms',
 'sfb6': 'Winter Fiesta Party',
 'slf1': 'Loafers',
 'smj4': 'Invisible Ninja Suit',
 'smt1': 'Penguin Mail',
 'sox1': 'Oxfords',
 'srb1': 'Bumble Bee',
 'sst1': 'Pizzatron 3000',
 'swb1': 'Card-Jitsu',
 'swb2': 'Adopt-A-Puffle',
 'swk1': 'Rock & Roll Suit',
 'scs6': 'Construction',
 'smb5': 'Hidden Pins',
 'sht2': 'Treasure Hunt Game',
 'srb2': 'DJ3K',
 'sts3': 'Surf Boards',
 'sts4': 'Beach Chair Chilling',
 'sts5': 'Telescope',
 'srb3': 'Fish Costume',
 'srb4': 'Crow\'s Nest',
 'sat4': 'The Cove',
 'shw1': 'Captain\'s Quarters',
 'shw2': 'Iceberg'}
AccessoryNamePrefix = {0: 'hat unisex ',
 1: 'The Lounge',
 2: 'Rockhopper\'s Key',
 3: 'Penguins That Time Forgot',
 4: 'Team Blue Rally',
 5: 'Jet Pack Adventure',
 6: 'Ruby and the Ruby',
 7: 'Snowball Fight',
 8: 'Snowball Press',
 9: 'Music Jam',
 10: 'Puffle Chew-Chew',
 11: 'Fairy Fables'}
AwardManagerAccessoryNames = {}
AccessoryTypeNames = {}
for accessoryId in list(CatalogAccessoryItemGlobals.AccessoryTypes.keys()):
    accessoryInfo = CatalogAccessoryItemGlobals.AccessoryTypes[accessoryId]
    if accessoryInfo[0] % 4 == 0:
        accessoryStyleDescription = HatStylesDescriptions
    elif accessoryInfo[0] % 4 == 1:
        accessoryStyleDescription = GlassesStylesDescriptions
    elif accessoryInfo[0] % 4 == 2:
        accessoryStyleDescription = BackpackStylesDescriptions
    else:
        accessoryStyleDescription = ShoesStylesDescriptions
    if accessoryInfo[3]:
        AwardManagerAccessoryNames[accessoryId] = AccessoryNamePrefix[accessoryInfo[0]] + accessoryStyleDescription[accessoryInfo[1]]
    AccessoryTypeNames[accessoryId] = accessoryStyleDescription[accessoryInfo[1]]

ShirtStylesDescriptions = {'bss1': 'solid',
 'bss2': 'Jelly Fish',
 'bss3': 'collar',
 'bss4': 'Pirate',
 'bss5': 'Fish Bait',
 'bss6': 'Hydro Hopper',
 'bss7': 'hawaiian',
 'bss8': 'Puffle O\'s',
 'bss9': 'Fall Fair Games',
 'bss10': 'Thinga-ma-jig 3000',
 'bss11': 'Rad Scientist',
 'bss12': 'Quip and Qua',
 'bss13': 'Twee',
 'bss14': 'Coins For Change',
 'bss15': 'guayavera',
 'gss1': 'Surfing with the Sharks',
 'gss2': 'Dance Contest',
 'gss3': 'Purple Octopus',
 'gss4': 'Giant Squid',
 'gss5': 'Penguin Band',
 'gss6': 'Dojo Sketch',
 'gss7': 'Flare Flinger 3000',
 'gss8': 'Herbert & Klutzy',
 'gss9': 'Coffee Delivery Truck',
 'gss10': 'Anniversary Party',
 'gss11': 'Halloween Party',
 'gss12': 'Sensei',
 'gss13': 'Jackhammers',
 'gss14': 'Quest for the Golden Puffle',
 'gss15': 'Storm',
 'c_ss1': 'Rockhopper',
 'c_ss2': 'Camera',
 'c_ss3': 'Wigs',
 'c_bss1': 'Pizza Parlor',
 'c_bss2': 'Coffee Machine',
 'c_bss3': 'Costume Trunk',
 'c_bss4': 'Pet Shop Staff',
 'c_gss1': 'Stompin\' Bob',
 'c_gss2': 'G Billy',
 'c_gss3': 'Outdoor Igloo',
 'c_gss4': 'Ticket Booth',
 'c_gss5': 'Ridge Run',
 'c_ss4': 'Clock Tower',
 'c_ss5': 'White Puffles',
 'c_ss6': 'Dojo Courtyard',
 'c_ss7': 'Rocking Horse',
 'c_ss8': 'Penguin Style',
 'c_ss9': 'Stage Director',
 'c_ss10': 'Conductor',
 'c_ss11': 'Beacon',
 'hw_ss1': 'Discovering The Underground',
 'hw_ss2': 'Franky',
 'hw_ss3': 'Petey K.',
 'hw_ss4': 'Boombox',
 'hw_ss5': 'Mild Mannered Reporter',
 'hw_ss6': 'The Twelfth Fish',
 'hw_ss7': 'April Fool\'s Day Party',
 'hw_ss8': 'Plasma Glow Wave',
 'hw_ss9': 'Cowbell',
 'wh_ss1': 'O Berry Bush',
 'wh_ss2': 'Chester The Time Traveler',
 'wh_ss3': '101 Days of Fun',
 'wh_ss4': 'Color Vote',
 'vd_ss1': 'Christmas Party',
 'vd_ss2': 'Viking Opera',
 'vd_ss3': 'Water Balloons',
 'vd_ss4': 'Tuba',
 'vd_ss5': 'Rockhopper\'s Plants',
 'vd_ss6': 'Adventure Party',
 'vd_ss7': 'Penguin Play Awards',
 'sd_ss1': "All-Access Pass",
 'sd_ss2': "Cadence's Autograph",
 'sd_ss3': 'Treasure Book',
 'tc_ss1': 'Black Hoodie',
 'tc_ss2': 'Propellor Cap',
 'tc_ss3': 'Dessert Pizza',
 'tc_ss4': 'Black Electric Guitar',
 'tc_ss5': 'Mastering The Elements',
 'tc_ss6': 'Elite Penguin Force',
 'tc_ss7': 'Switchbox 3000',
 'j4_ss1': 'Medieval Party',
 'j4_ss2': 'Cadence',
 'c_ss12': 'Cloud Wave',
 'c_ss13': 'Ghost Sheet',
 'pj_ss1': 'Cart Surfer',
 'pj_ss2': 'Keytar',
 'pj_ss3': 'X-treme Jetpack',
 'sa_ss1': 'Box Dimension',
 'sa_ss2': 'Gold Viking Helmet',
 'sa_ss3': 'Gary The Gadget Guy',
 'sa_ss4': 'Rockhopper\'s Cannon',
 'sa_ss5': 'Multi-Player',
 'sa_ss6': 'Fire Battle',
 'sa_ss7': 'Fired Up',
 'sa_ss8': 'Goldsmith',
 'sa_ss9': 'Scroll',
 'sa_ss10': 'Volcano',
 'sa_ss11': 'Ready For Battle',
 'sa_ss12': 'Flying Flippers Emporium',
 'sa_ss13': 'Duel',
 'sa_ss14': 'Concentrate',
 'sa_ss15': 'Interior Construction',
 'sa_ss16': 'Elements Hideout',
 'sa_ss17': 'Scavenger Hunt',
 'sa_ss18': 'Fire Wheel',
 'sa_ss19': 'Amulet Construction',
 'sa_ss20': 'Fire Dance',
 'sa_ss21': 'Sketched Action',
 'sa_ss22': 'Fire Guardian',
 'sa_ss23': 'Hot Sauce Reserve',
 'sa_ss24': 'Sketched: Volcano',
 'sa_ss25': 'Orange Sky',
 'sa_ss26': 'Sketched: Enter',
 'sa_ss27': 'Amulet',
 'sa_ss28': 'A New Journey',
 'sa_ss29': 'Fire Door & Key',
 'sa_ss30': 'Sensei Fire',
 'sa_ss31': 'Fire Ninja',
 'sa_ss32': 'Monkey King',
 'sa_ss33': 'Jet Pack Pilot',
 'sa_ss34': 'Fairy Princess',
 'sa_ss35': 'Puffle Grooming',
 'sa_ss36': 'Halloween Costumes',
 'sa_ss37': 'Costume Show',
 'sa_ss38': 'Soccer Match',
 'sa_ss39': 'Bean Counters',
 'sa_ss40': 'Earth Day Recycling',
 'sa_ss41': 'Penguin Play Awards',
 'sa_ss42': 'Goal!',
 'sa_ss43': 'Bamboo Forest Sketch',
 'sa_ss44': 'The Mine Cave is Safe!',
 'sa_ss45': 'Mine Cave Construction',
 'sa_ss46': 'Guardian Dog',
 'sa_ss47': 'The Fair',
 'sa_ss48': 'Hockey Gear',
 'sa_ss49': 'Puffle Show',
 'sa_ss50': 'Holiday Gifts',
 'sa_ss51': 'Holiday Activities',
 'sa_ss52': 'Stadium',
 'sa_ss53': 'Igloo Items',
 'sa_ss54': 'Music Jam',
 'sa_ss55': 'Elite Penguin Sketch',
 'sc_1': 'Festival of Flight',
 'sc_2': 'Test Glider',
 'sc_3': 'Puffle Paddle',
 'sil_1': 'Fancy Formal Wear',
 'sil_2': 'The Docks',
 'sil_3': 'Orange Puffle',
 'sil_4': 'Community Tree',
 'sil_5': 'Community Garden',
 'sil_6': 'Island Adventure Party',
 'sil_7': 'Shops in Igloos',
 'sil_8': 'Seafarer\'s Gown',
 'emb_us1': 'Music Jam Dancers',
 'emb_us2': 'Music Jam Rock Stage',
 'emb_us3': 'Music Jam Pop Stage',
 'sb_1': 'Underwater Adventure',
 'lb_1': 'Norman Swarm',
 'jb_1': 'Puffle Rescuer',
 'jb_2': 'Everyday Phoning Facility',
 'ugcms': 'Jet Packs'}
BottomStylesDescriptions = {'bbs1': 'Pumpkin Igloo',
 'bbs2': 'belt',
 'bbs3': 'cargo',
 'bbs4': 'hawaiian',
 'bbs5': 'Treasure Hunt Adventure',
 'bbs6': 'Destroyed PSA HQ',
 'bbs7': 'Captains',
 'bbs8': 'denim',
 'vd_bs1': 'April Fools',
 'vd_bs2': 'The Great Snow Maze',
 'vd_bs3': 'Jacques Hammer',
 'c_bs1': 'Throne of April Fools',
 'c_bs2': 'The Test',
 'c_bs5': 'Cloud Maker 3000',
 'sd_bs1': 'Super Exclusives',
 'sd_bs2': 'Rockslide at the Mine',
 'pj_bs1': 'Mer-penguins',
 'pj_bs2': 'Puffer Fish',
 'pj_bs3': 'Garden Hose',
 'wh_bs1': 'Fixing the Mine Shack',
 'wh_bs2': 'Puffle Circus',
 'wh_bs3': 'Puffle Play Sketch',
 'wh_bs4': 'Dragon Statue',
 'hw_bs1': 'Popcorn Party',
 'hw_bs2': 'White Puffle Room',
 'hw_bs5': 'Green Puffle Sketch',
 'hw_bs6': 'Fishbowl Igloo',
 'hw_bs7': 'Ship Battle Adventure',
 'sil_bs1': 'Elite Penguin Force',
 'gsk1': 'solid',
 'gsk2': 'Rockhopper\'s Notice Board',
 'gsk3': 'Squid Lid',
 'gsk4': 'Hidden Lake',
 'gsk5': 'Orange Puffle Wagon',
 'gsk6': 'Haunted House',
 'gsk7': 'Fire Dragon',
 'gsh1': 'Puffle Rescue: Underground',
 'gsh2': 'flower',
 'gsh3': 'Double Necked Guitar',
 'c_gsk1': 'Puffle Rescue: Ice Floes',
 'c_gsk2': 'Spy Phone',
 'c_gsk3': 'Dance Contest',
 'vd_gs1': 'Crab Costume',
 'vd_gs2': 'Puffle Washer',
 'vd_gs3': 'Green Jackhammer',
 'c_gsk4': 'The Veggie Villain',
 'sd_gs1': 'Island Lifter 3000',
 'sd_gs2': 'Flare',
 'c_gsk5': 'Popcorn Device',
 'c_gsk6': 'Field-Ops',
 'c_bs3': 'Recipe for Disaster',
 'c_bs4': 'Elite Agent',
 'j4_bs1': 'Aunt Arctic Sketch',
 'j4_gs1': 'Yeti Cave',
 'c_gsk7': 'Shocktopus',
 'pj_gs1': 'Puffle Rescue: Underwater',
 'pj_gs2': 'Hidden Lake Lock',
 'pj_gs3': 'Knight\'s Quest',
 'wh_gsk1': 'Spooky Igloo Contest',
 'wh_gsk2': 'Halloween Countdown!',
 'wh_gsk3': 'Stormy Skies',
 'wh_gsk4': '5th Anniversary Party',
 'sa_bs1': '5th Anniversary Cake',
 'sa_bs2': '5th Anniversary Yearbook',
 'sa_bs3': 'Snowball Fight!',
 'sa_bs4': 'Find Four',
 'sa_bs5': 'Cozy Ski Lodge',
 'sa_bs6': 'Holiday Decorations!',
 'sa_bs7': 'Book Room Adventures',
 'sa_bs8': 'Halloween Forest',
 'sa_bs9': 'Brown Puffle Rocket',
 'sa_bs10': 'Fun at the Fair!',
 'sa_bs11': 'Ski Hill Challenge',
 'sa_bs12': 'Holiday Party Skating',
 'sa_bs13': 'Treasure!',
 'sa_bs14': 'Lumberjack Look',
 'sa_bs15': 'Pink Sparkle Snowshoes',
 'sa_bs16': 'Holiday Tree 2010',
 'sa_bs17': 'Fill the Lighthouse!',
 'sa_bs18': 'Wilderness Machine',
 'sa_bs19': 'Expedition Boat',
 'sa_bs20': 'Wilderness Expedition Cave',
 'sa_bs21': 'Water Party Prep',
 'sa_gs1': 'Water Dance',
 'sa_gs2': 'Stamp Collectors',
 'sa_gs3': 'Explore the Wilderness',
 'sa_gs4': 'Coins for Change 2010!',
 'sa_gs5': 'Penguin Colors',
 'sa_gs6': 'Fairy Fables',
 'sa_gs7': 'Penguins That Time Forgot',
 'sa_gs8': 'EPF Sketch',
 'sa_gs9': 'Cove Stories',
 'sa_gs10': 'Orange Circus Puffle',
 'sa_gs11': 'Hydro Hopper',
 'sa_gs12': 'Igloo Party!',
 'sa_gs13': 'Life Underwater',
 'sa_gs14': 'Herbert\'s Monologue',
 'sa_gs15': 'Enemy Bots',
 'sa_gs16': 'Paint By Letters',
 'sa_gs17': 'Secret Agent',
 'sa_gs18': 'Fireworks',
 'sa_gs19': 'EPF Tech Agent',
 'sa_gs20': 'Popcorn Explosion',
 'sa_gs21': 'Walk Your Puffle',
 'sc_bs1': 'Sumo Smash',
 'sc_bs2': 'inventive Brown Puffle',
 'sc_bs3': 'Holiday Party Tree',
 'sc_gs1': 'EPF Enemies',
 'sc_gs2': 'Tall Tree Maze',
 'sc_gs3': 'Sled \'n Slide',
 'sil_bs1': 'Underwater at the Stage',
 'sil_gs1': 'Wilderness Expedition Travel',
 'hw_bs3': 'Catch the Mullet!',
 'hw_gs3': 'Great Puffle Circus',
 'hw_bs4': 'Intense Black Puffle',
 'hw_gs4': 'Brown Puffle Storyboard',
 'hw_gs1': 'Java Jump',
 'hw_gs2': 'Master the Elements',
 'hw_gs5': 'Fairy Fables Stage',
 'hw_gs6': 'Creative Puffles',
 'hw_gs7': 'Goofy Green Puffle',
 'hw_gsk1': 'EPF Test Room'}
AwardMgrBoy = 'boy'
AwardMgrGirl = 'girl'
AwardMgrUnisex = 'unisex'
AwardMgrShorts = 'shorts'
AwardMgrSkirt = 'skirt'
AwardMgrShirt = 'shirt'
SpecialEventMailboxStrings = {1: 'Snowball Battle',
 2: "Fabulous Purple Puffle",
 3: "Water Party Sketch",
 4: 'Zany Orange Puffle',
 5: 'Sporty Pink Puffle',
 6: 'Wii Game Day "Goal!"',
 7: "Epic White Puffle",
 8: 'Awesome Blue Puffle',
 9: '"Feed a Puffle"',
 10: 'Ninja Battle',
 11: 'The Mystery of Sensei',
 12: 'Master the Elements',
 13: 'Brown Puffle',
 14: 'Fire Wave',
 15: 'Black Puffles in Cart Surfer',
 16: 'Mountain Expedition',
 17: 'Climbing the Mountain'}
RentalHours = 'Hours'
RentalOf = 'Of'
RentalCannon = 'Cannons!'
RentalGameTable = 'Top of Toughest Mountain'
EstateCannonGameEnd = 'Cart Surfer Stamps'
GameTableRentalEnd = 'Stamp Book'
MessageConfirmRent = 'Stormy Sky'
MessageConfirmGarden = 'Water Wave Sketches'
NametagPaid = 'Storm Baffles Gary'
NametagAction = 'Water Ninja'
NametagFrilly = 'The First Rainstorm'
FurnitureYourOldCloset = 'Ninja Face-off'
FurnitureYourOldBank = 'Earning the Water Suit'
FurnitureYourOldTrunk = 'Water Pumping Gadget'
TrunkHatGUI = 'Hats'
TrunkGlassesGUI = 'Glasses'
TrunkBackpackGUI = 'Backpacks'
TrunkShoesGUI = 'Shoes'
ChatItemQuotes = '"%s"'
FurnitureNames = {100: 'Armchair',
 105: 'Armchair',
 110: 'Chair',
 120: 'Preparing the Water Dojo',
 130: 'Gate to the Water Dojo',
 140: 'Water Suit',
 145: 'Sign From The Elements',
 150: 'Sensei - Master of Water',
 160: 'Water Ninja Poster Sketch',
 170: 'Water Ninja Sketch',
 200: 'Bed',
 205: 'Bed',
 210: 'Bed',
 220: 'Water Beats Fire Sketch',
 230: 'Blast',
 240: 'Flare',
 250: 'Chirp',
 260: 'Pop',
 270: "Loop",
 300: 'Flit',
 310: 'Bouncer',
 400: 'Fireplace',
 410: 'Fireplace',
 420: 'Ed McCool and Destructo',
 430: 'Fireplace',
 440: 'Niblet',
 450: "Snowy Night",
 460: "Puffles on the Loose",
 470: 'Cadence and the Keeper',
 480: 'Golden puffle',
 490: 'Meteor puffle',
 491: 'Rainbow puffle',
 492: 'Abominable snow puffle',
 500: 'Wardrobe',
 502: 'Black Puffle',
 504: 'Blue Puffle',
 506: 'Pink Puffle',
 508: 'Green Puffle',
 510: 'Wardrobe',
 512: 'Purple Puffle',
 514: 'Red Puffle',
 516: 'Yellow Puffle',
 518: 'Puffle Round Up',
 600: 'Fire Ninja Force',
 610: 'Halloween Swamp',
 620: 'Prepare for Pumpkins',
 625: 'Finding Rockhopper',
 630: 'Elite Puffle: Flare',
 640: 'Giant Pearl',
 650: 'Water Stamps',
 660: 'EPF Agents',
 670: 'Puffle Rescue',
 680: 'Candle',
 681: 'Fire Dojo Challenge',
 700: 'System Defender',
 705: 'Adventurous Red Puffle',
 710: 'Couch',
 715: 'Couch',
 720: 'G and the Machine',
 730: 'Enemies of the System',
 800: 'Desk',
 810: 'Holiday Dojo Lights',
 900: 'Wii Rollin\' Riot',
 910: 'EPF Under Attack',
 920: 'Elite Comm Class Agents',
 930: 'Brown Puffle Cliff',
 940: 'Coins for Change Goal!',
 950: 'Sensei Water Battle',
 960: 'Green Puffles in Jet Pack Adve',
 970: 'Water Dojo',
 980: 'Teepee',
 990: "White Puffle",
 1000: 'Yarr',
 1010: 'Keeper of the Boiler Room',
 1015: 'Mobile Fire 1',
 1020: 'Mobile Snow 1',
 1030: 'Mobile Water 1',
 1040: 'Presents',
 1050: 'Sled',
 1100: 'Mobile Fire Power Card 1Contents',
 1110: 'Puffle Species',
 1120: 'Blue',
 1130: 'About Puffles',
 1140: 'Puffle Card',
 1200: 'Puffle Fun',
 1210: 'What Is A Puffle?',
 1215: 'Puffles are small, round, furry creatures. Each color is unique. And they make great pets!',
 1220: 'Most species are native to the wilds of Club Penguin, but some were discovered far away.',
 1230: 'Personality',
 1240: "Toys",
 1250: 'Observed',
 1260: 'in the Wild',
 1300: 'Favorite Snack',
 1310: 'Best Game',
 1320: 'Cool Fact',
 1330: 'Would you like to purchase a new puffle?',
 1340: 'Puffle Quiz',
 1350: 'Which puffle is the most like you?',
 1399: 'Telephone',
 1400: 'Stats',
 1410: 'Flowers',
 1420: 'Name',
 1430: 'Weight',
 1440: 'Toonscape',
 1441: "Personality",
 1442: 'Toy',
 1443: 'Favorite Game',
 1450: 'Adopt',
 1500: 'Radio',
 1510: 'Radio',
 1520: 'Radio',
 1530: 'Television',
 1600: 'Ready to adopt',
 1610: 'your new puffle?',
 1620: 'Name Ideas',
 1630: 'Adopt',
 1640: 'Feeding',
 1650: 'Bathing',
 1660: 'Grooming',
 1661: 'Manual',
 1670: 'I, agree to adopt for 400 coins.',
 1680: 'You currently have coins.',
 1700: 'Yes',
 1710: 'Ladybug',
 1720: 'Fountain',
 1725: 'No',
 1800: 'Walk',
 1810: 'Igloo',
 1900: 'Swordfish',
 1910: 'Hammerhead',
 1920: 'you\'d make a great puffle owner.',
 1930: 'Adopt',
 1940: 'I, agree to adopt for 400 coins.',
 1950: 'Ready to adopt your new healthy, happy puffle?',
 1960: 'Horseshoe',
 1970: 'Adopt',
 2000: 'Adventerous, extreme',
 2010: 'Sporty, cheery',
 3000: 'Fabulous, particular',
 4000: 'Intense, strong',
 4010: 'Playful, funny',
 10000: 'Shy, powerful, gentle',
 10010: 'Creative, spontaneous',
 10020: 'Curious, unpredictable, zany',
 10030: 'Super smart, inventive'}
AwardManagerFurnitureNames = {100: 'Loyal, content, team player',
 105: 'TBD',
 110: 'Your puffle will let you know when it is happy, sad, tired or hungry.',
 120: 'Click the Food tab to feed it, the Play tab to get its toys, or the Care tab to groom, walk, or ask your puffle to sleep.',
 130: 'If you want to look at the Handbook or read/print your pet\'s Adoption Certificate, click "Pet Papers".',
 140: 'If you care for your puffle, it\'ll be in your igloo. If it isn\'t happy and healthy, it will return to its natural habitat.',
 145: 'Care',
 150: 'Certificate',
 160: 'Feed',
 170: 'Handbook',
 200: "Play",
 205: "Pet Papers",
 210: "Caring for your Puffle",
 220: 'Play',
 230: 'Puffles can dig up coins around the island. So walk a puffle wherever you go!',
 240: 'The longer you\'ve cared for your puffle, the more it will find!',
 250: 'Catchin\' Waves',
 260: 'Dance Contest',
 270: "Aqua Grabber",
 300: 'DJ3K',
 310: 'Cart Surfer',
 400: 'Jet Pack Adventure',
 410: 'Walk',
 420: 'Puffles love to walk with you, one at a time. They\'ll even dance when you do!',
 430: 'Treasure',
 440: 'Puffles love to play in your igloo. Give them their favorite toy! Or decorate with puffle furniture!',
 450: "Red",
 460: "Pink",
 470: 'Purple',
 480: 'Black',
 490: 'Green',
 491: 'White',
 492: 'Yellow',
 500: 'Orange',
 502: 'Brown',
 504: 'Care',
 506: 'Games',
 508: 'Play',
 510: 'Walk',
 512: 'They\'re known for their awesome team work. Few realize that each week blue puffles eat their weight in cookies.',
 514: 'From the wilds of Rockhopper Island, they love adventure. Puffle experts wonder what secrets they hold.',
 516: 'It is said that the pink puffle\'s fur can hold 30 times its weight in water.',
 518: 'The flash of a disco ball transforms this stylish puffle into a powerful dance force.',
 600: 'Although mostly quiet, sudden fiery outbursts show there is more to these intense creatures than meets the eye.',
 610: 'Are experts on unicycles. They are',
 620: 'also known for their love of',
 625: 'April Fool\'s parties.',
 630: 'It may be smaller than all other puffles, but its power is unmeasurable',
 640: 'It is rumored that the yellow puffle creates artwork from food and furniture.',
 650: 'This species has teeth strong enough to demolish petrified Puffle O\'s. And everything else.',
 660: 'It is documented that the brown puffle blinks more than all other puffles. Its dreams have graph paper backgrounds.',
 670: 'Loyal, team player',
 680: 'Candle',
 681: 'Adventurous, extreme',
 700: 'Athletic, cheery',
 705: 'Fabulous, particular',
 710: 'Intense, strong',
 715: 'Playful, funny',
 720: 'Shy, powerful, gentle',
 730: 'Creative, spontaneous',
 800: 'Desk',
 810: 'Curious, zany',
 900: 'Smart, inventive',
 910: 'Ball, snowballs',
 920: 'Bowling pins, cannon',
 930: 'Skipping rope, snorkel, trampoline',
 940: 'Disco ball, bubble wand',
 950: 'Skateboard',
 960: 'Propeller Cap, unicycle',
 970: 'Ice skates, snowflakes',
 980: 'Teepee',
 990: "Paintbrush, easel",
 1000: 'Box, wagon, truck',
 1010: 'Beakers, rockets',
 1015: 'Rallying teams together',
 1020: 'Hunting for buried treasure',
 1030: 'Using bubblegum to float',
 1040: 'Presents',
 1050: 'Sled',
 1100: 'Bursting into flames after eating Puffle O\'s',
 1110: 'Vacuums up cookies',
 1120: 'with its mouth',
 1130: 'Makes music that gets everyone dancing',
 1140: 'Choosing just the right outfit for just the right occasion',
 1200: 'Freezes liquid at will',
 1210: 'Making quick decisions',
 1215: 'Superior machine',
 1220: 'building skills',
 1230: 'Favorite Place',
 1240: "Pretzels",
 1250: 'Stinky cheese',
 1260: 'Watermelon',
 1300: 'Fish burger',
 1310: 'Tacos',
 1320: 'Performing and creating',
 1330: 'Hummus and pita',
 1340: 'Yogurt parfait',
 1350: 'Socks',
 1399: 'Telephone',
 1400: 'Astronaut ice cream',
 1410: 'Flowers',
 1420: 'Can bounce really high',
 1430: 'Originally from',
 1440: 'Toonscape',
 1441: "Rockhopper Island",
 1442: 'Loves to exercise and swim',
 1443: 'Super good at skateboarding',
 1450: 'Laughs an average of 14.7 times a day',
 1500: 'Wears a beret to paint',
 1510: 'Uses a sleep mask for beauty rest',
 1520: 'Slightly smaller than',
 1530: 'Television',
 1600: 'other species',
 1610: 'Rumored to eat fridges whole',
 1620: 'Afraid of balloons',
 1630: 'Catchin\' Waves',
 1640: 'Aqua Grabber',
 1650: 'Cart Surfer',
 1660: 'DJ3K',
 1661: 'Dance Contest',
 1670: 'Snow Forts',
 1680: 'Are you sure you want to return to its natural habitat?',
 1700: 'Your puffle was returned successfully.',
 1710: 'Ladybug',
 1720: 'Fountain',
 1725: 'Ok',
 1800: 'Your coins:',
 1810: '0',
 1900: 'Swordfish',
 1910: 'Hammerhead',
 1920: 'This certifies that',
 1930: 'belongs to:',
 1940: 'Adopted on:/2',
 1950: 'Do you want to take for a walk or back to your igloo?',
 1960: 'Horseshoe',
 1970: 'Pizza Parlor',
 2000: 'The Dojo',
 2010: 'Jet Pack Adventure',
 3000: 'Buy a membership',
 4000: 'Print',
 4010: 'To adopt and care for more than 2 puffles, you must',
 10000: 'become a member.',
 10010: 'We\'d love to have you join!',
 10020: 'OOPS!',
 10030: 'Popcorn'}
ClothingArticleNames = ('Shirt',
 'Shirt',
 'Shirt',
 'Shorts',
 'Shorts',
 'Skirt',
 'Shorts')
ClothingTypeNames = {1001: 'Ok',
 1002: 'Learn More',
 1112: 'Everyone can adopt 2 puffles (red and blue).',
 1113: 'And members can adopt every color',
 1114: '- up to!',
 1115: 'Auto Disconnect, your penguin has been idle for more than 10 minutes',
 1116: 'You need more coins',
 1117: 'You can only have one Club Penguin window open at a time. Please close any other windows and tabs in your internet browser to connect.',
 1118: 'The connection has been lost.',
 1119: 'Thank you for playing Club Penguin.',
 1120: 'Waddle on!',
 1121: 'Find out more',
 1122: 'Done',
 1123: 'Sorry, that name is unavailable!',
 1124: 'You already own the maximum number of puffles!',
 1125: 'Penguin is playing Aqua Grabber',
 1126: 'Penguin is playing Astro Barrier',
 1127: 'Penguin is playing Bean Counters',
 1304: "O'Shirt",
 1305: "O'Shorts",
 1306: "O'Skirt",
 1400: "Penguin is Cart Surfing",
 1401: "Penguin is Ice Fishing",
 1402: "Penguin is flying a Jet Pack",
 1600: 'Penguin is playing Thin Ice',
 1601: 'Penguin is Surfing',
 1602: 'Penguin is playing Hydro Hopper',
 1603: 'Penguin is making pizzas',
 1604: 'Penguin is rounding up puffles',
 1605: 'Penguin is playing Manacala',
 1606: 'Penguin is playing Find Four',
 1607: 'Penguin is in a Sled Race',
 1608: 'Penguin is reading a Book',
 1723: 'Penguin is reading a Book',
 1724: 'Penguin is reading a Book',
 1734: 'Penguin is Mixing Music',
 1735: 'Penguin is digging for treasure',
 1739: 'Penguin is playing Balloon Pop',
 1740: 'Penguin is playing Ring The Bell',
 1743: 'Penguin is playing Feed-A-Puffle',
 1744: 'Penguin is playing Memory Card Game',
 1745: 'Penguin is playing Puffle Paddle',
 1746: 'Penguin is playing Puffle Shuffle',
 1747: 'Penguin is playing Puffle Soaker',
 1748: 'Penguin is playing Spin To Win',
 1749: 'Penguin is playing Card-Jitsu',
 1750: 'Penguin is playing Card-Jitsu Fire',
 1751: 'Penguin is playing Card-Jitsu Water',
 1752: 'Penguin is challenging the Sensei',
 1753: 'Penguin is challenging the Sensei',
 1754: 'Penguin is challenging the Sensei',
 1755: 'Penguin is in a Dance Contest!',
 1756: 'Penguin is Rescuing Puffles',
 1757: 'Penguin is playing System Defender',
 1758: 'Penguin is playing Bits and Bolts',
 1763: 'Penguin is on an Adventure',
 1764: 'Penguin is on an Adventure',
 1765: 'Penguin is on an Adventure',
 1766: 'Penguin is on an Adventure',
 1767: 'Penguin is on an Adventure',
 1768: 'Penguin is on an Adventure',
 1769: 'Penguin is on an Adventure',
 1770: 'Penguin is on an Adventure',
 1771: 'Penguin is on an Adventure',
 1772: 'Penguin is on an Adventure',
 1773: 'Penguin is on an Adventure',
 1774: 'Penguin is in the Town',
 1775: 'Penguin is in the Coffee Shop',
 1776: 'Penguin is in the Book Room',
 1777: 'Penguin is in the Dance Club',
 1778: 'Penguin is in the Dance Lounge',
 1779: 'Penguin is in the Clothes Shop',
 1780: 'Penguin is in the Ski Village',
 1781: 'Penguin is on top of the Mountain',
 1782: 'Penguin is in the Sport Shop',
 1783: 'Penguin is in the Plaza',
 1784: 'Penguin is in the Pet Shop',
 1801: 'Penguin is in the Dojo',
 1802: 'Penguin is in the Dojo Courtyard'}
AccessoryArticleNames = ('Hat',
 'Glasses',
 'Backpack',
 'Shoes',
 'Hat',
 'Glasses',
 'Backpack',
 'Shoes',
 'Hat',
 'Glasses',
 'Backpack',
 'Shoes')
SurfaceNames = ('Wallpaper',
 'Moulding',
 'Flooring',
 'Wainscoting',
 'Border')
WallpaperNames = {1000: 'Parchment',
 1100: 'Milan',
 1200: 'Dover',
 1300: 'Victoria',
 1400: 'Newport',
 1500: 'Pastoral',
 1600: 'Harlequin',
 1700: 'Moon',
 1800: 'Stars',
 1900: 'Flowers',
 2000: 'Penguin is in Hiding',
 2100: 'Penguin is in the Fire Dojo',
 2200: 'Penguin is in the Water Dojo',
 2300: 'Touchdown!',
 2400: 'Penguin is in the Pizza Parlor',
 2500: 'Penguin is at the Beach',
 2600: 'Springtime',
 2700: 'Kokeshi',
 2800: 'Posies',
 2900: 'Penguin is in the Lighthouse',
 3000: 'Bubbles',
 3100: 'Bubbles',
 3200: 'Penguin is at the Lighthouse Beacon',
 3300: 'Penguin is on the Pirate Ship',
 3400: 'Penguin is in the Pirate Ship Hold',
 3500: 'Penguin is in the Captain\'s Quarters',
 3600: 'Underwater',
 3700: 'Boots',
 3800: 'Cactus',
 3900: 'Penguin is in the Crow\'s Nest',
 10100: 'Cats',
 10200: 'Bats',
 11000: 'Snowflakes',
 11100: 'Hollyleaf',
 11200: 'Snowman',
 12000: 'ValenToons',
 12100: 'ValenToons',
 12200: 'ValenToons',
 12300: 'ValenToons',
 13000: 'Shamrock',
 13100: 'Shamrock',
 13200: 'Rainbow',
 13300: 'Shamrock'}
FlooringNames = {1000: 'Penguin is at the Dock',
 1010: 'Carpet',
 1020: 'Penguin is at the Snow Forts',
 1030: 'Penguin is hiding',
 1040: 'Grass',
 1050: 'Penguin is hiding',
 1060: 'Penguin is hiding',
 1070: 'Penguin is in the Everyday Phoning Facility',
 1080: 'Stone',
 1090: 'Boardwalk',
 1100: 'Dirt',
 1110: 'Penguin is hiding',
 1120: 'Tile',
 1130: 'Honeycomb',
 1140: 'Water',
 1150: 'Penguin is in the Boiler Room',
 1160: 'Penguin is on the Iceberg (hidden on your map)',
 1170: 'Penguin is in the Cave (hidden underground)',
 1180: 'Penguin is in the Mine (hidden underground)',
 1190: 'Sand',
 10000: 'Penguin is in the Mine Shack',
 10010: 'Igloo',
 11000: 'Shamrock',
 11010: 'Shamrock'}
MouldingNames = {1000: 'Knotty',
 1010: 'Painted',
 1020: 'Dental',
 1030: 'Flowers',
 1040: 'Flowers',
 1050: 'Ladybug',
 1060: 'ValenToons',
 1070: 'Beach',
 1080: 'Penguin is in the Forest',
 1085: 'Penguin is at the Cove',
 1090: 'Penguin is in the Box Dimension',
 1100: "Penguin is digging for gold in the Gold Mine",
 1110: "Penguin is at the Hidden Lake",
 1120: "Penguin is in the Underwater Room"}
WainscotingNames = {1000: 'Painted',
 1010: 'Penguin is in the University',
 1020: 'Wood',
 1030: 'ValenToons',
 1040: 'Underwater'}
WindowViewNames = {10: 'Penguin is ???',
 20: 'Penguin is in an igloo',
 30: 'Penguin is in their igloo',
 40: 'Cityscape',
 50: 'Penguin is in your igloo',
 60: 'Would you like to addme to your ignore list?',
 70: 'Done',
 80: 'Would you like to removeme from your ignore list?',
 90: 'Done',
 100: 'Town',
 110: 'Coffee Shop',
 120: 'Book Room',
 130: 'Dance Club'}
SpecialEventNames = {1: 'Dance Lounge',
 2: "Clothes Shop",
 3: "Ski Village",
 4: 'Ski Lodge',
 5: 'Lodge Attic',
 6: 'Sport Shop',
 7: "Mountain",
 8: 'Plaza',
 9: 'Pet Shop',
 10: 'Dojo',
 11: 'Dojo Courtyard',
 12: 'Ninja Hideout',
 13: 'Fire Dojo',
 14: 'Water Dojo',
 15: 'Pizza Parlor',
 16: 'Stage',
 17: 'Beach'}
NewCatalogNotify = 'Lighthouse'
NewDeliveryNotify = 'Beacon'
CatalogNotifyFirstCatalog = 'Pirate Ship'
CatalogNotifyNewCatalog = 'Your cattlelog #%s has arrived!  You can go to your phone to order items from this cattlelog.'
CatalogNotifyNewCatalogNewDelivery = 'A new delivery has arrived at your mailbox!  Also, your cattlelog #%s has arrived!'
CatalogNotifyNewDelivery = 'Ship Hold'
CatalogNotifyNewCatalogOldDelivery = 'Your cattlelog #%s has arrived, and there are still items waiting in your mailbox!'
CatalogNotifyOldDelivery = 'Captain\'s Quarters'
CatalogNotifyInstructions = 'Crow\'s Nest'
CatalogNewDeliveryButton = 'New\nDelivery!'
CatalogNewCatalogButton = 'New\nCattlelog'
CatalogSaleItem = 'Sale!  '
DistributedMailboxEmpty = 'Dock'
DistributedMailboxWaiting = 'Snow Forts'
DistributedMailboxReady = 'Stadium'
DistributedMailboxNotOwner = 'HQ'
DistributedPhoneEmpty = "EPF Command Room"
Clarabelle = 'Clarabelle'
MailboxExitButton = 'The Facility'
MailboxAcceptButton = 'Everyday Phoning Facility'
MailBoxDiscard = 'VR Room'
MailboxAcceptInvite = 'Boiler Room'
MailBoxRejectInvite = 'Iceberg'
MailBoxDiscardVerify = 'Are you sure you want to Discard %s?'
MailBoxRejectVerify = 'Are you sure you want to Reject %s?'
MailboxOneItem = 'Cave'
MailboxNumberOfItems = 'Your mailbox contains %s items.'
MailboxGettingItem = 'Taking %s from mailbox.'
MailboxGiftTag = 'Gift From: %s'
MailboxGiftTagAnonymous = 'Anonymous'
MailboxItemNext = 'Next\nItem'
MailboxItemPrev = 'Previous\nItem'
MailboxDiscard = 'Discard'
MailboxReject = 'Reject'
MailboxLeave = 'Keep'
CatalogCurrency = 'beans'
CatalogHangUp = 'Mine'
CatalogNew = 'NEW'
CatalogBackorder = 'BACKORDER'
CatalogLoyalty = 'SPECIAL'
CatalogEmblem = 'EMBLEM'
CatalogPagePrefix = 'Page'
CatalogGreeting = "Mine Shack"
CatalogGoodbyeList = ['Bye now!',
 'Forest',
 'Cove',
 'Box Dimension',
 'Bye!']
CatalogHelpText1 = 'Gold Mine'
CatalogSeriesLabel = 'Series %s'
CatalogGiftFor = 'Hidden Lake'
CatalogGiftTo = 'To: %s'
CatalogGiftToggleOn = 'Underwater Room'
CatalogGiftToggleOff = 'Recycling Plant'
CatalogGiftToggleWait = 'Trying!...'
CatalogGiftToggleNoAck = 'Unavailable'
CatalogPurchaseItemAvailable = 'Treasure Room'
CatalogPurchaseGiftItemAvailable = 'Excellent!  %s can start using your gift right away.'
CatalogPurchaseItemOnOrder = '???'
CatalogPurchaseGiftItemOnOrder = 'Excellent! Your gift to %s will be delivered to their mailbox.'
CatalogAnythingElse = 'Penguin is online'
CatalogPurchaseClosetFull = 'Would you like to addme as your Friend?'
CatalogPurchaseNoTrunk = 'Request Sent'
CatalogPurchaseTrunkFull = 'Are you sure you want to remove this friend?'
CatalogAcceptClosetFull = 'Penguin has asked to be your buddy. Do you accept?'
CatalogAcceptNoTrunk = "Penguin is now your buddy!"
CatalogAcceptTrunkFull = 'Loading Create Penguin'
CatalogAcceptShirt = 'Loading Engine'
CatalogAcceptShorts = 'Loading Interface'
CatalogAcceptSkirt = 'Loading Gridview'
CatalogAcceptHat = 'Loading Mail'
CatalogAcceptGlasses = 'Loading Clothing'
CatalogAcceptBackpack = 'Loading Your Inventory'
CatalogAcceptShoes = 'Loading Local Language'
CatalogAcceptPole = "Loading the Igloo"
CatalogAcceptPoleUnneeded = 'Would you like to open your igloo?'
CatalogAcceptChat = 'This will add your igloo to the map.'
CatalogAcceptEmote = 'Energy'
CatalogAcceptBeans = 'Health'
CatalogAcceptRATBeans = 'Rest'
CatalogAcceptPartyRefund = "Play with Pet"
CatalogAcceptNametag = 'Feed your Pet'
CatalogAcceptGarden = 'Sleep'
CatalogAcceptPet = 'Walk your Pet'
CatalogPurchaseHouseFull = 'Loading Your Furniture'
CatalogAcceptHouseFull = 'Stop Edit'
CatalogAcceptInAttic = 'Edit Igloo'
CatalogAcceptInAtticP = 'Loading Controls'
CatalogPurchaseMailboxFull = "Loading Furniture"
CatalogPurchaseGiftMailboxFull = "%s's mailbox is full!  You can't purchase this item."
CatalogPurchaseOnOrderListFull = "Loading Floor"
CatalogPurchaseGiftOnOrderListFull = '%s has too many items currently on order.'
CatalogPurchaseGeneralError = 'The item could not be purchased because of some internal game error: error code %s.'
CatalogPurchaseGiftGeneralError = 'The item could not be gifted to %(friend)s because of some internal game error: error code %(error)s.'
CatalogPurchaseGiftNotAGift = 'This item could not be sent to %s because it would be an unfair advantage.'
CatalogPurchaseGiftWillNotFit = "This item could not be sent to %s because it doesn't fit them."
CatalogPurchaseGiftLimitReached = "This item could not be sent to %s because they've already have it."
CatalogPurchaseGiftNotEnoughMoney = "This item could not be sent to %s because you can't afford it."
CatalogAcceptGeneralError = 'The item could not be removed from your mailbox because of some internal game error: error code %s.'
CatalogAcceptRoomError = "Close Igloo"
CatalogAcceptLimitError = "Open Igloo"
CatalogAcceptFitError = "View Items"
CatalogAcceptInvalidError = 'Buy Items'
CatalogAcceptClosetError = 'Upgrade Igloo'
MailboxOverflowButtonDicard = 'Discard'
MailboxOverflowButtonLeave = 'Leave'
HDMoveFurnitureButton = 'Move\nFurniture'
HDStopMoveFurnitureButton = 'Done\nMoving'
HDAtticPickerLabel = 'Play Music'
HDInRoomPickerLabel = 'Save Igloo'
HDInTrashPickerLabel = 'All'
HDDeletePickerLabel = 'Delete?'
HDInAtticLabel = 'Attic'
HDInRoomLabel = 'Room'
HDInTrashLabel = 'Trash'
HDToAtticLabel = 'Enter Contest'
HDMoveLabel = 'Move'
HDRotateCWLabel = 'View Stored Igloo'
HDRotateCCWLabel = 'Your Friends'
HDReturnVerify = 'Users in Room'
HDReturnFromTrashVerify = 'Ignore List'
HDDeleteItem = 'Old news'
HDNonDeletableItem = "Aqua Grabber"
HDNonDeletableBank = "Astro Barrier"
HDNonDeletableCloset = "Play Beans"
HDNonDeletablePhone = "Cart Surfer"
HDNonDeletableTrunk = "Go Fishing"
HDNonDeletableNotOwner = "You can't delete %s's things!"
HDHouseFull = 'Play Jet Pack'
HDHelpDict = {'DoneMoving': 'Thin Ice',
 'Attic': 'Go Surfing',
 'Room': 'Hydro Hopper',
 'Trash': 'Play Pizzatron',
 'ZoomIn': 'Puffle Roundup',
 'ZoomOut': 'Play Mancala',
 'SendToAttic': 'Play Find Four',
 'RotateLeft': 'Join Sled Race',
 'RotateRight': 'Mix Music',
 'DeleteEnter': 'Treasure Hunt',
 'DeleteExit': 'Balloon Pop',
 'Ring The Bell': 'Send %s to trash.',
 'Feed-A-Puffle': 'Place %s in room.',
 'Memory Game': 'Return %s to attic.',
 'Puffle Paddle': 'Return %s to attic.'}
MessagePickerTitle = 'You have too many phrases. In order to purchase\n"%s"\n you must choose one to remove:'
MessagePickerCancel = lCancel
MessageConfirmDelete = 'Are you sure you want to remove "%s" from your SpeedChat menu?'
CatalogBuyText = 'Buy'
CatalogRentText = 'Rent'
CatalogGiftText = 'Gift'
CatalogOnOrderText = 'Puffle Shuffle'
CatalogPurchasedText = 'Puffle Soaker'
CatalogCurrent = 'Current'
CatalogGiftedText = 'Spin To Win'
CatalogPurchasedGiftText = 'Already\nOwned'
CatalogMailboxFull = 'Practice Card-Jitsu'
CatalogNotAGift = 'Practice Card-Jitsu Fire'
CatalogNoFit = "Doesn't\nFit"
CatalogMembersOnly = 'Members\nOnly!'
CatalogSndOnText = 'Practice Card-Jitsu Water'
CatalogSndOffText = 'Dance Contest'
CatalogPurchasedMaxText = 'Puffle Rescue'
CatalogVerifyPurchase = 'Purchase %(item)s for %(price)s jellybeans?'
CatalogVerifyPurchaseBeanSilverGold = 'Purchase %(item)s for %(price)s jellybeans, %(silver)s silver emblems and %(gold)s gold emblems?'
CatalogVerifyPurchaseBeanGold = 'Purchase %(item)s for %(price)s jellybeans and %(gold)s gold emblems?'
CatalogVerifyPurchaseBeanSilver = 'Purchase %(item)s for %(price)s jellybeans and %(silver)s silver emblems?'
CatalogVerifyPurchaseSilverGold = 'Purchase %(item)s for %(silver)s silver emblems and %(gold)s gold emblems?'
CatalogVerifyPurchaseSilver = 'Purchase %(item)s for %(silver)s silver emblems?'
CatalogVerifyPurchaseGold = 'Purchase %(item)s for %(gold)s gold emblems?'
CatalogVerifyRent = 'Rent %(item)s for %(price)s jellybeans?'
CatalogVerifyGift = 'Purchase %(item)s for %(price)s jellybeans as a gift for %(friend)s?'
CatalogOnlyOnePurchase = 'You may only have one of these items at a time.  If you purchase this one, it will replace %(old)s.\n\nAre you sure you want to purchase %(item)s for %(price)s jellybeans?'
CatalogExitButtonText = 'System Defender'
CatalogCurrentButtonText = 'Bits and Bolts'
CatalogPastButtonText = 'Find Player'
TutorialHQOfficerName = 'Send Mail'
NPCToonNames = {20000: 'Free Gift',
 999: 'Report Player',
 1000: lToonHQ,
 20001: Flippy,
 2001: Flippy,
 2002: 'Ignore Player',
 2003: 'Remove Ignore',
 2004: 'Add Friend',
 2005: 'Remove Friend',
 2006: 'Visit Igloo',
 2011: 'Ban Player',
 2007: lHQOfficerM,
 2008: lHQOfficerM,
 2009: lHQOfficerF,
 2010: lHQOfficerF,
 2012: 'Mute Player',
 2018: 'Kick Player',
 2013: 'Clear Penguin',
 2014: 'Town',
 2015: 'Coffee Shop',
 2016: 'Book Room',
 2017: 'Dance Club',
 2018: 'Lounge',
 2019: 'Clothes Shop',
 2020: 'Ski Village',
 2101: 'Sport Shop',
 2102: 'Ski Lodge',
 2103: 'Lodge Attic',
 2104: lHQOfficerM,
 2105: lHQOfficerM,
 2106: lHQOfficerF,
 2107: lHQOfficerF,
 2108: 'Ski Hill',
 2109: 'The Plaza',
 2110: 'Pet Shop',
 2111: 'Dojo',
 2112: 'Dojo Courtyard',
 2113: 'Pizza Parlor',
 2114: 'Stage',
 2115: 'The Beach',
 2116: 'Lighthouse',
 2117: 'Beacon',
 2118: 'Pirate Ship',
 2119: 'Hold',
 2120: 'Captain\'s Quarters',
 2121: 'Crow\'s Nest',
 2122: 'The Dock',
 2123: 'Snow Forts',
 2124: 'T.P. Rolle',
 2125: 'Stadium',
 2126: 'EPF Command Room',
 2127: 'Facility',
 2128: 'Everyday Phoning Facility',
 2129: 'VR Room',
 2130: 'Boiler Room',
 2131: 'Iceberg',
 2132: 'Cave',
 2133: 'Mine',
 2134: 'Mine Shack',
 2135: 'Mary',
 2136: 'Forest',
 2137: 'Cove',
 2138: 'Muldoon',
 2139: 'Box Dimension',
 2140: 'Cave Mine',
 2201: 'Hidden Lake',
 2202: 'Underwater Room',
 2203: lHQOfficerM,
 2204: lHQOfficerM,
 2205: lHQOfficerF,
 2206: lHQOfficerF,
 2207: 'Recycling Plant',
 2208: '???',
 2209: 'Member Igloos',
 2210: 'All Items',
 2211: 'Head Items',
 2212: 'Face Items',
 2213: 'Neck Items',
 2214: 'Body Items',
 2215: 'Hand Items',
 2216: 'Feet Items',
 2217: 'Pins/Flags',
 2218: 'Other Items',
 2219: 'Backgrounds',
 2220: 'Awards',
 2221: 'Colors',
 2222: 'Teleport',
 2223: 'Visit HQ',
 2224: 'Emotes',
 2225: 'Actions',
 2301: 'Snowball',
 2302: 'Friends',
 2303: 'Show Online',
 2304: lHQOfficerM,
 2305: lHQOfficerM,
 2306: lHQOfficerF,
 2307: lHQOfficerF,
 2308: 'Show Ignored',
 2309: 'Edit Player',
 2311: 'Your Igloo',
 2312: 'Edit Account',
 2313: 'Send',
 2314: 'Chat',
 2315: 'Incorrect Password',
 2316: 'Too many failed login attempts. Please try again later.',
 2318: 'Joining',
 2319: 'Zippy',
 2320: 'Logging in',
 2321: 'Joining Player\'s Igloo',
 1001: 'PLEASE SELECT A SERVER',
 1002: 'Penguin Name:',
 1003: lHQOfficerM,
 1004: lHQOfficerF,
 1005: lHQOfficerM,
 1006: lHQOfficerF,
 1007: 'Password:',
 1008: 'Remember me on this computer',
 1009: 'Remember my password',
 1010: 'Forgot your password?',
 1011: 'Forget my penguin',
 1012: 'Login as a different penguin',
 1013: 'Your Suggested Servers',
 1101: 'Buddies online',
 1102: 'Amount of penguins online',
 1103: 'Ultimate safe chat',
 1104: 'Parents',
 1105: 'Click Here',
 1106: 'Don\'t have a penguin?',
 1107: 'Create a free account now',
 1108: lHQOfficerM,
 1109: lHQOfficerF,
 1110: lHQOfficerM,
 1111: lHQOfficerF,
 1112: 'Start',
 1113: 'Back',
 1114: 'This will permanently remove all postcards. Do you want to do this?',
 1115: 'Are you sure you want to recycle this postcard?',
 1116: 'Are you sure you want to ?',
 1117: 'This will remove all messages. This is not undoable.',
 1118: 'You havember postcards!',
 1121: 'You have 1 postcard!',
 1122: 'You have no postcards!',
 1123: 'From:',
 1124: 'New!',
 1125: 'message',
 1126: 'Send this postcard toforcoins?',
 1201: 'Buy and send',
 1202: 'Art',
 1203: 'Ahab',
 1204: 'postcards for',
 1205: lHQOfficerM,
 1206: lHQOfficerF,
 1207: lHQOfficerM,
 1208: lHQOfficerF,
 1209: 'Send to:',
 1210: 'Failed to send Postcard.',
 1211: 'You need more coins.',
 1212: 'This penguin\'s mailbox is full. Your postcard could not be sent. Please try again later.',
 1213: 'Postcard sent',
 1214: 'Postcards',
 1215: 'Preview Postcard',
 1216: 'Select a Postcard',
 1217: 'Send To',
 1218: 'Inbox',
 1219: 'You have no postcards',
 1220: 'Would you like to play',
 1221: 'Aqua Grabber?',
 1222: 'Would you like to play',
 1223: 'Astro Barrier?',
 1224: 'Would you like to play',
 1225: 'Bean Counters?',
 1226: 'Would you like to go on a',
 1227: 'Jet Pack Adventure?',
 1228: 'Would you like to go',
 1301: 'Alice',
 1302: 'Melville',
 1303: 'Claggart',
 1304: 'Svetlana',
 1305: lHQOfficerM,
 1306: lHQOfficerF,
 1307: lHQOfficerM,
 1308: lHQOfficerF,
 1309: 'Seafoam',
 1310: 'Ice Fishing?',
 1311: 'Would you like to play',
 1312: 'Hydro Hopper?',
 1313: 'Would you like to play',
 1314: 'Puffle Roundup?',
 1315: 'Would you like to join this',
 1316: 'Mancala game?',
 1317: 'Would you like to join this',
 1318: 'Find Four game?',
 1319: 'Would you like to go',
 1320: 'Cart Surfing?',
 1321: 'Would you like to play',
 1322: 'Thin Ice?',
 1323: 'Would you like to play',
 1324: 'Pizzatron 3000?',
 1325: 'Would you like to',
 1326: 'catch some waves?',
 1327: 'Would you like to join this',
 1328: 'Sled race?',
 1329: 'Would you like to read',
 1330: 'My Puffle?',
 1331: 'Would you like to read',
 1332: 'Burnt Out Bulbs?',
 3001: 'Would you like to read',
 3002: lHQOfficerM,
 3003: lHQOfficerF,
 3004: lHQOfficerM,
 3005: lHQOfficerM,
 3006: 'Lime Green Dojo Clean?',
 3007: 'Would you like to',
 3008: 'dig for treasure?',
 3009: 'Would you like to play',
 3010: 'Balloon Pop?',
 3011: 'Would you like to play',
 3012: 'Ring The Bell?',
 3013: 'Would you like to play',
 3014: 'Feed-A-Puffle?',
 3101: 'Would you like to play',
 3102: 'Memory Card Game?',
 3103: 'Fred',
 3104: 'Bonnie',
 3105: 'Would you like to play',
 3106: 'Puffle Paddle?',
 3107: 'Would you like to play',
 3108: 'Puffle Shuffle?',
 3109: 'Kate',
 3110: 'Would you like to play',
 3111: 'Puffle Soaker?',
 3112: 'Would you like to play Daily Spin?',
 3113: 'Would you like to practice',
 3114: 'Card-Jitsu?',
 3115: lHQOfficerM,
 3116: lHQOfficerF,
 3117: lHQOfficerM,
 3118: lHQOfficerM,
 3119: 'Would you like to practice',
 3120: 'Card-Jitsu Fire?',
 3121: 'Would you like to practice',
 3122: 'Card-Jitsu Water?',
 3123: 'Would you like to talk',
 3124: 'to the Sensei?',
 3125: 'Would you like to talk',
 3126: 'to the Sensei?',
 3127: 'Would you like to talk',
 3128: 'to the Sensei?',
 3129: 'You need a deck of Cards to play.',
 3130: 'Sandy',
 3131: 'Please see the Sensei first.',
 3132: 'Ashy',
 3133: 'You need a Fire Booster Deck to play.',
 3134: 'Please see the Sensei first.',
 3135: 'You need a Water Booster Deck to play.',
 3136: 'Please see the Sensei first.',
 3137: 'Would you like to dance?',
 3138: 'Would you like to play Puffle Rescue?',
 3139: 'Would you like to play System Defender?',
 3140: 'Would you like to play Bits and Bolts?',
 3201: 'You have earned 0 coins.',
 3202: 'Shakey',
 3203: 'Walt',
 3204: 'You now coins.',
 3205: 'You have earned 1 coin.',
 3206: 'You now coins.',
 3207: 'You have  coins.',
 3208: 'You now coins.',
 3209: 'Are you sure you want to quit this game?',
 3210: 'Penguin has quit the game.',
 3211: 'Loading Tutorial Prompt',
 3212: 'Your Coins:tal',
 3213: lHQOfficerM,
 3214: lHQOfficerF,
 3215: lHQOfficerM,
 3216: lHQOfficerM,
 3217: 'coins',
 3218: 'Would you like to adopt this puffle for 400 coins?',
 3219: 'Your puffle needs a name.',
 3220: 'Your new puffle is now in your igloo. Enjoy!',
 3221: 'You already own the maximum number of puffles!',
 3222: 'Would you like to buyme forst coins?',
 3223: 'Chappy',
 3224: 'Would you like to buyme forst coins?',
 3225: 'Would you like to buyme forst coins?',
 3226: 'Would you like to buyme forst coins?',
 3227: 'Would you like to buy some Pet Food for 10 coins?',
 3228: 'Would you like to bathe your puffle for 5 coins?',
 3229: 'Would you like to buy some Gum for 5 coins?',
 3230: 'Would you like to buy a Cookie for 5 coins?',
 3231: 'Choppy',
 3232: 'Penguin',
 3301: 'has been added to your inventory.',
 3302: 'Penguin has been added to your inventory.',
 3303: 'You currently havem coins.',
 3304: 'You have found ame.',
 3305: 'Would you like to pick it up?',
 3306: 'Would you like to get your Medal of Excellence?',
 3307: 'Would you like to get your gift?',
 3308: 'You have found ame.',
 3309: 'Bootsy',
 3310: 'Would you like to pick it up?',
 3311: 'You have found ame.',
 3312: 'Would you like to upgrade your igloo?',
 3313: lHQOfficerM,
 3314: lHQOfficerF,
 3315: lHQOfficerM,
 3316: lHQOfficerF,
 3317: 'You already have this item.',
 3318: 'Sorry, you must wear the tour guide',
 3319: 'hat to use this feature',
 3320: 'Are you sure you want to change your igloo? Your flooring will be lost. Igloo items will be saved in your inventory.',
 3321: 'You need more coins.',
 3322: 'You already have this item.',
 3323: 'You already have this flooring.',
 3324: 'White',
 3325: 'Yellow',
 3326: 'Blanche',
 3327: 'Orange',
 3328: 'Green',
 3329: 'Blue',
 4001: 'Red',
 4002: lHQOfficerM,
 4003: lHQOfficerF,
 4004: lHQOfficerF,
 4005: lHQOfficerF,
 4006: 'Purple',
 4007: 'Brown',
 4008: 'Black',
 4009: 'Blue',
 4010: 'Pink',
 4011: 'Black',
 4012: 'Green',
 4013: 'Purple',
 4014: 'Red',
 4101: 'Tom',
 4102: 'Fifi',
 4103: 'Yellow',
 4104: lHQOfficerM,
 4105: lHQOfficerF,
 4106: lHQOfficerF,
 4107: lHQOfficerF,
 4108: 'Cleff',
 4109: 'Carlos',
 4110: 'White',
 4111: 'Orange',
 4112: 'Fa',
 4113: 'Brown',
 4114: 'Login to Unlock Your Items',
 4115: 'What word is on pagefrom the left on line',
 4116: 'Piccolo',
 4117: 'word',
 4118: 'words',
 4119: 'items remaining',
 4120: 'item remaining',
 4121: 'You have unlockedmber item(s)!',
 4122: 'You still have items to unlock. Your code is only valid once, if you quit before you finish unlocking all your items your remaining choices will be lost.',
 4123: 'Are you sure you want to quit?',
 4124: 'Are you sure you want to redeem',
 4125: 'emName?',
 4126: 'Hello',
 4127: 'Congratulations! You\'re done! Click Yes to see what has been added to your inventory.',
 4128: 'You\'ll need to entermber more Treasure Book code(s) to unlock this page.',
 4129: 'Puffle',
 4130: 'Blue',
 4131: 'Pink',
 4132: 'Black',
 4133: 'Green',
 4134: 'Purple',
 4135: 'Red',
 4136: 'Yellow',
 4137: 'White',
 4138: 'Orange',
 4139: 'Brown',
 4140: 'You now have theem!',
 4141: 'You\'ll need to entermber more code(s) to unlock this page.',
 4201: 'Tina',
 4202: 'Barry',
 4203: 'You can choosember more Super Exclusive item(s).',
 4204: lHQOfficerM,
 4205: lHQOfficerF,
 4206: lHQOfficerF,
 4207: lHQOfficerF,
 4208: 'Hedy',
 4209: 'Yes',
 4211: 'No',
 4212: 'Ok',
 4213: 'Start',
 4214: 'Okay',
 4215: 'Close',
 4216: 'Learn More',
 4217: 'Login',
 4218: 'Sign In',
 4219: 'Visit Community Section',
 4220: 'a-z A-Z !?',
 4221: 'Loading Localized Files',
 4222: 'Loading Global Files',
 4223: 'Loading Content',
 4224: 'Loading Communication',
 4225: 'Loading Login',
 4226: 'Loading Music',
 4227: 'Rockhopper',
 4228: 'Aunt Arctic',
 4229: 'Cadence',
 4230: 'Gary',
 4231: 'Franky',
 4232: 'Petey K',
 4233: 'G Billy',
 4234: 'Stompin Bob',
 4235: 'Sensei',
 4301: 'Yuki',
 4302: 'Anna',
 4303: 'Leo',
 4304: lHQOfficerM,
 4305: lHQOfficerF,
 4306: lHQOfficerF,
 4307: lHQOfficerF,
 4308: 'Tabitha',
 4309: 'Marshall',
 4310: 'Page',
 4311: 'New',
 4312: 'Empty',
 4313: 'Club Penguin',
 4314: 'am',
 4315: 'pm',
 4316: 'hour',
 4317: 'hours',
 4318: 'of',
 4319: 'Loading',
 4320: 'Loading Ninja Progress',
 4321: 'Cards Collected:Power Cards:ofCurrent Belt',
 4322: 'Next Belt',
 4323: 'Current Item',
 4324: 'Ellie',
 4325: 'Next Item',
 4326: 'Sunday',
 4327: 'Monday',
 4328: 'Wagner',
 4329: 'Tuesday',
 4330: 'Quentin',
 4331: 'Wednesday',
 4332: 'Ziggy',
 4333: 'Harry',
 4334: 'Thursday',
 4335: 'Friday',
 5001: lHQOfficerM,
 5002: lHQOfficerM,
 5003: lHQOfficerF,
 5004: lHQOfficerF,
 5005: 'Saturday',
 5006: 'Loading Binoculars',
 5007: 'Loading Telescope',
 5008: 'Click where you want to go.',
 5009: 'Loading Map',
 5010: 'Loading Igloo Map',
 5011: 'Loading Penguin',
 5012: 'Loading Archives',
 5013: 'Loading Mancala',
 5101: 'Artie',
 5102: 'Susan',
 5103: 'Bud',
 5104: 'Flutterby',
 5105: 'Jack',
 5106: 'Loading Find Four',
 5107: 'Loading Aqua Grabber',
 5108: 'Loading Astro Barrier',
 5109: lHQOfficerM,
 5110: lHQOfficerM,
 5111: lHQOfficerF,
 5112: lHQOfficerF,
 5113: 'Loading Beans',
 5114: 'Wilt',
 5115: 'Loading Cart Surfer',
 5116: 'Loading Gone Fishing',
 5117: 'Petal',
 5118: 'Loading Jet Pack Adventure',
 5119: 'Loading Thin Ice',
 5120: 'Gopher',
 5121: 'Loading Catchin Waves',
 5122: 'Loading Hydro Hopper',
 5123: 'Loading Pizzatron 3000',
 5124: 'Loading Puffle Round-up',
 5125: 'Loading Sled Racing',
 5126: 'Loading Paint by Letters',
 5127: 'Loading Paint by Letters',
 5128: 'Loading Paint by Letters',
 5129: 'Loading Treasure Hunt',
 5201: 'Jake',
 5202: 'Cynthia',
 5203: 'Lisa',
 5204: 'Bert',
 5205: 'Loading Balloon Pop',
 5206: 'Loading Ring The Bell',
 5207: 'Loading Feed-A-Puffle',
 5208: 'Loading Memory Card Game',
 5209: lHQOfficerM,
 5210: lHQOfficerM,
 5211: lHQOfficerF,
 5212: lHQOfficerF,
 5213: 'Loading Puffle Paddle',
 5214: 'Loading Puffle Shuffle',
 5215: 'Loading Puffle Soaker',
 5216: 'Loading Spin To Win',
 5217: 'Loading Card-Jitsu',
 5218: 'Loading Card-Jitsu Fire',
 5219: 'Loading Card-Jitsu Water',
 5220: 'Loading the Sensei',
 5221: 'Loading the Sensei',
 5222: 'Loading the Sensei',
 5223: 'Clearing the dance floor...',
 5224: 'Loading Puffle Rescue',
 5225: 'Loading System Defender',
 5226: 'Loading Bits and Bolts',
 5227: 'Mancala',
 5228: 'Find Four',
 5229: 'Sled Racing',
 5301: lHQOfficerM,
 5302: lHQOfficerM,
 5303: lHQOfficerM,
 5304: lHQOfficerM,
 5305: 'Crystal',
 5306: 'Treasure Hunt',
 5307: 'Card-Jitsu',
 5308: 'Card-Jitsu Fire',
 5309: 'Card-Jitsu Water',
 5310: 'Timothy',
 5311: 'Dance Contest',
 5312: 'Eugene',
 5313: 'Settings',
 5314: 'You\'re onrvername',
 5315: 'Your penguin isold',
 5316: 'Mute Music',
 5317: 'Manage Account',
 5318: 'Caesar',
 5319: 'Rose',
 5320: 'April',
 5321: 'Friends',
 5322: 'Igloo Contest',
 8001: 'Igloo Contest',
 8002: 'Igloo Background',
 8003: 'Igloo Storage',
 8004: 'Loading Mission',
 9001: "Loading Mission",
 9002: 'Loading Mission',
 9003: 'Loading Mission',
 9004: lHQOfficerF,
 9005: lHQOfficerF,
 9006: lHQOfficerM,
 9007: lHQOfficerM,
 9008: 'Loading Mission',
 9009: 'Loading Mission',
 9010: 'Loading Mission',
 9011: 'Loading Mission',
 9012: 'Loading Mission',
 9013: 'Loading Mission',
 9014: 'Loading Mission',
 9015: 'Loading Town',
 9016: 'Loading Coffee Shop',
 9101: 'Ed',
 9102: 'Loading Book Room',
 9103: 'P.J.',
 9104: 'Loading Dance Club',
 9105: 'Loading Dance Lounge',
 9106: 'Max',
 9107: 'Snuggles',
 9108: 'Loading Clothes Shop',
 9109: 'Loading Ski Village',
 9110: 'Loading Ski Lodge',
 9111: 'Loading Lodge Attic',
 9112: 'Loading Sport Shop',
 9113: 'Loading Mountain',
 9114: 'Loading the Plaza',
 9115: 'Loading the Pet Shop',
 9116: 'Loading the Dojo',
 9117: 'Loading the Dojo Courtyard',
 9118: 'Loading the Ninja Hideout',
 9119: 'Rocco',
 9120: 'Loading the Fire Dojo',
 9121: 'Loading Water Dojo',
 9122: 'Loading the Pizza Parlor',
 9123: 'Loading the Stage',
 9124: 'Loading Beach',
 9125: 'Loading Lighthouse',
 9126: 'Loading Beacon',
 9127: 'Loading Pirate Ship',
 9128: "Loading Ship Hold",
 9129: 'Loading Captain\'s Quarters',
 9130: 'Loading Crow\'s Nest',
 9131: 'Loading the Dock',
 9132: lHQOfficerF,
 9133: lHQOfficerF,
 9134: lHQOfficerF,
 9135: lHQOfficerF,
 9136: 'Loading Snow Forts',
 9201: 'Bernie',
 9202: 'Orville',
 9203: 'Nat',
 9204: 'Loading Stadium',
 9205: 'Loading HQ',
 9206: 'Loading EPF Command Room',
 9207: 'Loading the Facility',
 9208: 'Loading the Phoning Facility',
 9209: 'Loading the VR Room',
 9210: 'Loading Boiler Room',
 9211: 'Dawn',
 9212: 'Moonbeam',
 9213: 'Loading the Iceberg',
 9214: 'Loading Cave',
 9215: 'Rip',
 9216: 'Cat',
 9217: 'Loading Mine',
 9218: 'Loading Mine Shack',
 9219: 'Loading Forest',
 9220: 'Loading the Cove',
 9221: 'Zari',
 9222: 'Loading Box Dimension',
 9223: 'Loading Cave Mine',
 9224: 'Loading the Hidden Lake',
 9225: 'Loading Underwater Room',
 9226: 'Loading Recycling Plant',
 9227: 'Loading',
 9228: 'Loading',
 9229: 'Loading',
 9230: 'Tex',
 9231: 'Loading ???',
 9232: 'Pins',
 9233: lHQOfficerM,
 9234: lHQOfficerM,
 9235: lHQOfficerM,
 9236: lHQOfficerM,
 9237: 'Released:nthy/year.',
 9301: 'All Stamps',
 9302: 'Color',
 9303: 'GiggleMesh',
 9304: 'Highlight',
 9305: 'Pattern',
 9306: 'J.S. Bark',
 9307: 'Icon',
 9308: '0/1',
 9309: 'Total Stamps:',
 9310: 'Page',
 9311: '0 ofYour Pins:',
 9312: 'Your New Stamps',
 7001: 'These are your recently earned stamps:',
 7002: 'R.E. Leaseme',
 7003: 'Congratulations on earning',
 7004: 'stamp!',
 7005: 'Congratulations on earning',
 7006: 'stamps!',
 7007: 'Total Stamps1',
 7008: 'Penguin Stamps:',
 7009: 'Penguin:'}
zone2TitleDict = {2513: ('Contents', ''),
 2514: ('Cover', ''),
 2516: ('Stamp Book Guide', ''),
 2518: ('Easy', ''),
 2519: ('Medium', ''),
 2520: (lToonHQ, ''),
 2521: ('Hard', ''),
 2522: ('Extreme', ''),
 2601: ('Member Stamp', ''),
 2602: ('', ''),
 2603: ('New Stamp', ''),
 2604: ('Edit Stamp Book', ''),
 2605: ('Save Stamp Book', ''),
 2606: ('', ''),
 2607: ('Released:nth/day/year.', ''),
 2610: ('Loading Stampbook', ''),
 2611: ('', ''),
 2616: ("Loading Stampbook", ''),
 2617: ('You\'ve earned:', ''),
 2618: ('num coins', ''),
 2621: ('num x 2 =m_x2 coins', ''),
 2624: ('1 coin', ''),
 2625: ('Your total coins:m', ''),
 2626: ("num oftal", ''),
 2629: ("Congratulations, allme_name stamps earned. Double coin bonus!", ''),
 2632: ('Congratulations, double coin bonus!', ''),
 2633: ('Earn Stamps!', ''),
 2638: ('How to earn stamps', ''),
 2639: ('game_name Stamps', ''),
 2643: ('Stamp Earned!', ''),
 2644: ('Congratulations, allme_name stamps earned.', ''),
 2649: ('Stamp Book', ''),
 2652: ('', ''),
 2653: ('', ''),
 2654: ('Your Stamps:merator/denominator', ''),
 2655: ('Loading Award', ''),
 2656: ('Loading Award', ''),
 2657: ("Loading Award", ''),
 2659: ('Loading Award', ''),
 2660: ('Loading Award', ''),
 2661: ('Loading Award', ''),
 2662: ('Loading Forest Map', ''),
 2663: ('Loading Award', ''),
 2664: ('Loading Award', ''),
 2665: ("Loading Award", ''),
 2666: ('Loading Award', ''),
 2667: ('Loading Thank You Card', ''),
 2669: ("Loading Award", ''),
 2670: ('Loading Award', ''),
 2671: ('', ''),
 2701: ('', ''),
 2704: ('Loading Award', ''),
 2705: ("Loading Award", ''),
 2708: ('Loading Award', ''),
 2711: ('Loading Award', ''),
 2712: ('Loading Award', ''),
 2713: ('Loading Award', ''),
 2714: ('Loading Starter Deck', ''),
 2716: ('Loading Award', ''),
 2717: ('Loading Award', ''),
 2720: ('Loading Wood EPF Badge', ''),
 2725: ('', ''),
 2727: ('Loading Ice EPF Badge', ''),
 2728: ('Loading Bronze EPF Badge', ''),
 2729: ('Loading Silver EPF Badge', ''),
 2730: ('Loading Gold EPF Badge', ''),
 2731: ('', ''),
 2732: ('Loading EPF Certificate', ''),
 2733: ('Loading Fire Booster Deck', ''),
 2734: ('Loading Award', ''),
 2735: ('Loading Award', ''),
 2739: ("Loading Water Booster Deck", ''),
 2740: ('Loading Stowaway', ''),
 2741: ('', ''),
 2742: ('', ''),
 2743: ('Loading Franky', ''),
 2744: ('', ''),
 2747: ('Loading Spice', ''),
 2748: ('Loading Dare', ''),
 2801: ('Loading Journal', ''),
 2802: ('Loading Tales \'07', ''),
 2803: ('Loading Tales \'08', ''),
 2804: ('Loading Tales \'09', ''),
 2805: ('', ''),
 2809: ('Loading Yearbook 05/06', ''),
 2814: ('Loading Yearbook 06/07', ''),
 2818: ('Loading Yearbook 07/08', ''),
 2821: ('', ''),
 2822: ('Loading Yearbook 08/09', ''),
 2823: ('Loading Yearbook 09/10', ''),
 2824: ('Loading Rockhopper Island', ''),
 2829: ('Loading Music Makes Magic', ''),
 2830: ("Loading Fairy Fables", ''),
 2831: ("Give a Tour", ''),
 2832: ('', ''),
 2833: ('', ''),
 2834: ('Loading Clothing Catalog', ''),
 2836: ('', ''),
 2837: ('Loading Costume Catalog', ''),
 2839: ('Loading Sport Catalog', ''),
 2841: ('', ''),
 1506: ('Loading Hair Catalog', ''),
 1507: ('Loading FISH Catalog', ''),
 1508: ('Loading Puffle Catalog', ''),
 1510: ('', ''),
 1602: ('Loading Puffle Catalog', ''),
 1604: ('Loading Pirate Catalog', ''),
 1606: ("Loading Igloo Catalog", ''),
 1608: ("Loading Furniture Catalog", ''),
 1609: ('Loading Music Catalog', ''),
 1612: ('Loading Merchandise Catalog', ''),
 1613: ('Loading Merchandise Catalog', ''),
 1614: ('Loading Prize Booth', ''),
 1615: ("Loading Member Prize Booth", ''),
 1616: ("Loading Ninja Catalog", ''),
 1617: ('Loading Cove Catalog', ''),
 1619: ('Loading Dock Catalog', ''),
 1620: ('Loading Lodge Catalog', ''),
 1621: ('Loading Ski Hill Catalog', ''),
 1622: ('Loading Diving Catalog', ''),
 1624: ('Loading Dance Catalog', ''),
 1626: ('Loading Catalog', ''),
 1627: ("Loading Lighthouse Catalog", ''),
 1628: ('Loading Member Prize Booth', ''),
 1629: ('', ''),
 1701: ('Loading Clock Tower Plaque', ''),
 1703: ('Loading Backstage Note', ''),
 1705: ('Loading Rockhopper\'s Note', ''),
 1706: ('Loading Secret Lab Note', ''),
 1707: ('Loading Ninja Belts Legend', ''),
 1709: ('Loading Sensei\'s Note', ''),
 1710: ('Loading Color Poster', ''),
 1711: ('Loading Corkboard', ''),
 1712: ('Take a Tour', ''),
 1713: ("Haunted House Poster", ''),
 1714: ("Loading Sensei's Note", ''),
 1716: ('Loading Sensei\'s Note', ''),
 1717: ('Loading Fire Clothing Poster', ''),
 1718: ('Loading Water Clothing Poster', ''),
 1719: ("Loading Maze Map", ''),
 1720: ('Loading Video', ''),
 1721: ('Loading Video', ''),
 1723: ("Loading Christmas Poster", ''),
 1724: ("Loading Dig Poster", ''),
 1725: ("Loading Dig Poster", ''),
 1726: ('Loading Treasure', ''),
 1727: ('Loading Treasure', ''),
 1728: ('Loading Treasure', ''),
 1729: ('', ''),
 1802: ('Loading Treasure', ''),
 1804: ('Loading Note', ''),
 1805: ('Loading Video', ''),
 1806: ('Loading Video', ''),
 1807: ('Loading Video', ''),
 1808: ('Loading Video', ''),
 1809: ('Loading Video', ''),
 1810: ('Loading Video', ''),
 1811: ("Loading Poster", ''),
 1813: ('Loading Recycle Poster', ''),
 1814: ('Loading Recycle Note', ''),
 1815: ("Loading Quest Poster", ''),
 1818: ('Loading Ship Poster', ''),
 1819: ("Loading Dragon Poster", ''),
 1820: ('Loading Poster', ''),
 1821: ("Loading Poster", ''),
 1823: ('Poster', ''),
 1824: ('Loading Note', ''),
 1825: ('Loading Note', ''),
 1826: ("Loading Note", ''),
 1828: ("Loading Note", ''),
 1829: ('Loading Note', ''),
 1830: ('Loading Video', ''),
 1831: ('Loading Moderator', ''),
 1832: ("Loading Timer", ''),
 1833: ('Loading Help', ''),
 1834: ('Loading Coins For Change', ''),
 1835: ('', ''),
 4503: ('Loading Music Menu', ''),
 4504: ('Loading Missions', ''),
 4506: ('Agent Form', ''),
 4508: ('', ''),
 4603: ("Newspaper Form", ''),
 4604: ('Tour Guide Form', ''),
 4605: ("Report Form", ''),
 4606: ('Submission Form', ''),
 4607: ('Loading Library', ''),
 4609: ('Loading Voting Booth', ''),
 4610: ('Loading Art', ''),
 4611: ('Loading Sculpture Plaque', ''),
 4612: ("Loading Sculpture Plaque", ''),
 4614: ('Loading Sculpture Plaque', ''),
 4615: ("Loading Sculpture Plaque", ''),
 4617: ('Loading Sculpture Plaque', ''),
 4618: ('Loading Sculpture Plaque', ''),
 4619: ('Loading Sculpture Plaque', ''),
 4622: ('Loading Sculpture Plaque', ''),
 4623: ('Loading Sculpture Plaque', ''),
 4625: ('Loading Sculpture Plaque', ''),
 4626: ('Notations', ''),
 4628: ('Loading Sculpture Plaque', ''),
 4629: ("Loading Sculpture Plaque", ''),
 4630: ('Loading Sculpture Plaque', ''),
 4631: ('Loading Sculpture Plaque', ''),
 4632: ('Loading Sculpture Plaque', ''),
 4635: ('Loading Treasure Hunt Instructions', ''),
 4637: ('Loading Mancala Instructions', ''),
 4638: ('Loading Card-Jitsu Instructions', ''),
 4639: ('Loading Card-Jitsu Fire Instructions', ''),
 4641: ('Loading Instructions', ''),
 4642: ('Loading Membership', ''),
 4645: ('Loading Membership', ''),
 4646: ('', ''),
 4648: ('Loading Membership', ''),
 4649: ('', ''),
 4652: ('Loading Membership', ''),
 4653: ('', ''),
 4654: ('Loading Membership', ''),
 4655: ("Loading Membership", ''),
 4656: ('', ''),
 4657: ('Loading Membership', ''),
 4658: ('Loading Membership', ''),
 4659: ('', ''),
 4701: ('Loading Membership', ''),
 4702: ('Loading Membership', ''),
 4703: ('Loading Membership', ''),
 4704: ("Loading Membership", ''),
 4705: ('Loading Membership', ''),
 4707: ("Loading Membership", ''),
 4709: ('Loading Membership', ''),
 4710: ('Loading Membership', ''),
 4712: ('Loading Membership', ''),
 4713: ('Loading Membership', ''),
 4716: ('Loading Membership', ''),
 4717: ('Loading Membership', ''),
 4718: ('Loading Membership', ''),
 4719: ('Loading Membership', ''),
 4720: ('Loading Membership', ''),
 4722: ('Loading Membership', ''),
 4723: ('Loading Membership', ''),
 4724: ('Loading Membership', ''),
 4725: ('Loading Membership', ''),
 4727: ('Loading Membership', ''),
 4728: ("Loading Membership", ''),
 4729: ('Loading Membership', ''),
 4730: ('Loading Membership', ''),
 4731: ('Loading Membership', ''),
 4732: ('Loading Membership', ''),
 4733: ('', ''),
 4734: ('', ''),
 4735: ('Loading Membership', ''),
 4736: ('Loading Membership', ''),
 4737: ('Loading Membership', ''),
 4738: ('Loading Membership', ''),
 4739: ('', ''),
 4801: ("Loading Membership", ''),
 4803: ('Loading Membership', ''),
 4804: ('Loading Membership', ''),
 4807: ('Loading Membership', ''),
 4809: ("Loading Membership", ''),
 4812: ('', ''),
 4817: ('Loading Membership', ''),
 4819: ("Loading Membership", ''),
 4820: ('', ''),
 4821: ("Loading Membership", ''),
 4827: ('Loading Membership', ''),
 4828: ("Loading Membership", ''),
 4829: ("January", ''),
 4835: ('February', ''),
 4836: ('March', ''),
 4838: ('April', ''),
 4840: ('May', ''),
 4841: ('June', ''),
 4842: ('July', ''),
 4843: ('', ''),
 4844: ('August', ''),
 4845: ("September", ''),
 4848: ('October', ''),
 4849: ('', ''),
 4850: ('November', ''),
 4852: ('December', ''),
 4853: ("day", ''),
 4854: ("days", ''),
 4855: ('Loading Newspaper', ''),
 4856: ('', ''),
 4862: ("Loading Last Week's Issue", ''),
 4867: ("Loading Old Issue", ''),
 4868: ('', ''),
 4870: ("Loading Old Issue", ''),
 4871: ("Loading Old Issue", ''),
 4872: ("Loading Old Issue", ''),
 4873: ('', ''),
 5501: ('Loading Old Issue', ''),
 5502: (lToonHQ, ''),
 5503: ('Loading Recycle Hunt', ''),
 5505: ('', ''),
 5601: ('Loading Recycle Hunt', ''),
 5602: ("Loading Recycle Hunt", ''),
 5603: ('Loading Recycle Hunt', ''),
 5604: ('Loading Scavenger Hunt', ''),
 5605: ('Loading', ''),
 5606: ('Petals', ''),
 5607: ('SILLY SCAVENGER HUNT', ''),
 5608: ('You have found', ''),
 5609: ('You have foundm piece', ''),
 5610: ("You have foundm eggs", ''),
 5611: ("Claim Prize", ''),
 5613: ('Continue', ''),
 5615: ("Elite Gear", ''),
 5616: ('Field-Ops', ''),
 5617: ("Field-Ops", ''),
 5618: ("Elite Puffle", ''),
 5619: ("Recruit", ''),
 5620: ('Coming Soon', ''),
 5621: ('Objective', ''),
 5622: ('EPF Message', ''),
 5623: ('Congratulations', ''),
 5624: ("Puffle Whistle Message", ''),
 5625: ('Field Op Complete', ''),
 5626: ('Medal Earned!', ''),
 5627: ('', ''),
 5701: ('Messages', ''),
 5702: ("WAIT!", ''),
 5703: ("Do other people use this computer?", ''),
 5704: ('If you save your password here, anyone who uses this computer could access your account.', ''),
 5705: ('Save Password', ''),
 5706: ('Don\'t Save Password', ''),
 5707: ('Learn More', ''),
 5708: ("They could spend your coins!", ''),
 5709: ('They could change your igloo!', ''),
 5710: ('They could get your penguin banned!', ''),
 5711: ('You can\'t store more than 99 of these items.', ''),
 5712: ('percentage', ''),
 5713: ('Puffle Launch', ''),
 5714: ('Loading Christmas Carol', ''),
 5715: ('Penguin is playing Puffle Launch', ''),
 5716: ('Would you like to play Puffle Launch?', ''),
 5717: ('Loading Puffle Launch', ''),
 5718: ('You\'ll need to entermber more Treasure Book code(s) to unlock this page.', ''),
 5719: ('Best Speed', ''),
 5720: ('Normal', ''),
 5721: ('Best Graphics', ''),
 5725: ('Please confirm your parent\'s email address. Club Penguin will send your parent an email with an activation code.', ''),
 5726: ("Use this email", ''),
 5727: ('Change this email', ''),
 5728: ('', ''),
 5802: (lToonHQ, ''),
 5804: ('Please enter your parent\'s valid email address. Club Penguin will send your parent an email with an activation code.', ''),
 5805: ('The email address is not entered correctly.  Please try again.', ''),
 5809: ('There are too many accounts assigned to this email address to add a new one.', ''),
 5810: ('The given domain name is part of our banned email list. Please contact Club Penguin support if you have questions.', ''),
 5811: ('Email is not properly formatted. Please try again.', ''),
 5815: ('An email address cannot contain a \'+\'. Please try again.', ''),
 5817: ('Before you can login, your penguin account must be activated. Ask your parents to check their email.', ''),
 5819: ('An email has been sent to with the next steps to activate your penguin.', ''),
 5821: ('Penguin is on Santa\'s Sled', ''),
 5826: ('Loading Membership', ''),
 5827: ('Loading Catalogue', ''),
 5828: ('Loading Catalogue', ''),
 5830: ('Loading Catalog', ''),
 5833: ('Loading Catalog', ''),
 5835: ('Club Penguin', ''),
 5836: ("Loading Club Penguin", ''),
 5837: ('Penguin is in Club Penguin', ''),
 9501: ('Club Penguin', ''),
 9503: ('Games', ''),
 9504: ('Places', ''),
 9505: (lToonHQ, ''),
 9506: ('Shops', ''),
 9508: ('', ''),
 9601: ('Pets', ''),
 9602: ('Ice Fishing', ''),
 9604: ("Sled Racing", ''),
 9605: ('Jet Pack Adventure', ''),
 9607: ("Hydro Hopper", ''),
 9608: ('Bean Counters', ''),
 9609: ('Arcade', ''),
 9613: ('Dance Contest', ''),
 9616: ('SoundStudio', ''),
 9617: ('Puffle Roundup', ''),
 9619: ('Pizzatron 3000', ''),
 9620: ("Puffle Launch", ''),
 9622: ('Cart Surfer', ''),
 9625: ('Puffle Rescue', ''),
 9626: ('Catchin\' Waves', ''),
 9627: ('Aqua Grabber', ''),
 9628: ('Card-Jitsu', ''),
 9629: ('Penguin Style', ''),
 9630: ('Costume Trunk', ''),
 9631: ('Pet Furniture', ''),
 9633: ('Game Upgrade', ''),
 9634: ('Music Catalog', ''),
 9636: ('Game Upgrade', ''),
 9639: ('Game Upgrade', ''),
 9640: ('Game Upgrade', ''),
 9642: ('Snow and Sports', ''),
 9643: ('Game Upgrade', ''),
 9644: ('Puffle Adoption', ''),
 9645: ('Town', ''),
 9647: ('The Plaza', ''),
 9649: ('The Dock', ''),
 9650: ('Snow Forts', ''),
 9651: ('The Beach', ''),
 9652: ('', ''),
 9703: ('Ski Village', ''),
 9704: ('Ski Hill', ''),
 9705: ('Stadium', ''),
 9706: ('Dojo Courtyard', ''),
 9707: ("Mine", ''),
 9708: ('Forest', ''),
 9709: ('Cove', ''),
 9710: ('Iceberg', ''),
 9711: ('Igloos', ''),
 9712: ("Open Igloos", ''),
 9713: ('0 is not a valid email provider.  Please check the spelling and try again.', ''),
 9714: ('Exclusive Bonus Items', ''),
 9715: ('Congratulations!', ''),
 9716: ('You\'ve entered codes and unlocked the Super Exclusives page, and bonus items of your choice.', ''),
 9717: ("I've got a Code", ''),
 9718: ("I've got a Book", ''),
 9719: ('Unlock your items. Choose an option.', ''),
 9720: ('Enter your code!', ''),
 9721: ('Make sure you enter it exactly as it appears.', ''),
 9722: ('Choose your book from the list below', ''),
 9725: ("Hint: First line starts with the title!", ''),
 9727: ('I\'ve got a code', ''),
 9736: ('View Toys', ''),
 9737: ("Exclusive Treasure Book", ''),
 9738: ('Exclusive Bonus Items', ''),
 9740: ('You\'ve unlocked:', ''),
 9741: ("Play now!", ''),
 9744: ("Enter another code", ''),
 9752: ('To unlock your toy code, you will be logged out of the game.', ''),
 9753: ("Do you want to continue?", ''),
 9754: ('To look at toys, you will be logged out of the game.', ''),
 9755: ('Do you want to continue?', ''),
 9756: ('', ''),
 9759: ('Congratulations!', ''),
 3507: ('These items have been added to your inventory!', ''),
 3508: (lToonHQ, ''),
 3509: ('Bonus item unlocked!', ''),
 3511: ('', ''),
 3601: ('Because you already have [item name], you can now access a bonus Treasure Book item!', ''),
 3602: ("Unlock Bonus Items", ''),
 3605: ('', ''),
 3607: ('0 added to your inventory. You already have the max number of puffles, so you get a bonus item!', ''),
 3608: ('You already have the max number of hats, so you get a bonus item!', ''),
 3610: ("You already have the max number of puffles and hats, so you get 2 bonus items!", ''),
 3611: ("Your and its exclusive have been added to your igloo.", ''),
 3612: ('Give your new puffle a name.', ''),
 3613: ('Enter Penguin Name', ''),
 3614: ('Enter Password', ''),
 3615: ('Next', ''),
 3617: ('Exclusive Bonus Items', ''),
 3618: ('Congratulations!', ''),
 3620: ('You\'ve entered codes and unlocked the Super Exclusives page, and bonus items of your choice.', ''),
 3621: ('I\'ve got a Code', ''),
 3622: ('', ''),
 3623: ('I\'ve got a Book', ''),
 3624: ('Unlock your items. Choose an option.', ''),
 3625: ("Enter your code!", ''),
 3627: ('Make sure you enter it exactly as it appears.', ''),
 3629: ('Choose your book from the list below', ''),
 3630: ('Hint: First line starts with the title!', ''),
 3634: ('I\'ve got a code', ''),
 3635: ('View Toys', ''),
 3636: ('Exclusive Treasure Book', ''),
 3637: ("You can't store more than 75 of this item.", ''),
 3638: ('Drag here to remove', ''),
 3641: ("Loading Treasure Book", ''),
 3642: ('Please name your puffle.', ''),
 3643: ('Congratulations! Your puffle has been added to your igloo.', ''),
 3644: ('needs to eat.', ''),
 3647: ('needs to sleep.', ''),
 3648: ('wants to play.', ''),
 3649: ('Hambrrrgers', ''),
 3650: ('needs a bath.', ''),
 3651: ("Hide Games", ''),
 3653: ('Different colored puffles play different games.', ''),
 3654: ('', ''),
 3702: ('Puffle Care', ''),
 3703: ('', ''),
 3705: ('Show Games', ''),
 3706: ("Walk your puffle to its favorite game to play it.", ''),
 3707: ('Buy more food from', ''),
 3708: ("next", ''),
 3710: ('G\'Day!', ''),
 3711: ('', ''),
 3712: ('I\'m here to show you how to care for your puffles!', ''),
 3713: ('Click these tabs to:', ''),
 3715: ("feed", ''),
 3716: ('play', ''),
 3717: ('clean', ''),
 3718: ('rest', ''),
 3719: ('When you run out of food,', ''),
 3721: ("click this catalog to buy more.", ''),
 3722: ('Have fun,', ''),
 3723: ("and good luck!", ''),
 3724: ('and dress your puffle.', ''),
 3725: ('done', ''),
 3726: ('Walk your puffle to its favorite game to play it.', ''),
 3728: ('YOUR COINS', ''),
 3729: ('', ''),
 3730: ('Your puffle\'s stats tell you when it is happy, sad, hungry, tired or messy.', ''),
 3731: ('Give them snacks, toys, baths, and sleep to fill their stats.', ''),
 3732: ('Go to Pet Papers to view', ''),
 3734: ('your Adoption Certificates.', ''),
 3735: ('Take your puffle for a walk and care for it at the Puffle Hotel!', ''),
 3736: ('Care', ''),
 3737: ('Adoption Certificate', ''),
 3738: ("Feed", ''),
 3739: ('', ''),
 3801: ('Puffle Handbook', ''),
 3806: ('Play', ''),
 3807: ('Pet Papers', ''),
 3808: ('Care', ''),
 3809: ('Groom', ''),
 3810: ('Sleep', ''),
 3811: ('Dress Up', ''),
 3812: ('Pet Stats', ''),
 3813: ("Play", ''),
 3814: ('needs to eat.', ''),
 3815: ('needs to sleep.', ''),
 3816: ('wants to play.', ''),
 3817: ('needs a bath.', ''),
 3818: ('Hide Games', ''),
 3819: ('Different colored puffles play different games', ''),
 3820: ('Puffle Care', ''),
 3821: ('Show Games', ''),
 3823: ('Walk your puffle to its favorite game to play it.', ''),
 3824: ('Buy more food from', ''),
 3825: ('next', ''),
 3826: ('G\'Day', ''),
 3827: ('Im here to show you how to care for your puffles!', ''),
 3828: ("Click these tabs to:", ''),
 3829: ('feed', ''),
 3830: ('play', '')}
ClosetTimeoutMessage = 'clean'
ClosetNotOwnerMessage = "rest"
ClosetPopupOK = lOK
ClosetPopupCancel = lCancel
ClosetDiscardButton = 'Remove'
ClosetAreYouSureMessage = 'When you run out of food,'
ClosetYes = lYes
ClosetNo = lNo
ClosetVerifyDelete = 'Really delete %s?'
ClosetShirt = 'click this catalog to buy more.'
ClosetShorts = 'Have fun,'
ClosetSkirt = 'and good luck!'
ClosetDeleteShirt = 'Delete\nshirt'
ClosetDeleteShorts = 'Delete\nshorts'
ClosetDeleteSkirt = 'Delete\nskirt'
TrunkNotOwnerMessage = "Loading Yearbook 10/11"
TrunkNotPaidMessage = 'and dress your puffle.'
TrunkAreYouSureMessage = 'done'
TrunkHat = 'Easter Egg Scavenger Hunt'
TrunkGlasses = 'Claim Prize'
TrunkBackpack = 'Continue'
TrunkShoes = 'num ghosts caught'
TrunkDeleteHat = 'Delete\nhat'
TrunkDeleteGlasses = 'Delete\nglasses'
TrunkDeleteBackpack = 'num eggs found'
TrunkDeleteShoes = 'Delete\nshoes'
EstateOwnerLeftMessage = "Sorry, the owner of this estate left.  You'll be sent to the playground in %s seconds"
EstatePopupOK = lOK
EstateTeleportFailed = "The first egg's hid near shining gold, Somewhere deep and dark and cold."
EstateTeleportFailedNotFriends = "Sorry, %s is in a toon's estate that you are not friends with."
EstateTargetGameStart = 'The next egg\'s found near works of art, Plus lots of books to make you smart!'
EstateTargetGameInst = "This next egg's near a snowy shore. It's hidden well. You must explore."
EstateTargetGameEnd = 'Now head towards a wooden shack. You\'re doing well, you\'re right on track!'
AvatarsHouse = '%s\n House'
BankGuiCancel = lCancel
BankGuiOk = lOK
DistributedBankNoOwner = 'Search now near a tall white chair, For watching waves. The egg is there.'
DistributedBankNotOwner = 'The next one\'s sure to make you smile. Just like you, this egg\'s got style.'
FishGuiCancel = lCancel
FishGuiOk = 'The next egg\'s near a chair that lifts. You\'re getting close, you must be swift!'
FishTankValue = 'Hi, %(name)s! You have %(num)s fish in your bucket worth a total of %(value)s jellybeans. Do you want to sell them all?'
FlowerGuiCancel = lCancel
FlowerGuiOk = 'The last egg\'s near a big, bright light. You\'re almost done, the end\'s in sight.'
FlowerBasketValue = '%(name)s, you have %(num)s flowers in your basket worth a total of %(value)s jellybeans. Do you want to sell them all?'

def GetPossesive(name):
    if name[-1:] == 's':
        possesive = name + "'"
    else:
        possesive = name + "'s"
    return possesive


PetTrait2descriptions = {'hungerThreshold': ('Go to settings to remove players on your ignore list.',
                     'Would you like to addme',
                     'to your Friends list?',
                     'Would you like to removeme from your Friends list?'),
 'Remove Friend': ('Add Friend',
                      'Show Friends',
                      'Remove Friend',
                      'Loading Pufflescape'),
 'angerThreshold': ('Penguin is playing Pufflescape',
                    'Pufflescape',
                    'Would you like to play Pufflescape?',
                    'Loading Membership'),
 'forgetfulness': ('Sorry, you may only have four Card-Jitsu Mat igloo items.',
                   'Card-Jitsu All Access ends Dec. 6. A membership will be required to play.',
                   'Would you like to play',
                   'Card-Jitsu Fire?'),
 'Card-Jitsu Water?': ('Would you like to play',
                         'Would you like to play',
                         'Card-Jitsu?',
                         'Earn Your Fire Suit'),
 'Earn Your Belts': ('Earn Your Water Suit',
                      'Penguin is now offline',
                      'Loading the Ninja Hideout',
                      'Loading the Dojo Courtyard'),
 '250 coins were added to your account': ('100 coins were added to your account',
                           '500 coins were added to your account',
                           'Mom and Dad',
                           'Dad'),
 'Pufflescape': ('Mom',
                          'Ok',
                          'Cancel',
                          'Please enter your parent\'s valid email address. Club Penguin will send your parent an email with an activation code.'),
 'Club Penguin Rules': ('Loading Poster',
                         'Loading CFC Poster',
                         'CFC Poster',
                         'Loading Advent Note'),
 'Loading Advent Note': ('Loading Advent Note',
                      'Loading Advent Note',
                      'Loading Advent Note',
                      'Loading Advent Note'),
 'Loading Advent Note': ('Loading Advent Note',
                        'Loading Advent Note',
                        'Loading Advent Note',
                        'Loading Advent Note'),
 'Party 1': ('Loading Advent Note',
                       'Loading Poster',
                       'Loading Note',
                       'Loading Catalog'),
 'Attempted Game Manipulation': ('You already have the max number of puffles, so you get a bonus item!',
                        'You\'ve used up your time to play on Club Penguin for today. Your parent has set your play time to,.',
                        'You have left to play Club Penguin today. Your parent has set your play time to,.',
                        'minute')}
FireworksInstructions = lToonHQ + 'minutes'
startFireworksResponse = "Usage: startFireworksShow ['num']\n                                         'num' = %s - New Years\n                                         %s - Party Summer \n                                         %s - 4th of July"
FireworksJuly4Beginning = lToonHQ + 'hour'
FireworksJuly4Ending = lToonHQ + 'hours'
FireworksNewYearsEveBeginning = lToonHQ + 'Choose Your'
FireworksNewYearsEveEnding = lToonHQ + 'Puffle'
FireworksComboBeginning = lToonHQ + 'PH'
FireworksComboEnding = lToonHQ + 'Your parent has changed your play time on Club Penguin to  ,.'
BlockerTitle = 'Sorry, you can only buy this item 99 times.'
BlockerLoadingTexts = ['Scrubbing pie tins',
 'Party 5',
 'Party 6',
 'Party 7',
 'Party 8',
 'You\'ve Been Hit!',
 'by from the Club Penguin App',
 'Would you like to throw one back?',
 'You\'ve thrown a snowball back at',
 "You've Been Hit!",
 'Throw snowballs back?',
 'Snowballs thrown at!',
 'Your parent has changed your play time on Club Penguin to  ,.',
 "Are you prepared for battle?",
 'Your current igloo',
 'Edit',
 'Igloo Visitors',
 'Friends',
 'Everyone',
 'Are you sure that you want to delete this igloo?',
 'Music',
 'Hide',
 'Show',
 'My Saved Tracks',
 'Igloo Music',
 'Go to DJ3K!',
 "Song Not Playing",
 'Go There!',
 'Record and save your',
 'own music mixes in DJ3K.',
 'Use arrow keys to change this item.',
 'Are you sure you want to add an igloo? Your flooring and igloo furniture will be saved in your inventory.']
TIP_NONE = 0
TIP_GENERAL = 1
TIP_STREET = 2
TIP_MINIGAME = 3
TIP_COGHQ = 4
TIP_ESTATE = 5
TIP_KARTING = 6
TIP_GOLF = 7
TipTitle = 'Are you sure you want to move your igloo? Your flooring and igloo furniture will be saved in your inventory.'
TipDict = {TIP_NONE: ('',),
 TIP_GENERAL: ('Are you sure you want to remove your igloo? Your flooring and igloo furniture will be saved in your inventory.',
               'Popular',
               'Friends',
               'Everyone',
               'Likes',
               'You will lose all your LIKES for this igloo.',
               'OK',
               'OK',
               "OK",
               'Calling all heroes! Super Villains have been spotted at the Bank!',
               'Fires reported downtown! The city needs a hero!',
               'The police could use some back-up! Go to the Jail!',
               'Heroes - gather forces at the Super Hero HQ. For great justice!',
               'It\'s time to defeat evil once and for all! To the Super Villain Lair!',
               'Press Conference at the Coffee Shop. The city wants answers!',
               'Giant monsters spotted at the Iceberg! Move out!',
               'Defend the Club Penguin Times at any cost!',
               'The Bank vault is defenseless! You know what to do...',
               'Villains - join forces downtown. Nothing can stop us!',
               'All Super Villains, go to the Jail! Cause trouble, but don\'t get caught!',
               'The Super Heroes think their HQ is safe...',
               'Attention Villains! Meet up at the Lair for an evil planning session!',
               'No Super Villains allowed at the Coffee Shop. Wear a disguise. They\'ll never know it\'s you!',
               'Giant monsters, your time has come... to the Iceberg!',
               'Shut down the presses at the Club Penguin Times! First the newspaper... then the world!',
               'Super powered penguins spotted at the Bank! Also pizza!',
               'Fires reported downtown. Please expect traffic delays.',
               'Watch out for villains escaping the Jail! They ALWAYS do that!',
               'Super Villains have been spotted heading to the Super Hero HQ!',
               'Super Heroes reported heading to the Super Villain Lair!',
               'Fresh coffee reported at the Coffee Shop! Also Super Heroes and Super Villains!',
               'Giant monsters spotted at the Iceberg! Run!',
               'Super Heroes and Villains spotted at the Club Penguin Times!',
               'Non-member trying to enter fort',
               'Grand Total Likes:',
               'Buy more wall items from the Furniture Catalog',
               'Buy more pet furniture from the Puffle Catalog in the Pet Shop',
               'Martial Artworks',
               'Buy more furniture from the Furniture Catalog',
               'Buy more flooring from the Furniture Catalog',
               'Buy more igloos from the Igloo Catalog',
               'Feb',
               'Mar',
               'Apr',
               'May',
               'Jun',
               'Jul',
               'Aug',
               'Sept',
               "Oct",
               'Nov',
               'Dec',
               'Jan'),
 TIP_STREET: ('OK!',
              'OK!',
              'OK!',
              'Calling all heroes! Super Villains have been spotted at the Bank!',
              'Fires reported downtown! The city needs a hero!',
              'The police could use some back-up! Go to the Jail!',
              'Heroes - gather forces at the Super Hero HQ. For great justice!',
              'It\'s time to defeat evil once and for all! To the Super Villain Lair!',
              'Press Conference at the Coffee Shop. The city wants answers!',
              'Giant monsters spotted at the Iceberg! Move out!',
              'Defend the Club Penguin Times at any cost!',
              'The Bank vault is defenseless! You know what to do...',
              'Villains - join forces downtown. Nothing can stop us!',
              'All Super Villains, go to the Jail! Cause trouble, but don\'t get caught!',
              'The Super Heroes think their HQ is safe...',
              'Attention Villains! Meet up at the Lair for an evil planning session!',
              'No Super Villains allowed at the Coffee Shop. Wear a disguise. They\'ll never know it\'s you!',
              'Giant monsters, your time has come... to the Iceberg!',
              'Shut down the presses at the Club Penguin Times! First the newspaper... then the world!',
              'Super powered penguins spotted at the Bank! Also pizza!',
              'Fires reported downtown. Please expect traffic delays.',
              'Watch out for villains escaping the Jail! They ALWAYS do that!',
              'Super Villains have been spotted heading to the Super Hero HQ!',
              'Super Heroes reported heading to the Super Villain Lair!',
              'Fresh coffee reported at the Coffee Shop! Also Super Heroes and Super Villains!',
              'Giant monsters spotted at the Iceberg! Run!',
              'Super Heroes and Villains spotted at the Club Penguin Times!',
              'You already have this location.',
              'Grand Total Likes',
              'Anonymous',
              'Create a Penguin',
              'Learn more about Membership',
              'Scorn Battle',
              'Penguin is in an epic battle!',
              'Smoothie Smash',
              'Would you like to play Smoothie Smash?',
              'Penguin is making smoothies.'),
 TIP_MINIGAME: ('You\'ve unlocked items!',
                'We\'ve added them to your inventory.',
                'There are fruit items left to unlock.',
                'You\'ve unlocked all the fruit items.',
                'Unlock your bonus item now!',
                'Pineapple Igloo Unlocked!',
                'We\'ve added them to your inventory.' + lToontownCentral + 'You\'ve unlocked more items!' + lDonaldsDreamland + 'You\'ve unlocked all fruit items and earned the bonus Pineapple Igloo!',
                'Unlock Bonus Item'),
 TIP_COGHQ: ('Make Smoothies',
             'Party 3',
             'Party 4',
             'Access Security Terminal?',
             'Login to play!',
             'OR',
             'Create',
             'Cloud Forest',
             'Penguin is in the Cloud Forest',
             'Hotel Lobby',
             'Penguin is in the Hotel Lobby',
             'Hotel Spa',
             'Penguin is in the Hotel Spa',
             'Hotel Rooftop',
             'Penguin is in the Hotel Rooftop',
             'This rainbow puffle has chosen you!',
             'Choose a name',
             'Adopt',
             'Rainbow',
             'These majestic puffles enjoy the',
             'fantastical. They may be the only',
             'creature to have seen a real unicorn.',
             'Confident, regal',
             'Cloud',
             'Rainbow lollipop' + Foreman + 'Cloud surfing and riding down rainbows',
             "Farts sparkles",
             'Rainbow Quest',
             '10 coins were added to your account',
             '1000 coins were added to your account',
             "20 coins were added to your account"),
 TIP_ESTATE: ('50 coins were added to your account',
              'Penguin is in the Hotel Spa',
              "Penguin is on the Hotel Roof",
              'Hotel Lobby',
              "Hotel Spa",
              'Hotel Rooftop',
              'Mute All Sounds',
              'You already have the max number of puffles. All other items have been added to your inventory.',
              'Would you like to buy 3 Power Cards forst coins?',
              'My Progress',
              'My progress',
              'Go back',
              'Next Reward',
              'Talk to Sensei to begin your Ninja journey.',
              'Become a Fire Ninja. Discover the power of the flame.',
              "Become a Water Ninja. Discover the power of the wave.",
              'Become a Snow Ninja. Discover the power of the flurry.',
              'Well done! Challenge Sensei to earn your Ninja Mask!',
              "Excellent! Challenge Sensei to become a Fire Ninja!",
              "Impressive skills! Challenge Sensei to become a Water Ninja!",
              'Ninja!',
              'Fire Ninja!',
              'Water Ninja!',
              'Snow Ninja!',
              'My Cards',
              "I've got a Code",
              "Card-Jitsu Saga",
              "Unite with ninjas in Card-Jitsu Snow battle to unlock",
              'Long, Long Ago�',
              'Training Begins',
              'Snow Match',
              'Counter Strike',
              'Battle Snow Minions',
              'Blasted Back',
              'The Earth Quivered�',
              'A Broken Tusk',
              'Challenge Tusk'),
 TIP_KARTING: ("Tusk's Vow",
               "Tusk Defeated",
               'Redeeming Codes',
               "To unlock a card code, you will be logged out of the game. Do you want to continue?",
               'Not�now',
               'Log out to redeem',
               'Spy Drills',
               'Would you like to play Spy Drills?',
               'Loading Spy Drills',
               'Penguin is in the Robot Factory',
               'These 3 Power Cards have been added to your inventory.'),
 TIP_GOLF: ('Would you like to play', 'Snow Dojo', 'Penguin is in the Snow Dojo')}
FishGenusNames = {0: 'Card-Jitsu Snow?',
 2: 'Snow Gem',
 4: 'Your coins:',
 6: '0',
 8: 'Your puffles:',
 10: 'Puffles for everyone',
 12: 'Quest for a Rainbow Puffle',
 14: 'Go to the Puffle Hotel',
 16: 'Complete all four tasks in the Puffle Care Quest',
 18: 'Launch into the Cloud Forest to meet their new pet!',
 20: 'Learn More About Membership',
 22: 'Go to Puffle Hotel',
 24: 'pufflename found',
 26: 'Everyone\'s puffles can dig up coins!',
 28: '0 found coins!',
 30: '0 was added to your inventory!',
 32: 'Send your puffle back to the wilds',
 34: 'Treasure'}
FishSpeciesNames = {0: ('Games',
     'Taking some puffles into games can help you earn more coins!',
     'Click your puffle\'s leash to take it for a walk.',
     'To send it back to your igloo, open your player card and click your puffle.',
     'Penguin is playing Card-Jitsu Snow'),
 2: ('Puffle Treasure',
     'Members can walk puffles for the chance to find rare items.',
     'Penguin is learning how to scare',
     'Penguin is in the University',
     'About Membership'),
 4: ('Clear Igloo',
     'Are you sure you want to clear this player\'s igloo?',
     'A Moderator has cleared your igloo because it was inappropriate.',
     'Please remember to follow the Club Penguin rules.'),
 6: ('Oops! You used a rude or inappropriate word.',),
 8: ('If you break a Club Penguin rule again, you may be banned.',
     'A Moderator removed you from this server.',
     'Please remember to follow the Club Penguin rules.',
     'You used a rude or inappropriate word.',
     'This penguin account has been banned for hours.'),
 10: ('You were caught cheating.',),
 12: ('BANNED',
      'Club Penguin Rules',
      'Respect others',
      'No bullying or being mean to others',
      'Chat nicely'),
 14: ('Stay safe online', 'No rude or inappropriate language'),
 16: ('No cheating or use of third party programs', 'Play fair', 'No sharing personal information'),
 18: ('Buy Power Cards', 'Population', 'Rules'),
 20: ('Members Only',
      '(0 ban)',
      '(0 bans)',
      'Ban for saying',
      'Bullying',
      'Inappropriate words'),
 22: ('Shared personal info',
      'Cheating',
      'Warning only',
      '24 hrs'),
 24: ('72 hrs',
      'Permanently',
      'BAN!',
      'Notes:'),
 26: ('Comments are saved on player\'s record',
      'WARNED',
      'Warn again',
      'You were disrespectful to others.',
      'You shared personal information.',
      'This penguin has been permanently banned for repeatedly not following the Club Penguin rules.',
      'You�ve used up your time to play today. Your parent has set your play time to -',
      'You have left to play on Club Penguin today. Your parent has set your play time to -'),
 28: ('Will you take up the challenge?', 'Become an agent and help protect Club Penguin.', '0, the island needs you.'),
 30: ('Welcome to the Elite Penguin Force Agent (0).',
      'Here\'s your spy phone - your most important tool.',
      'Keep it on you to receive your orders.',
      'Very well. Carry on.',
      'If you change your mind, give us a call.'),
 32: ('Add phone',
      'The Director',
      'We look forward to working with you, agent.',
      'Enter the Command Room to hone your skills.',
      'And good luck.'),
 34: ('OK',)}
CogPartNames = ('Favorite Foods',
 'Members can walk their puffles for the chance to find their favorite food.',
 'Feed your puffle their favorite snack and their stats will go up to 100!',
 'Fish Burger',
 'Pretzels',
 'Astronaut',
 'Ice Cream',
 'Tacos',
 'Chest',
 'Socks',
 'Pelvis',
 'Watermelon',
 'Hummus',
 'and Pita',
 'Rainbow',
 'Lollipop',
 'Stinky')
CogPartNamesSimple = ('Cheese',)
SellbotLegFactorySpecMainEntrance = 'Yogurt Parfait'
SellbotLegFactorySpecLobby = 'Lobby'
SellbotLegFactorySpecLobbyHallway = 'Popcorn'
SellbotLegFactorySpecGearRoom = 'Puffle Treasure Hunting'
SellbotLegFactorySpecBoilerRoom = 'Take good care'
SellbotLegFactorySpecEastCatwalk = 'of your pet!'
SellbotLegFactorySpecPaintMixer = 'Healthy puffles can'
SellbotLegFactorySpecPaintMixerStorageRoom = 'dig up more coins.'
SellbotLegFactorySpecWestSiloCatwalk = 'Take a break'
SellbotLegFactorySpecPipeRoom = 'while walking.'
SellbotLegFactorySpecDuctRoom = 'Puffles can hunt for'
SellbotLegFactorySpecSideEntrance = 'treasure when you stop.'
SellbotLegFactorySpecStomperAlley = 'If your puffle finds'
SellbotLegFactorySpecLavaRoomFoyer = 'treasure, it\'ll start digging.'
SellbotLegFactorySpecLavaRoom = 'If not, try another spot.'
SellbotLegFactorySpecLavaStorageRoom = 'OK'
SellbotLegFactorySpecWestCatwalk = 'on'
SellbotLegFactorySpecOilRoom = 'the'
SellbotLegFactorySpecLookout = 'Lookout'
SellbotLegFactorySpecWarehouse = 'Warehouse'
SellbotLegFactorySpecOilRoomHallway = 'MENU'
SellbotLegFactorySpecEastSiloControlRoom = 'Walk your puffle to feed it at the'
SellbotLegFactorySpecWestSiloControlRoom = 'Snack Stations!'
SellbotLegFactorySpecCenterSiloControlRoom = 'Uh-oh!'
SellbotLegFactorySpecEastSilo = 'You\'ll need more coins'
SellbotLegFactorySpecWestSilo = 'to get this item.'
SellbotLegFactorySpecCenterSilo = 'Earn more coins by'
SellbotLegFactorySpecEastSiloCatwalk = 'Playing games'
SellbotLegFactorySpecWestElevatorShaft = 'Walking your puffle'
SellbotLegFactorySpecEastElevatorShaft = 'Go There!'
FishBingoBingo = 'BINGO!'
FishBingoVictory = 'VICTORY!!'
FishBingoJackpot = 'JACKPOT!'
FishBingoGameOver = 'OK'
FishBingoIntermission = 'You\'ll need more coins'
FishBingoNextGame = 'to send this postcard.'
FishBingoTypeNormal = 'Classic'
FishBingoTypeCorners = 'Gold'
FishBingoTypeDiagonal = 'Diagonals'
FishBingoTypeThreeway = 'The legendary gold puffles live near'
FishBingoTypeBlockout = 'BLOCKOUT!'
FishBingoStart = "gold deposits in the earth's crust. They"
FishBingoOngoing = 'are known to dig up rare golden items.'
FishBingoEnd = 'Lucky, energetic'
FishBingoHelpMain = 'Jackhammer'
FishBingoHelpFlash = 'Distracted by golden objects'
FishBingoHelpNormal = 'Chocolate coins'
FishBingoHelpDiagonals = 'Hide-and-Seek'
FishBingoHelpCorners = 'Champion'
FishBingoHelpThreeway = "Chocolate"
FishBingoHelpBingo = 'Bingo!'
FishBingoHelpBlockout = 'Coins'
FishBingoOfferToSellFish = 'Oops!'
FishBingoJackpotWin = 'Win %s jellybeans!'
ResistanceToonupMenu = 'Toon-up'
ResistanceToonupItem = '%s Toon-up'
ResistanceToonupItemMax = 'Max'
ResistanceToonupChat = 'left to activate your account. Unactivated accounts will be deleted.'
ResistanceRestockMenu = 'Gag-up'
ResistanceRestockItem = 'Gag-up %s'
ResistanceRestockItemAll = 'All'
ResistanceRestockChat = 'Your parent needs to activate your account so you can keep playing. Ask them to check their email for the activation link.'
ResistanceMoneyMenu = 'jellybeans'
ResistanceMoneyItem = '%s jellybeans'
ResistanceMoneyChat = 'Didn\'t get an email?'
ResistanceEmote1 = NPCToonNames[9228] + 'OK'
ResistanceEmote2 = NPCToonNames[9228] + 'Welcome to Club Penguin!'
ResistanceEmote3 = NPCToonNames[9228] + 'You can waddle around without activating for'
KartUIExit = 'Ask your parent to check their email.'
KartShop_Cancel = lCancel
KartShop_BuyKart = 'after the trial period, unactivated accounts will be deleted.'
KartShop_BuyAccessories = 'Welcome back!'
KartShop_BuyAccessory = 'You can waddle around without activating for'
KartShop_Cost = 'Cost: %d Tickets'
KartShop_ConfirmBuy = 'Buy the %s for %d Tickets?'
KartShop_NoAvailableAcc = 'Activate account to enable chat.'
KartShop_FullTrunk = 'Dig up gold nuggets!'
KartShop_ConfirmReturnKart = 'You can dig for gold nuggets until you log off. Any gold nuggets you collect will be saved.'
KartShop_ConfirmBoughtTitle = 'Take the gold nuggets to the Gold Mine to activate the jackhammer.'
KartShop_NotEnoughTickets = 'Go There!'
KartView_Rotate = 'Rotate'
KartView_Right = 'Right'
KartView_Left = 'Left'
StartingBlock_NotEnoughTickets = "Insert coins below to feed"
StartingBlock_NoBoard = 'your puffle a gold O\'berry'
StartingBlock_NoKart = 'Walk your puffle anywhere to dig up gold nuggets.'
StartingBlock_Occupied = 'Bring the gold nuggets to the Gold Mine'
StartingBlock_TrackClosed = 'to activate the jackhammer!'
StartingBlock_EnterPractice = 'You already have the'
StartingBlock_EnterNonPractice = 'Would you like to enter a %s race for %s tickets?'
StartingBlock_EnterShowPad = 'max number of puffles.'
StartingBlock_KickSoloRacer = 'Walk your puffle here'
StartingBlock_Loading = 'to feed it a gold O\'berry!'
LeaderBoard_Time = 'Time'
LeaderBoard_Name = 'Your Coins:'
LeaderBoard_Daily = 'INSERT'
LeaderBoard_Weekly = '0 found 1 gold nugget!'
LeaderBoard_AllTime = '0 found gold nuggets!'
RecordPeriodStrings = [LeaderBoard_Daily, LeaderBoard_Weekly, LeaderBoard_AllTime]
KartRace_RaceNames = ['Practice', 'Toon Battle', 'Grand Prix']
from toontown.racing import RaceGlobals
KartRace_Go = 'Go!'
KartRace_Reverse = ' Rev'
KartRace_TrackNames = {RaceGlobals.RT_Speedway_1: 'Gold Puffle Quest',
 RaceGlobals.RT_Speedway_1_rev: 'You need more gold nuggets' + KartRace_Reverse,
 RaceGlobals.RT_Rural_1: 'to activate the jackhammer.',
 RaceGlobals.RT_Rural_1_rev: 'Go to the Pet Shop with' + KartRace_Reverse,
 RaceGlobals.RT_Urban_1: 'a puffle to start your quest.',
 RaceGlobals.RT_Urban_1_rev: 'You already own the maximum' + KartRace_Reverse,
 RaceGlobals.RT_Speedway_2: 'number of puffles!',
 RaceGlobals.RT_Speedway_2_rev: 'You found' + KartRace_Reverse,
 RaceGlobals.RT_Rural_2: 'a gold puffle!',
 RaceGlobals.RT_Rural_2_rev: 'Congratulations!' + KartRace_Reverse,
 RaceGlobals.RT_Urban_2: 'Your new puffle comes with its very own',
 RaceGlobals.RT_Urban_2_rev: 'adoption certificate and exclusive toy.' + KartRace_Reverse}
KartRace_Unraced = 'N/A'
KartDNA_KartNames = {0: 'Cruiser',
 1: 'Roadster',
 2: 'Adoption'}
KartDNA_AccNames = {1000: 'Certificate',
 1001: 'Toy',
 1002: 'Members can:',
 1003: 'Feed your puffle a gold',
 1004: 'O\'berry to begin your quest.',
 1005: 'Learn More',
 1006: 'About Membership',
 1007: 'OK',
 1008: 'Resend activation email to',
 1009: 'Parent email address',
 1010: 'Send Email',
 2000: 'Re-send email',
 2001: 'Change email',
 2002: 'You can waddle around without activating for more hours.',
 2003: 'You have one more hour to play without activating.',
 2004: 'By activating your account you can keep exploring, chatting, adding friends, and more!',
 2005: 'You have less than one hour to activate your account. Unactivated accounts will be deleted.',
 2006: '0',
 2007: 'days',
 2008: 'sp9',
 2009: 'sp10',
 3000: '0',
 3001: "hour(s)",
 3002: 'An activation link was sent to',
 3003: 'Resend activation email to',
 3004: 'Adding an igloo requires',
 3005: 'a paid membership',
 3006: 'Members can:',
 3007: 'Save more unique igloo designs',
 3008: 'fw9',
 3009: 'fw10',
 4000: 'Decorate their perfect igloo with the latest furniture',
 4001: 'Unlock their igloos and throw parties for their friends',
 4002: 'About Membership',
 4003: 'Adopting more than two puffles',
 4004: 'requires a paid membership',
 4005: 'Members can:',
 4006: 'Adopt a pet puffle in every color',
 4007: 'Care for up to 75 puffles',
 4008: 'Buy special toys and furnitur items for their pets',
 4009: 'About Membership',
 4010: 'This requires a paid membership',
 4011: 'Members can:',
 4012: 'Buy new clothing styles every month',
 5000: 'Turbo',
 5001: 'Moon',
 5002: 'Patched',
 5003: 'Design their own clothes',
 5004: 'Wear the latest party outfits',
 5005: 'Heart',
 5006: 'Mickey',
 5007: 'About Membership',
 5008: 'Daisy',
 5009: 'Basketball',
 5010: 'Hypno',
 5011: 'Tribal',
 5012: 'Gemstone',
 5013: 'Stage Costumes require',
 5014: 'Knockoff',
 6000: 'a paid membership',
 6001: 'Splatter',
 6002: 'Checkerboard',
 6003: 'Flames',
 6004: 'Hearts',
 6005: 'Bubbles',
 6006: 'Tiger',
 6007: 'Flowers',
 6008: 'Lightning',
 6009: 'Angel',
 7000: 'Chartreuse',
 7001: 'Peach',
 7002: 'Members can:',
 7003: 'Red',
 7004: 'Maroon',
 7005: 'Sienna',
 7006: 'Brown',
 7007: 'Tan',
 7008: 'Coral',
 7009: 'Orange',
 7010: 'Yellow',
 7011: 'Cream',
 7012: 'Citrine',
 7013: 'Lime',
 7014: 'Purchase costumes to wear everywhere',
 7015: 'Green',
 7016: 'Dress up and act on the Stage',
 7017: 'Aqua',
 7018: 'Blue',
 7019: 'Periwinkle',
 7020: 'Change their looks with the latest styles',
 7021: 'About Membership',
 7022: 'Purple',
 7023: 'Lavender',
 7024: 'Pink',
 7025: 'Plum',
 7026: 'Black'}
RaceHoodSpeedway = 'Speedway'
RaceHoodRural = 'Rural'
RaceHoodUrban = 'Urban'
RaceTypeCircuit = 'Tournament'
RaceQualified = 'qualified'
RaceSwept = 'swept'
RaceWon = 'won'
Race = 'race'
Races = 'races'
Total = 'total'
GrandTouring = 'Igloo Upgrades require a'

def getTrackGenreString(genreId):
    genreStrings = ['Speedway', 'Country', 'City']
    return genreStrings[genreId].lower()


def getTunnelSignName(trackId, padId):
    if trackId == 2 and padId == 0:
        return 'tunne1l_citysign'
    elif trackId == 1 and padId == 0:
        return 'tunnel_countrysign1'
    else:
        genreId = RaceGlobals.getTrackGenre(trackId)
        return 'tunnel%s_%ssign' % (padId + 1, RaceGlobals.getTrackGenreString(genreId))


KartTrophyDescriptions = [str(RaceGlobals.QualifiedRaces[0]) + ' ' + RaceHoodSpeedway + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[1]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[2]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[0]) + ' ' + RaceHoodRural + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[1]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[2]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[0]) + ' ' + RaceHoodUrban + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[1]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[2]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.TotalQualifiedRaces) + ' ' + Total + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.WonRaces[0]) + ' ' + RaceHoodSpeedway + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[1]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[2]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[0]) + ' ' + RaceHoodRural + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[1]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[2]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[0]) + ' ' + RaceHoodUrban + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[1]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[2]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.TotalWonRaces) + ' ' + Total + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.WonCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.WonCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.WonCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.SweptCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceSwept,
 str(RaceGlobals.SweptCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceSwept,
 str(RaceGlobals.SweptCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceSwept,
 GrandTouring,
 str(RaceGlobals.TrophiesPerCup) + 'paid membership',
 str(RaceGlobals.TrophiesPerCup * 2) + 'Members can:',
 str(RaceGlobals.TrophiesPerCup * 3) + 'Upgrade to the latest igloos']
KartRace_TitleInfo = 'Customize the flooring in their igloo'
KartRace_SSInfo = 'Decorate their igloo with furniture items'
KartRace_CoCoInfo = 'About Membership'
KartRace_RRInfo = 'Igloo Furniture and Items'
KartRace_AAInfo = 'require a paid membership'
KartRace_CCInfo = 'Members can:'
KartRace_BBInfo = 'Purchase furniture for their igloo'
KartRace_GeneralInfo = 'Design custom furniture for their igloo'
KartRace_TrackInfo = {RaceGlobals.RT_Speedway_1: KartRace_SSInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Speedway_1_rev: KartRace_SSInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Speedway_2: KartRace_CoCoInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Speedway_2_rev: KartRace_CoCoInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_1: KartRace_RRInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_1_rev: KartRace_RRInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_2: KartRace_AAInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_2_rev: KartRace_AAInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_1: KartRace_CCInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_1_rev: KartRace_CCInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_2: KartRace_BBInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_2_rev: KartRace_BBInfo + KartRace_GeneralInfo}
KartRecordStrings = {RaceGlobals.Daily: 'daily',
 RaceGlobals.Weekly: 'weekly',
 RaceGlobals.AllTime: 'Decorate their igloo any way they want'}
KartRace_FirstSuffix = 'st'
KartRace_SecondSuffix = '    nd'
KartRace_ThirdSuffix = '  rd'
KartRace_FourthSuffix = '   th'
KartRace_WrongWay = 'Wrong\nWay!'
KartRace_LapText = 'Lap %s'
KartRace_FinalLapText = 'About Membership'
KartRace_Exit = 'Instruments from the Music Catalog'
KartRace_NextRace = 'require a paid membership'
KartRace_Leave = 'About Membership'
KartRace_Qualified = 'Qualified!'
KartRace_Record = 'Record!'
KartRace_RecordString = 'You have set a new %s record for %s! Your bonus is %s tickets.'
KartRace_Tickets = 'Tickets'
KartRace_Exclamations = '!'
KartRace_Deposit = 'Deposit'
KartRace_Winnings = 'Winnings'
KartRace_Bonus = 'Bonus'
KartRace_RaceTotal = 'Ninja items require'
KartRace_CircuitTotal = 'a paid membership'
KartRace_Trophies = 'Trophies'
KartRace_Zero = '0'
KartRace_Colon = ':'
KartRace_TicketPhrase = '%s ' + KartRace_Tickets
KartRace_DepositPhrase = KartRace_Deposit + KartRace_Colon + '\n'
KartRace_QualifyPhrase = 'Qualify:\n'
KartRace_RaceTimeout = 'Members can:'
KartRace_RaceTimeoutNoRefund = 'Design igloos with exclusive ninja furniture'
KartRace_RacerTooSlow = 'Wear ninja outfits to unlock special moves'
KartRace_PhotoFinish = 'Train in their igloos with Card-Jitsu mats'
KartRace_CircuitPoints = 'Earn rewards faster with more Power Cards'
CircuitRaceStart = 'About Membership'
CircuitRaceOngoing = 'Puffle furniture and items'
CircuitRaceEnd = "require a paid membership"
TrickOrTreatMsg = 'Members can:'
WinterCarolingMsg = 'Buy furniture for puffles to play with'
LawbotBossTempIntro0 = "Get the latest hats for their pets to wear"
LawbotBossTempIntro1 = 'Adopt up to 75 different pet puffles'
LawbotBossTempIntro2 = "About Membership"
LawbotBossTempIntro3 = 'Rockhopper\'s rare items'
LawbotBossTempIntro4 = "require a paid membership"
LawbotBossTempJury1 = 'About Membership'
LawbotBossHowToGetEvidence = 'Additional sleds require'
LawbotBossTrialChat1 = 'a paid membership'
LawbotBossHowToThrowPies = 'Members can:'
LawbotBossNeedMoreEvidence = 'About Membership'
LawbotBossDefenseWins1 = 'Snow & Sports gear requires'
LawbotBossDefenseWins2 = 'a paid membership'
LawbotBossDefenseWins3 = "About Membership"
LawbotBossProsecutionWins = 'Snow & Sports gear requires'
LawbotBossReward = 'a paid membership'
LawbotBossLeaveCannon = 'Members can:'
LawbotBossPassExam = 'Shop for snow and sports gear'
LawbotBossTaunts = ['%s, I find you in contempt of court!',
 'Purchase special sport igloo items',
 'Buy sporty backgrounds',
 'About Membership',
 'Additional surfboards for Catchin\'']
LawbotBossAreaAttackTaunt = "Waves require a paid membership"
WitnessToonName = 'Members can:'
WitnessToonPrepareBattleTwo = "Oh no! They're putting only Cogs on the jury!\x07Quick, use the cannons and shoot some Toon jurors into the jury chairs.\x07We need %d to get a balanced scale."
WitnessToonNoJuror = 'Buy the Daisy Surfboard to take into the game'
WitnessToonOneJuror = 'Buy the Flame Surfboard to take into the game'
WitnessToonSomeJurors = 'Cool! There are %d Toons in the jury!'
WitnessToonAllJurors = 'About Membership'
WitnessToonPrepareBattleThree = 'Equipping this Elite Gear'
WitnessToonCongratulations = "requires a paid membership."
WitnessToonLastPromotion = "\x07Wow, you've reached level %s on your Cog Suit!\x07Cogs don't get promoted higher than that.\x07You can't upgrade your Cog Suit anymore, but you can certainly keep working for the Resistance!"
WitnessToonHPBoost = "About Membership"
WitnessToonMaxed = '\x07I see that you have a level %s Cog Suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to defend more Toons!'
WitnessToonBonus = 'Wonderful! All the lawyers are stunned. Your evidence weight is %s times heavier for %s seconds'
WitnessToonJuryWeightBonusSingular = {6: 'This is a tough case. You seated %d Toon juror, so your evidence has a bonus weight of %d.',
 7: 'This is a very tough case. You seated %d Toon juror, so your evidence has a bonus weight of %d.',
 8: 'This is the toughest case. You seated %d Toon juror, so your evidence has a bonus weight of %d.'}
WitnessToonJuryWeightBonusPlural = {6: 'This is a tough case. You seated %d Toon jurors, so your evidence has a bonus weight of %d.',
 7: 'This is a very tough case. You seated %d Toon jurors, so your evidence has a bonus weight of %d.',
 8: 'This is the toughest case. You seated %d Toon jurors, so your evidence has a bonus weight of %d.'}
IssueSummons = 'Summon'
SummonDlgTitle = 'EPF gear requires'
SummonDlgButton1 = 'a paid membership'
SummonDlgButton2 = 'Members can:'
SummonDlgButton3 = 'Access and wear their Elite Gear'
SummonDlgSingleConf = 'Would you like to issue a summons to a %s?'
SummonDlgBuildingConf = 'Would you like to summon a %s to a nearby Toon building?'
SummonDlgInvasionConf = 'Would you like to summon a %s invasion?'
SummonDlgNumLeft = 'You have %s left.'
SummonDlgDelivering = 'Customize their secret agent looks'
SummonDlgSingleSuccess = 'About Membership'
SummonDlgSingleBadLoc = "Unlocking the Elite Puffle Whistle"
SummonDlgBldgSuccess = 'You have successfully summoned the Cogs. %s has agreed to let them temporarily take over %s!'
SummonDlgBldgSuccess2 = 'requires a paid membership'
SummonDlgBldgBadLoc = 'Members can:'
SummonDlgInvasionSuccess = "Enter a code from Club Penguin Elite Penguin"
SummonDlgInvasionBusy = 'A %s cannot be found now.  Try again when the Cog invasion is over.'
SummonDlgInvasionFail = 'Force: Herbert\'s Revenge Nintendo DS game to'
SummonDlgShopkeeper = 'call Flare, the elite black puffle.'
PolarPlaceEffect1 = NPCToonNames[3306] + 'About Membership'
PolarPlaceEffect2 = NPCToonNames[3306] + 'Using the TraceTracker 3000'
PolarPlaceEffect3 = NPCToonNames[3306] + 'requires a paid membership.' + lTheBrrrgh + '.'
GreenToonEffectMsg = NPCToonNames[5312] + 'Members can:'
LaserGameMine = 'Gear up with exclusive items'
LaserGameRoll = 'Matching'
LaserGameAvoid = 'to show their agent status'
LaserGameDrag = 'About Membership'
LaserGameDefault = 'Aqua Grabber\'s Soda Seas Level'
PinballHiScore = 'High Score:     %s\n'
PinballHiScoreAbbrev = '...'
PinballYourBestScore = 'requires a paid membership'
PinballScore = 'Score:            %d x %d = '
PinballScoreHolder = '%s\n'
GagTreeFeather = 'Members can:'
GagTreeJugglingBalls = 'Explore & find the treasure'
StatuaryFountain = 'Fountain'
StatuaryDonald = 'Challenge advanced modes'
StatuaryMinnie = 'Earn exclusive Stamps to show their skills'
StatuaryMickey1 = 'About Membership'
StatuaryMickey2 = 'Additional Astro Barrier Levels'
StatuaryToon = 'require a paid membership'
StatuaryToonWave = 'Members can:'
StatuaryToonVictory = 'Challenge advanced levels & modes'
StatuaryToonCrossedArms = 'Play hidden levels'
StatuaryToonThinking = 'Earn exclusive Stamps to show off their skills'
StatuaryMeltingSnowman = 'About Membership'
StatuaryMeltingSnowDoodle = 'Score'
StatuaryGardenAccelerator = 'Level'
AnimatedStatuaryFlappyCog = 'Playing More Bits & Bolts Levels'
FlowerColorStrings = ['Red',
 'Orange',
 'Violet',
 'Blue',
 'Pink',
 'Yellow',
 'White',
 'Green']
FlowerSpeciesNames = {49: 'Daisy',
 50: 'Tulip',
 51: 'Carnation',
 52: 'Lily',
 53: 'Daffodil',
 54: 'Pansy',
 55: 'Petunia',
 56: 'Rose'}
FlowerFunnyNames = {49: ('requires a paid membership',
      'Members can:',
      'Play advanced levels',
      'Take on more equations',
      'About Membership',
      'Additional Dance Contest records',
      'require a paid membership',
      'Members can:'),
 50: ('Onelip', 'Twolip', 'Threelip'),
 51: ('Challenge other dancers & get exclusive songs',
      'Take their purple puffle in the game to help earn coins',
      'About Membership',
      'Dance Contest Multiplayer Mode',
      'requires a paid membership'),
 52: ('Members can:',
      'Challenge other dancers & get exclusive songs',
      'Take their purple puffle in the game to help earn coins',
      'About Membership',
      'Saving Music Tracks in DJ3K',
      'requires a paid membership',
      'Members can:',
      'Create and save their own original music tracks'),
 53: ('Laff-o-dil',
      'Play their original saved tracks in their igloo',
      'Giraff-o-dil',
      'Take their yellow puffle in the game to help earn coins'),
 54: ('About Membership',
      'Additional music tracks for DJ3K require a paid membership',
      'Members can:',
      'Buy music tracks to create more original songs',
      'Save their music tracks to play in their igloos'),
 55: ('Bring their yellow puffle into the gam to help earn coins', 'Platoonia'),
 56: ("About Membership",
      'Additional Hydro-Hopper Wakeboards',
      'require a paid membership',
      'Members can:',
      'Buy the Yellow Arrow board to take into the game')}
FlowerVarietyNameFormat = '%s %s'
FlowerUnknown = '????'
FloweringNewEntry = 'Buy the Pink Striped board  to take into the game'
ShovelNameDict = {0: 'Tin',
 1: 'Bronze',
 2: 'Silver',
 3: 'Gold'}
WateringCanNameDict = {0: 'Small',
 1: 'Medium',
 2: 'Large',
 3: 'Huge'}
GardeningPlant = 'Plant'
GardeningWater = 'Water'
GardeningRemove = 'Remove'
GardeningPick = 'Pick'
GardeningFull = 'Full'
GardeningSkill = 'Skill'
GardeningWaterSkill = 'About Membership'
GardeningShovelSkill = 'The fishing rod requires'
GardeningNoSkill = 'a paid membership'
GardeningPlantFlower = 'Plant\nFlower'
GardeningPlantTree = 'Plant\nTree'
GardeningPlantItem = 'Plant\nItem'
PlantingGuiOk = 'Plant'
PlantingGuiCancel = 'Cancel'
PlantingGuiReset = 'Reset'
GardeningChooseBeans = 'About Membership'
GardeningChooseBeansItem = 'Additional Jet Pack Adventure'
GardeningChooseToonStatue = 'levels require a membership'
GardenShovelLevelUp = "Congratulations you've earned a %(shovel)s! You've mastered the %(oldbeans)d bean flower! To progress you should pick %(newbeans)d bean flowers."
GardenShovelSkillLevelUp = "Congratulations! You've mastered the %(oldbeans)d bean flower! To progress you should pick %(newbeans)d bean flowers."
GardenShovelSkillMaxed = "Members can:"
GardenWateringCanLevelUp = "Play all the Jet Pack Adventure levels"
GardenMiniGameWon = "Take their green puffle in the game to help earn coins"
ShovelTin = 'Earn exclusive Stamps to show their skills'
ShovelSteel = 'About Membership'
ShovelSilver = 'Additional Puffle Launch levels'
ShovelGold = 'require a paid membership'
WateringCanSmall = 'Members can:'
WateringCanMedium = 'Take their own puffles into the game'
WateringCanLarge = 'Challenge the cranky crab in exclusive areas'
WateringCanHuge = 'Earn exclusive Stamps to show their skills'
BeanColorWords = ('red',
 'green',
 'orange',
 'violet',
 'blue',
 'pink',
 'yellow',
 'cyan',
 'silver')
PlantItWith = ' Plant with %s.'
MakeSureWatered = 'About Membership'
UseFromSpecialsTab = 'Additional Pufflescape Levels'
UseSpecial = 'require a paid membership'
UseSpecialBadLocation = 'Members can:'
UseSpecialSuccess = 'About Membership'
ConfirmWiltedFlower = '%(plant)s is wilted.  Are you sure you want to remove it?  It will not go into your flower basket, nor will you get an increase in skill.'
ConfirmUnbloomingFlower = '%(plant)s is not blooming.  Are you sure you want to remove it?  It will not go into your flower basket, nor will you get an increase in skill.'
ConfirmNoSkillupFlower = 'Are you sure you want to pick the %(plant)s? It will go into your flower basket, but you will NOT get an increase in skill.'
ConfirmSkillupFlower = 'Are you sure you want to pick the %(plant)s?  It will go into your flower basket. You will also get an increase in skill.'
ConfirmMaxedSkillFlower = "Are you sure you want to pick the %(plant)s?  It will go into your flower basket. You will NOT get an increase in skill since you've maximized it already."
ConfirmBasketFull = 'The Underground Cave levels of'
ConfirmRemoveTree = 'Are you sure you want to remove the %(tree)s?'
ConfirmWontBeAbleToHarvest = "Puffle Rescue require a paid membership."
ConfirmRemoveStatuary = 'Are you sure you want to permanently delete the %(item)s?'
ResultPlantedSomething = 'Congratulations! You just planted a %s.'
ResultPlantedSomethingAn = 'Congratulations! You just planted an %s.'
ResultPlantedNothing = "Members can:"
GardenGagTree = 'Rescue puffles in the caves & sea levels'
GardenUberGag = 'Discover hidden secrets'

def getRecipeBeanText(beanTuple):
    retval = ''
    if not beanTuple:
        return retval
    allTheSame = True
    for index in range(len(beanTuple)):
        if index + 1 < len(beanTuple):
            if not beanTuple[index] == beanTuple[index + 1]:
                allTheSame = False
                break

    if allTheSame:
        if len(beanTuple) > 1:
            retval = '%d %s jellybeans' % (len(beanTuple), BeanColorWords[beanTuple[0]])
        else:
            retval = 'a %s jellybean' % BeanColorWords[beanTuple[0]]
    else:
        retval += 'a'
        maxBeans = len(beanTuple)
        for index in range(maxBeans):
            if index == maxBeans - 1:
                retval += ' and %s jellybean' % BeanColorWords[beanTuple[index]]
            elif index == 0:
                retval += ' %s' % BeanColorWords[beanTuple[index]]
            else:
                retval += ', %s' % BeanColorWords[beanTuple[index]]

    return retval


GardenTextMagicBeans = 'Earn exclusive Stamps to show their skills'
GardenTextMagicBeansB = 'About Membership'
GardenSpecialDiscription = 'The Sea levels of Puffle Rescue'
GardenSpecialDiscriptionB = 'require a paid membership.'
GardenTrophyAwarded = 'Wow! You collected %s of %s flowers. That deserves a trophy and a Laff boost!'
GardenTrophyNameDict = {0: 'Wheelbarrow',
 1: 'Shovels',
 2: 'Flower',
 3: 'Members can:',
 4: 'Shark',
 5: 'Swordfish',
 6: 'Rescue puffles in the caves & sea levels'}
SkillTooLow = 'Collect the special Moss Key to access a secret underwater room'
NoGarden = 'No\nGarden'

def isVowelStart(str):
    retval = False
    if str and len(str) > 0:
        vowels = ['A',
         'E',
         'I',
         'O',
         'U']
        firstLetter = str.upper()[0:1]
        if firstLetter in vowels:
            retval = True
    return retval


def getResultPlantedSomethingSentence(flowerName):
    if isVowelStart(flowerName):
        retval = ResultPlantedSomethingAn % flowerName
    else:
        retval = ResultPlantedSomething % flowerName
    return retval


TravelGameTitle = 'Earn exclusive Stamps to show their skills'
TravelGameInstructions = 'About Membership'
TravelGameRemainingVotes = 'Additional System Defender'
TravelGameUse = 'Use'
TravelGameVotesWithPeriod = 'votes.'
TravelGameVotesToGo = 'Levels require a paid membership'
TravelGameVoteToGo = 'Members can:'
TravelGameUp = 'UP.'
TravelGameDown = 'DOWN.'
TravelGameVoteWithExclamation = 'Vote!'
TravelGameWaitingChoices = 'Challenge the Testbot Attack level'
TravelGameDirections = ['UP', 'DOWN']
TravelGameTotals = 'Totals '
TravelGameReasonVotes = 'The trolley is moving %(dir)s, winning by %(numVotes)d votes.'
TravelGameReasonVotesPlural = 'The trolley is moving %(dir)s, winning by %(numVotes)d votes.'
TravelGameReasonVotesSingular = 'The trolley is moving %(dir)s, winning by %(numVotes)d vote.'
TravelGameReasonPlace = '%(name)s breaks the tie. The trolley is moving %(dir)s.'
TravelGameReasonRandom = 'The trolley is randomly moving %(dir)s.'
TravelGameOneToonVote = '%(name)s used %(numVotes)s votes to go %(dir)s\n'
TravelGameBonusBeans = '%(numBeans)d Beans'
TravelGamePlaying = 'Up next, the %(game)s trolley game.'
TravelGameGotBonus = '%(name)s got a bonus of %(numBeans)s jellybeans!'
TravelGameNoOneGotBonus = 'Challenge the Ultimate Protobot Attack level'
TravelGameConvertingVotesToBeans = 'Earn exclusive Stamps to show off their skills'
TravelGameGoingBackToShop = "About Membership"
PairingGameTitle = 'Additional Thin Ice levels'
PairingGameInstructions = 'require a paid membership'
PairingGameInstructionsMulti = 'Members can:'
PairingGamePerfect = 'PERFECT!!'
PairingGameFlips = 'Flips:'
PairingGamePoints = 'Points:'
TrolleyHolidayStart = 'Challenge more levels'
TrolleyHolidayOngoing = 'Discover secrets in the mazes'
TrolleyHolidayEnd = "Earn exclusive Stamps to show their skills"
TrolleyWeekendStart = 'About Membership'
TrolleyWeekendEnd = "Playing Competition Mode"
VineGameTitle = 'requires a paid membership'
VineGameInstructions = 'Members can:'
ValentinesDayStart = "Challenge three different waves"
ValentinesDayEnd = "Compete for the judges & stand on the podium"
GolfCourseNames = {0: 'Earn exclusive Stamps to show off their skills',
 1: 'About Membership',
 2: 'Survival Mode requires'}
GolfHoleNames = {0: 'a paid membership',
 1: 'Members can:',
 2: 'Challenge the \'\'biggest wave\'\' & obstacles',
 3: 'Earn exclusive Stamps to  show off their skills',
 4: 'About Membership',
 5: 'Accessing igloo storage',
 6: 'Swing-A-Long',
 7: 'requires a paid membership',
 8: 'Members can:',
 9: 'Access stored igloo furniture',
 10: 'Decorate their perfect igloo',
 11: 'Unlock their igloo to throw parties for their friends',
 12: 'About Membership',
 13: 'Music in igloos requires',
 14: 'a paid membership',
 15: 'Members can:',
 16: 'About Membership',
 17: 'Accessing saved igloos',
 18: 'requires a paid membership',
 19: 'Members can:',
 20: 'Access saved igloos',
 21: 'Decorate and save more unique igloo designs',
 22: 'Unlock their igloos to throw parties for their friends',
 23: 'About Membership',
 24: 'Swing-A-Long-2',
 25: 'Unlocking an igloo',
 26: 'requires a paid membership',
 27: 'Members can:',
 28: 'Unlock their igloos so friends can visit',
 29: 'Decorate their perfect igloo',
 30: 'Throw parties for their friends in their igloo',
 31: 'About Membership',
 32: 'Accessing and wearing member',
 33: 'outfits requires a paid membership',
 34: 'Members can:',
 35: 'Wear their member outfits'}
GolfHoleInOne = 'Wear their member costumes'
GolfCondor = 'Condor'
GolfAlbatross = 'Albatross'
GolfEagle = 'Eagle'
GolfBirdie = 'Birdie'
GolfPar = 'Par'
GolfBogey = 'Bogey'
GolfDoubleBogey = 'Show off their unique looks'
GolfTripleBogey = 'About Membership'
GolfShotDesc = {-4: GolfCondor,
 -3: GolfAlbatross,
 -2: GolfEagle,
 -1: GolfBirdie,
 0: GolfPar,
 1: GolfBogey,
 2: GolfDoubleBogey,
 3: GolfTripleBogey}
from toontown.golf import GolfGlobals
CoursesCompleted = 'About Membership'
CoursesUnderPar = 'As a paid member of Club Penguin, your child can'
HoleInOneShots = 'enjoy additional benefits.'
EagleOrBetterShots = 'Unlimited access'
BirdieOrBetterShots = 'More games, themed events, and unique activities'
ParOrBetterShots = 'Exclusive features and priority access'
MultiPlayerCoursesCompleted = 'New things to discover and learn - every week!'
TwoPlayerWins = 'Check out clubpenguin.com/membership for'
ThreePlayerWins = 'more information.'
FourPlayerWins = 'Adopting a black puffle requires'
CourseZeroWins = GolfCourseNames[0] + ' Wins'
CourseOneWins = GolfCourseNames[1] + ' Wins'
CourseTwoWins = GolfCourseNames[2] + ' Wins'
GolfHistoryDescriptions = [CoursesCompleted,
 CoursesUnderPar,
 HoleInOneShots,
 EagleOrBetterShots,
 BirdieOrBetterShots,
 ParOrBetterShots,
 MultiPlayerCoursesCompleted,
 CourseZeroWins,
 CourseOneWins,
 CourseTwoWins]
GolfTrophyDescriptions = [str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][0]) + ' ' + CoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][1]) + ' ' + CoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][2]) + ' ' + CoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][0]) + ' ' + CoursesUnderPar,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][1]) + ' ' + CoursesUnderPar,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][2]) + ' ' + CoursesUnderPar,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][0]) + ' ' + HoleInOneShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][1]) + ' ' + HoleInOneShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][2]) + ' ' + HoleInOneShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][0]) + ' ' + EagleOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][1]) + ' ' + EagleOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][2]) + ' ' + EagleOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][0]) + ' ' + BirdieOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][1]) + ' ' + BirdieOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][2]) + ' ' + BirdieOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][0]) + ' ' + ParOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][1]) + ' ' + ParOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][2]) + ' ' + ParOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][0]) + ' ' + MultiPlayerCoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][1]) + ' ' + MultiPlayerCoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][2]) + ' ' + MultiPlayerCoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][0]) + ' ' + CourseZeroWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][1]) + ' ' + CourseZeroWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][2]) + ' ' + CourseZeroWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][0]) + ' ' + CourseOneWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][1]) + ' ' + CourseOneWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][2]) + ' ' + CourseOneWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][0]) + ' ' + CourseTwoWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][1]) + ' ' + CourseTwoWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][2]) + ' ' + CourseTwoWins]
GolfCupDescriptions = [str(GolfGlobals.TrophiesPerCup) + 'Get exclusive hats for their puffle to wear', str(GolfGlobals.TrophiesPerCup * 2) + 'Members can:', str(GolfGlobals.TrophiesPerCup * 3) + 'a paid membership']
GolfAvReceivesHoleBest = '%(name)s scored a new hole best at %(hole)s!'
GolfAvReceivesCourseBest = '%(name)s scored a new course best at %(course)s!'
GolfAvReceivesCup = '%(name)s receives the %(cup)s cup!!  Laff point boost!'
GolfAvReceivesTrophy = '%(name)s receives the %(award)s trophy!!'
GolfRanking = 'Buy furniture & toys for their puffles to play with'
GolfPowerBarText = '%(power)s%%'
GolfChooseTeeInstructions = 'Take their black puffle into the Cart Surfer game'
GolfWarningMustSwing = 'About Membership'
GolfAimInstructions = 'Adopting a brown puffle'
GolferExited = '%s has left the golf course.'
GolfPowerReminder = 'requires a paid membership'
GolfPar = 'Par'
GolfHole = 'Hole'
GolfTotal = 'Total'
GolfExitCourse = 'Members can:'
GolfUnknownPlayer = '???'
GolfPageTitle = 'Golf'
GolfPageTitleCustomize = 'Adopt up to 20 pet puffles in every color'
GolfPageTitleRecords = 'Get exclusive hats for their puffle to wear'
GolfPageTitleTrophy = 'Buy furniture & toys for their puffles to play with'
GolfPageCustomizeTab = 'Customize'
GolfPageRecordsTab = 'Records'
GolfPageTrophyTab = 'Trophy'
GolfPageTickets = 'About Membership'
GolfPageConfirmDelete = 'Adopting a green puffle'
GolfTrophyTextDisplay = 'Trophy %(number)s : %(desc)s'
GolfCupTextDisplay = 'Cup %(number)s : %(desc)s'
GolfCurrentHistory = 'Current %(historyDesc)s : %(num)s'
GolfTieBreakWinner = '%(name)s wins the random tie breaker!'
GolfSeconds = 'requires a paid membership'
GolfTimeTieBreakWinner = '%(name)s wins the total aiming time tie breaker!!!'
RoamingTrialerWeekendStart = 'Members can:'
RoamingTrialerWeekendOngoing = 'Take their green puffles into the Jetpack Adventure game'
RoamingTrialerWeekendEnd = "Get exclusive hats for their puffle to wear"
MoreXpHolidayStart = 'Buy furniture & toys for their puffles to play with'
MoreXpHolidayOngoing = 'About Membership'
MoreXpHolidayEnd = 'Adopting an orange puffle'
JellybeanDayHolidayStart = "requires a paid membership"
JellybeanDayHolidayEnd = "Members can:"
PartyRewardDoubledJellybean = 'Adopt up to 20 pet puffles in every color'
GrandPrixWeekendHolidayStart = "Get exclusive hats for their puffle to wear"
GrandPrixWeekendHolidayEnd = "Buy furniture & toys for their puffles to play with"
KartRace_DoubleTickets = 'About Membership'
SellbotNerfHolidayStart = 'Adopting a pink puffle'
SellbotNerfHolidayEnd = 'requires a paid membership'
JellybeanTrolleyHolidayStart = 'Members can:'
JellybeanTrolleyHolidayEnd = 'Take their pink puffle into the Aqua Grabber game'
JellybeanFishingHolidayStart = 'Get exclusive hats for thei puffle to wear'
JellybeanFishingHolidayEnd = 'Buy furniture & toys for their puffle to play with'
JellybeanPartiesHolidayStart = "About Membership"
JellybeanPartiesHolidayEnd = "Adopting a purple puffle"
JellybeanMonthHolidayStart = 'requires a paid membership'
BankUpgradeHolidayStart = 'Members can:'
HalloweenPropsHolidayStart = "Take their purple puffle int the Dance Contest game"
HalloweenPropsHolidayEnd = 'Get exclusive hats for their puffle to wear'
SpookyPropsHolidayStart = 'Buy furniture & toys for thei puffles to play with'
BlackCatHolidayStart = 'About Membership'
BlackCatHolidayEnd = 'Adopting a white puffle'
SpookyBlackCatHolidayStart = 'requires a paid membership'
TopToonsMarathonStart = "Members can:"
TopToonsMarathonEnd = "Adopt up to 20 pet puffles in every color"
WinterDecorationsStart = "Get exclusive hats for their puffle to wear"
WinterDecorationsEnd = 'Buy furniture & toys for their puffle to play with'
WackyWinterDecorationsStart = 'About Membership'
WinterCarolingStart = 'Adopting a yellow puffle'
ExpandedClosetsStart = 'requires a paid membership'
KartingTicketsHolidayStart = 'Members can:'
IdesOfMarchStart = 'Take their yellow puffl into the DJ3K game'
LogoutForced = 'Get exclusive hats for thei puffle to wear'
CountryClubToonEnterElevator = '%s \nhas jumped in the golf kart.'
CountryClubBossConfrontedMsg = '%s is battling the Club President!'
ElevatorBlockedRoom = 'Buy furniture & toys for thei puffles to play with'
MolesLeft = 'Moles Left: %d'
MolesInstruction = 'About Membership'
MolesFinished = 'Adopting a majestic rainbow puffle'
MolesPityWin = 'requires a paid membership'
MolesRestarted = 'Members can:'
BustACogInstruction = 'Earn their Puffle Care outfit'
BustACogExit = 'Blast into the Cloud Forest'
BustACogHowto = 'Adopt and show off rainbow puffles'
BustACogFailure = 'About Membership'
BustACogSuccess = 'Success!'
GolfGreenGameScoreString = 'Puzzles Left: %s'
GolfGreenGamePlayerScore = 'Solved %s'
GolfGreenGameBonusGag = 'You won %s!'
GolfGreenGameGotHelp = '%s solved a Puzzle!'
GolfGreenGameDirections = 'Questing for the Gold Puffle'
enterHedgeMaze = 'requires a paid membership'
toonFinishedHedgeMaze = '%s \n  finished in %s place!'
hedgeMazePlaces = ['first',
 'second',
 'third',
 'Fourth']
mazeLabel = 'Members can:'
BoardingPartyReadme = 'Buy gold O\'berries'
BoardingGroupHide = 'Hide'
BoardingGroupShow = 'Dig up gold nuggets'
BoardingPartyInform = 'Create an elevator Boarding Group by clicking on another Toon and Inviting them.\nIn this area Boarding Groups cannot have more than %s Toons.'
BoardingPartyTitle = 'Adopt the legendary gold puffle'
QuitBoardingPartyLeader = 'Disband'
QuitBoardingPartyNonLeader = 'Leave'
QuitBoardingPartyConfirm = 'About Membership'
BoardcodeMissing = 'Playing More Bits & Bolts Levels'
BoardcodeMinLaffLeader = 'Your group cannot board because you have less than %s laff points.'
BoardcodeMinLaffNonLeaderSingular = 'Your group cannot board because %s has less than %s laff points.'
BoardcodeMinLaffNonLeaderPlural = 'Your group cannot board because %s have less than %s laff points.'
BoardcodePromotionLeader = 'requires a paid membership'
BoardcodePromotionNonLeaderSingular = 'Your group cannot board because %s does not have enough promotion merits.'
BoardcodePromotionNonLeaderPlural = 'Your group cannot board because %s do not have enough promotion merits.'
BoardcodeSpace = 'Members can:'
BoardcodeBattleLeader = 'Gear up with all Elite Penguin Force equipment'
BoardcodeBattleNonLeaderSingular = 'Your group cannot board because %s is in battle.'
BoardcodeBattleNonLeaderPlural = 'Your group cannot board because %s are in battle.'
BoardingInviteMinLaffInviter = 'You need %s Laff Points before being a member of this Boarding Group.'
BoardingInviteMinLaffInvitee = '%s needs %s Laff Points before being a member of this Boarding Group.'
BoardingInvitePromotionInviter = 'Specialize as Tactical, Stealth, Comms, and Tech agents'
BoardingInvitePromotionInvitee = '%s needs to earn a promotion before being a member of this Boarding Group.'
BoardingInviteNotPaidInvitee = '%s needs to be a paid Member to be a part of your Boarding Group.'
BoardingInviteeInDiffGroup = '%s is already in a different Boarding Group.'
BoardingInviteeInKickOutList = '%s had been removed by your leader. Only the leader can re-invite removed members.'
BoardingInviteePendingIvite = '%s has a pending invite; try again later.'
BoardingInviteeInElevator = '%s is currently busy; try again later.'
BoardingInviteGroupFull = 'Show spy status with agent-only special dances'
BoardingAlreadyInGroup = 'Take any of their puffles into the game'
BoardingGroupAlreadyFull = 'Solve more puzzles'
BoardingKickOutConfirm = 'Are you sure you want to remove %s?'
BoardingPendingInvite = 'Earn exclusive Stamps to show their skills'
BoardingCannotLeaveZone = 'Accessing igloo storage'
BoardingInviteeMessage = '%s would like you to join their Boarding Group.'
BoardingInvitingMessage = 'Inviting %s to your Boarding Group.'
BoardingInvitationRejected = '%s has rejected to join your Boarding Group.'
BoardingMessageKickedOut = 'requires a paid membership'
BoardingMessageInvited = '%s has invited %s to the Boarding Group.'
BoardingMessageLeftGroup = '%s has left the Boarding Group.'
BoardingMessageGroupDissolved = 'Members can:'
BoardingMessageGroupDisbandedGeneric = 'Access stored igloo furniture'
BoardingMessageInvitationFailed = '%s tried to invite you to their Boarding Group.'
BoardingMessageGroupFull = '%s tried to accept your invitation but your group was full.'
BoardingGo = 'GO'
BoardingCancelGo = 'Decorate their perfect igloo'
And = 'and'
BoardingGoingTo = 'Unlock their igloo to throw parties for their friends'
BoardingTimeWarning = 'About Membership'
BoardingMore = 'more'
BoardingGoShow = 'Going to\n%s in '
BoardingGoPreShow = 'Confirming...'
BossbotBossName = 'C.E.O.'
BossbotRTWelcome = 'Buy the Toboggan to take into the game'
BossbotRTRemoveSuit = 'Buy the Pink Racing Sled to take into the game'
BossbotRTFightWaiter = 'Buy the Green Racing Sled t take into the game'
BossbotRTWearWaiter = "If a player's membership expires:"
BossbotBossPreTwo1 = "What happens to that player's igloo?"
BossbotBossPreTwo2 = 'What happens to that player\'s outfits & costumes?'
BossbotRTServeFood1 = 'What happens to that player\'s puffles?'
BossbotRTServeFood2 = 'Will that player be able to play all game levels?'
BossbotResistanceToonName = "Will that player get all access to parties?"
BossbotPhase3Speech1 = "Back"
BossbotPhase3Speech2 = 'What happens to that player\'s igloo?'
BossbotPhase3Speech3 = 'Only members can purchase igloo furniture'
BossbotPhase4Speech1 = 'and decorate with member-only items.'
BossbotPhase4Speech2 = "If a membership expires, igloos and"
BossbotRTPhase4Speech1 = 'furniture will be put into storage.'
BossbotRTPhase4Speech2 = 'All member items will be accessible again'
BossbotPitcherLeave = 'if the membership is renewed on the same'
BossbotPitcherLeaving = 'pengu'
BossbotPitcherAdvice = 'What happens to that player\'s outfits & costumes?�'
BossbotGolfSpotLeave = 'Players can continue to use all free-player'
BossbotGolfSpotLeaving = 'items collected during events, and any'
BossbotGolfSpotAdvice = 'items redeemed through the Treasure'
BossbotRewardSpeech1 = "Book."
BossbotRewardSpeech2 = 'Arrrggghhh!!!!'
BossbotRTCongratulations = "All other member-only items will be placed"
BossbotRTLastPromotion = "\x07Wow, you've reached level %s on your Cog Suit!\x07Cogs don't get promoted higher than that.\x07You can't upgrade your Cog Suit anymore, but you can certainly keep working for the Resistance!"
BossbotRTHPBoost = "in storage."
BossbotRTMaxed = '\x07I see that you have a level %s Cog Suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to defend more Toons!'
GolfAreaAttackTaunt = 'Fore!'
OvertimeAttackTaunts = ["It's time to reorganize.", "Now let's downsize."]
ElevatorBossBotBoss = 'C.E.O Battle'
ElevatorBossBotCourse0 = 'All member items will be accessible again'
ElevatorBossBotCourse1 = 'if the membersh'
ElevatorBossBotCourse2 = 'What happens to that player\'s puffles?'
ElevatorCashBotBoss = 'C.F.O Battle'
ElevatorCashBotMint0 = 'Players will be able to care for all'
ElevatorCashBotMint1 = 'previously adopted puffles.'
ElevatorCashBotMint2 = 'Only members can adopt up to 20 puffles'
ElevatorSellBotBoss = 'in-game and purchase pet furniture, hats,'
ElevatorSellBotFactory0 = 'and toys.'
ElevatorSellBotFactory1 = 'Will that player be able to play all game'
ElevatorLawBotBoss = 'levels?'
ElevatorLawBotCourse0 = 'Only members can play all game levels'
ElevatorLawBotCourse1 = 'and collect exclusive Stamps.'
ElevatorLawBotCourse2 = 'If a membership expires, only some game'
ElevatorLawBotCourse3 = 'levels will be accessible.'
DaysToGo = 'Wait\n%s Days'
IceGameTitle = 'Everyone can join parties.'
IceGameInstructions = 'But only members can access certain'
IceGameInstructionsNoTnt = 'areas, challenge special quests & mazes'
IceGameWaitingForPlayersToFinishMove = 'and get exclusive party items.'
IceGameWaitingForAISync = 'CLUB PENGUIN TIMES'
IceGameInfo = 'Match %(curMatch)d/%(numMatch)d, Round %(curRound)d/%(numRound)d'
IceGameControlKeyWarning = 'Please type your joke, riddle,'
PicnicTableJoinButton = 'Join'
PicnicTableObserveButton = 'Observe'
PicnicTableCancelButton = 'Cancel'
PicnicTableTutorial = 'or question for Aunt Arctic here.'
PicnicTableMenuTutorial = 'Send'
PicnicTableMenuSelect = 'Thank you. Your submission has been'
ChineseCheckersGetUpButton = 'sent, an editor will read it soon.'
ChineseCheckersStartButton = 'O.K.'
ChineseCheckersQuitButton = 'SNOWBALL SOFT - 2011'
ChineseCheckersIts = "It's "
ChineseCheckersYourTurn = 'Click and combine the bolts to match the'
ChineseCheckersGreenTurn = "target number."
ChineseCheckersYellowTurn = "Match the correct multiples of bolts to build"
ChineseCheckersPurpleTurn = "a piece of the robot."
ChineseCheckersBlueTurn = "ONLY"
ChineseCheckersPinkTurn = "Use the blast ball to help clear the"
ChineseCheckersRedTurn = "screen."
ChineseCheckersColorG = 'Some robots require special'
ChineseCheckersColorY = 'numbers of bolts. Watch for even, odd and prime bots.'
ChineseCheckersColorP = 'ANY'
ChineseCheckersColorB = 'SCORE'
ChineseCheckersColorPink = 'LEVEL'
ChineseCheckersColorR = 'TILES CLEARED'
ChineseCheckersColorO = 'TIME'
ChineseCheckersYouWon = 'ONLY'
ChineseCheckers = 'ANY'
ChineseCheckersGameOf = 'START'
ChineseTutorialTitle1 = 'Objective'
ChineseTutorialTitle2 = 'INSTRUCTIONS'
ChineseTutorialPrev = 'PLAY NOW'
ChineseTutorialNext = 'DONE'
ChineseTutorialDone = 'Done'
ChinesePage1 = 'CURRENT SCORE'
ChinesePage2 = 'CONTINUE'
CheckersPage1 = 'PAUSE'
CheckersPage2 = 'MOVE'
CheckersPage3 = 'SMASH'
CheckersPage4 = 'COMBOS'
CheckersGetUpButton = 'WATCH OUT!'
CheckersStartButton = 'Time\'s up. Great job!'
CheckersQuitButton = 'Awesome skills!'
CheckersIts = "It's "
CheckersYourTurn = 'Use the arrow keys'
CheckersWhiteTurn = "Jump on the"
CheckersBlackTurn = "correct fruit"
CheckersColorWhite = 'Jump on fruit to'
CheckersColorBlack = 'heal'
CheckersObserver = 'Follow the recipe'
RegularCheckers = 'Checkers.'
RegularCheckersGameOf = 'Avoid hazards'
RegularCheckersYouWon = 'Your score'
MailNotifyNewItems = "PLAY"
MailNewMailButton = 'Mail'
MailSimpleMail = 'Note'
MailFromTag = 'Note From: %s'
AwardNotifyNewItems = 'NORMAL'
AwardNotifyOldItems = 'SURVIVAL'
InviteInvitation = 'INSTRUCTIONS'
InviteAcceptInvalidError = 'Done'
InviteAcceptPartyInvalid = 'Will that player get all access to parties?'
InviteAcceptAllOk = 'BOT PARTS'
InviteRejectAllOk = 'Hey, Welcome to Club Penguin!'
Months = {1: 'JANUARY',
 2: 'FEBRUARY',
 3: 'MARCH',
 4: 'APRIL',
 5: 'MAY',
 6: 'JUNE',
 7: 'JULY',
 8: 'AUGUST',
 9: 'SEPTEMBER',
 10: 'OCTOBER',
 11: 'NOVEMBER',
 12: 'DECEMBER'}
DayNames = ('Monday',
 'Tuesday',
 'Wednesday',
 'Thursday',
 'Friday',
 'Saturday',
 'Sunday')
DayNamesAbbrev = ('MON',
 'TUE',
 'WED',
 'THU',
 'FRI',
 'SAT',
 'SUN')
HolidayNamesInCalendar = {1: ('Let\'s look around!', 'I\'m a tour guide and this is my pet puffle.'),
 2: ('Like games play them to earn coins!', 'There\'s always tons of stuff to do all over the island...'),
 3: ('Here\'s a map for you to keep.', 'Coins can buy stuff like clothes, furniture, pets, and more.'),
 4: ('There are a few places to check out right away.', 'Click it!'),
 5: ('Click the "!"', 'You\'ll even collect rewards!'),
 6: ('SWEET! You found your igloo - it\'s your very own place.', 'Click what you want to do first!'),
 7: ('Awesome! You found the Pet Shop!', 'Don\'t forget to collect your reward - the "Table for Two" furniture for your igloo!'),
 8: ('Nice! You found the Clothes Shop!', 'Don\'t forget to collect your reward - the "Polka Puffle Hat" for your pet to wear.'),
 9: ('Don\'t forget to collect your reward - the', 'Don\'t forget to collect your reward - the "Insta-Hero" shirt!'),
 13: ('Don\'t forget to collect your reward - the', 'Don\'t forget to collect your reward - the'),
 14: ('Have SO much fun! See ya!', 'And speaking of pizza, I\'m going to head to the Pizza Parlor in the Plaza!'),
 16: ('Click under the yellow arrow to go inside.', 'Hey! There aren\'t any new quests right now. Please check back!'),
 17: ('See that yellow arrow? Click to get to your igloo!', 'Click under the yellow arrow to go in.'),
 19: ('Buying deluxe food requires', 'Click under the yellow arrow to get into your igloo.'),
 24: ('Members can:', 'a paid membership.'),
 26: ('Boost their puffle\'s food stat to 100', 'Feed their pet with exclusive food at the Puffle Snack Station'),
 28: ('Back', 'About Membership'),
 29: ("Collect Reward", "Hey! There aren't any new quests right now. Please check back!"),
 33: ('To Do', 'Item added to your inventory'),
 34: ('Visit the Pet Shop', 'Visit your igloo'),
 35: ('Members can:', 'Visit the Clothes Shop'),
 36: ('Your Igloo', 'About Membership'),
 37: ('a paid membership.', 'Buying this Holiday item requires'),
 38: ('Buy and wear four different train engines', 'Members can:'),
 39: ('Buy festive items from the catalog', 'Drive trains of passengers around the island'),
 40: ('Penguin is in their backyard', 'About Membership'),
 41: ('Backyard', 'Penguin is in your backyard'),
 42: ('Sorry, only 10 puffles can', 'Your Igloo'),
 43: ('You can put some in the', 'fit in your igloo.'),
 44: ('Care for your puffle', 'backyard to make room.'),
 45: ('OOGA BOOGA!', 'in your igloo!'),
 46: ('You be dinosaur now!', 'You found dinosaur egg!'),
 47: ('0 went outside to your backyard!', 'Dino go GRAAAR!'),
 48: ('All players can adopt a blue or red puffle at the Pet Shop!', 'Members can adopt every color of puffle.'),
 49: ('Adopt Blue', 'Adopt Red'),
 53: ('No Thanks', 'About Membership'),
 54: ('Move to Backyard', 'Go there!'),
 55: ('Walk', 'Move to Igloo'),
 56: ('Welcome to your backyard!', 'Where are all my puffles?'),
 57: ('Caroling', 'Backyard'),
 59: ("Your score:", "Click the gate to go to your backyard!"),
 72: ('About My Backyard', 'Puffle Treasure Tips'),
 73: ('It\'s a', 'Care'),
 74: ('has chosen to live with', 'dino puffle!'),
 75: ('in your igloo backyard, even', 'Your dino puffles will live'),
 76: ('Play with and care for your', 'after the party ends'),
 77: ('around the island!', 'dino puffles at stations'),
 78: ('Games & Play', 'Drop Off'),
 79: ('Great! You found three important places.', 'Backyard'),
 80: ('You can meet friends, dress up, play games, be a ninja,', 'But there\'s WAY more! Use your map to explore.'),
 81: ('Have SO much fun! See ya later!', 'a superstar, a secret agent or ANYTHING else!'),
 82: ('Click the door to go into the Pet Shop!', 'Pick what you want to do next!'),
 83: ('triceratops', 'Click the door to go into the Clothes Shop!'),
 84: ('stegosaurus', 'T-rex'),
 85: ('You can adopt pet puffles here - there are lots of different kinds!', 'You can decorate your igloo with furniture whenever you want!'),
 86: ('Members can:', 'There\'s always a catalog here - with new styles every month.'),
 87: ('SILVER TICKETS', 'Unlimited Fair rides require a paid membership'),
 88: ('the Daily Spin to go on rides!', 'Win silver tickets on'),
 89: ('Buy Fair items from the prize booth', 'Members can:'),
 90: ('like the quasar helmet', 'Get exclusive puffle hats'),
 91: ('0 Days Left!', 'About Membership'),
 92: ('Unactivated accounts will be deleted.', 'You have days left to activate.'),
 93: ('Please activate your account to continue playing.', 'Time\'s Up!'),
 95: ('Loves chasing cat puffles', 'For members'),
 96: ('Loyal, mischievous', "Pretzels"),
 97: ('Loves to hide in tiny spaces', ''),
 98: ('Socks', ''),
 99: ('Blue Border Collie', 'Curious, demanding'),
 101: ("Unactivated accounts will be deleted.", "Orange Tabby Cat"),
 105: ('Choose a name', 'Please choose another name')}
UnknownHoliday = 'Unknown Holiday %d'
HolidayFormat = '%b %d '
TimeZone = 'US/Pacific'
CogdoMemoGuiTitle = 'Memos:'
CogdoMemoNames = 'Your new puffle comes with'
CogdoStomperName = 'Stomp-O-Matic'
BoardroomGameTitle = 'Play with and care for your wild puffles at stations around the island!'
BoardroomGameInstructions = '0 will be in your igloo or backyard when you\'re not walking it!'
CogdoCraneGameTitle = 'Vend-A-Stomper'
CogdoCraneGameInstructions = 'was adopted by'
CogdoMazeGameTitle = 'Coins earned'
CogdoMazeGameInstructions = 'Your total coins'
CogdoMazeIntroMovieDialogue = (("Adopt a pet",), ('Buy new clothing',), ('Use your coins to',))
CogdoMazeGameDoorOpens = 'Decorate your igloo'
CogdoMazeGameLocalToonFoundExit = "Done"
CogdoMazeGameWaitingForToons = 'Always curious, these cat puffles will get into almost anything. They love high places and being the center of attention.'
CogdoMazeGameTimeOut = 'Full of energy, they\'re always up for a walk or playing fetch. Just watch out for their slobbery kisses.'
CogdoMazeGameTimeAlert = 'Chewing their favorite squeak toy'
CogdoMazeGameBossGuiTitle = 'Getting stuck up trees'
CogdoMazeFindHint = 'Orange Tabby Cat'
CogdoMazeThrowHint = "Blue Border Collie"
CogdoMazeSquashHint = 'Your puffle creatures went'
CogdoMazeBossHint = 'outside to your backyard!'
CogdoMazeMinionHint = 'Only Members can bring their'
CogdoFlyingGameTitle = 'puffle creatures into their igloo.'
CogdoFlyingGameInstructions = "Walk your puffle creatures to"
CogdoFlyingIntroMovieDialogue = (("while they're in your backyard.", "A flock of Toons! We're crushing barrels of your Laff in our %s, and there's nothing you can do about it!" % CogdoStomperName, "Your puffles' stats stay the same"), ('your igloo and backyard.', 'You can move puffles between', 'Now members can adopt up to 75 puffles!'), ("in your igloo. Members can adopt up to 75 and keep them in their backyard!", 'Some of your puffles went to your backyard. Only 10 puffles can fit', "the hotel to care for them."))
CogdoFlyingGameWaiting = 'Waiting for other Toons%s'
CogdoFlyingGameFuelLabel = 'Fuel'
CogdoFlyingGameLegalEagleTargeting = 'Now members can adopt up to 75 puffles!'
CogdoFlyingGameLegalEagleAttacking = 'You can move puffles between'
CogdoFlyingGamePickUpAPropeller = 'your igloo and backyard.'
CogdoFlyingGamePressCtrlToFly = "Your puffles' stats stay the same"
CogdoFlyingGameYouAreInvincible = 'while they\'re in your backyard.'
CogdoFlyingGameTimeIsRunningOut = 'Puffle Creatures'
CogdoFlyingGameMinimapIntro = 'Many puffle creatures have been discovered, but there could be even more out there!'
CogdoFlyingGameMemoIntro = 'Puffle creatures can dig'
CogdoFlyingGameOutOfTime = 'for rare treasures.'
CogdoFlyingGameYouMadeIt = 'Members can adopt some puffle creatures from the Wild Puffle Reserve. They can be cared for at the Puffle Hotel.'
CogdoFlyingGameYouMadeIt = 'Puffle Park'
CogdoFlyingGameTakingMemos = 'Walk their puffle creatures and care for them in the Puffle Hotel'
CogdoElevatorRewardLaff = 'Bring their puffle creatures into their igloo'
CogdoExecutiveSuiteTitle = 'Taking puffle creatures out of the backyard requires a paid membership.'
CogdoExecutiveSuiteIntroMessage = "OK"
CogdoExecutiveSuiteToonThankYou = 'Thanks for the rescue!\nIf you need help in a fight, use this SOS card to call my friend %s.'
CogdoExecutiveSuiteToonBye = 'Bye!'
SillySurgeTerms = {1: 'Puffle Park',
 2: 'Puffle Tricks',
 3: 'Adopt a puffle and walk it to perform tricks!',
 4: 'Go to Pet Shop',
 5: 'Walk your puffle to perform tricks!',
 6: 'Go to igloo',
 7: 'You have more items to unlock.',
 8: 'You can use your code later, but will need to choose new items.',
 9: 'Still want to quit?',
 10: 'Penguin is playing in the Puffle Park',
 11: 'Puffle Park',
 12: 'Cracked-Uptick!'}
InteractivePropTrackBonusTerms = {0: 'Puffle Tricks',
 1: '',
 2: '',
 3: '',
 4: 'Take your pet for a walk and click the puffle icon to perform tricks!',
 5: 'Nuzzle',
 6: ''}
PlayingCardUnknown = 'Speak'
