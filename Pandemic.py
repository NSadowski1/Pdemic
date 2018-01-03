'''
Pandemic
Nicholas Sadowski
Created:
Last Edited: 12/28/2017
'''
#Imports
import random
import tkinter
import sys
import traceback

#Variables
cure= {'Red' : False,'Blue' : False, 'Yellow' : False, 'Black' : False}
cubes = {'Red' : 0, 'Blue' : 0, 'Yellow' : 0, 'Black' : 0}
Epidemic =0
Outbreaks = 0
discard_pile =[]
research_stations = 5

class Suppressor(object):
    def __enter__(self):
        self.stdout= sys.stdout
        sys.stdout = self

    def __exit__(self,type,value,traceback):
        sys.stdout = self.stdout

    def write(self,x):
        pass

class city():
    cities = []
    def __init__ (self,name,cube,color,connections,research_station,protected,outbreaked = False):
        self.name = name
        self.cube = cube
        self.color = color
        self.connections = connections
        self.research_station = research_station
        self.protected = protected
        self.outbreaked = outbreaked
        city.cities.append(self)

    def add_cube(self,color):
        if self.cube[color]==3 and not self.protected:
            print(self.name + " had an outbreak\n")
            self.outbreak(color)
        elif not self.protected:
            print(self.name + ' had one ' + color + ' cube added')
            self.cube[color] +=1
            cubes[color] +=1
        else:
            print(self.name + ' was protected by quarinitine')

    def outbreak(self,color):
        global Outbreaks
        self.outbreaked = True
        Outbreaks += 1
        for city in self.connections:
            if not city.outbreaked:
                city.add_cube(color)
            else:
                print(city.name + ' has already outbreaked.')

    def info(self):
        print('Name:' + 20*' ' + self.name)
        print('Color:' + ' ' * 19 + self.color)
        print('Cubes:')
        for key in self.cube:
            print(key + (25-len(key)) * ' ' + str(self.cube[key]))
        print('Connections:')
        for city in self.connections:
            print(city.name)
        print('Research Station:' + 8 * ' ' + str(self.research_station))
        print('Protected:' + 15 * ' ' + str(self.protected))
        
            
        
        

#creating cities
#Blue cities
Atlanta = city('Atlanta',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Blue',[],True,False)
Chicago = city('Chicago',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Blue',[],False,False)
Washington = city('Washington',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Blue',[],False,False)
New_York = city('New York',{'Red':0,"Blue":0,"Yellow":0,"Black":0},"Blue",[],False,False)
San_Francisco = city('San Francisco',{'Red':0,"Blue":0,"Yellow":0,"Black":0},"Blue",[],False,False)
Montreal = city('Montreal',{'Red':0,"Blue":0,"Yellow":0,"Black":0},'Blue',[],False,False)
Madrid = city('Madrid',{'Red':0,"Blue":0,"Yellow":0,"Black":0},'Blue',[],False,False)
London = city('London',{'Red':0,"Blue":0,"Yellow":0,"Black":0},'Blue',[],False,False)
Essen = city('Essen',{'Red':0,"Blue":0,"Yellow":0,"Black":0},'Blue',[],False,False)
St_Petersburg = city('St Petersburg',{'Red':0,"Blue":0,"Yellow":0,"Black":0},'Blue',[],False,False)
Milan = city('Milan',{'Red':0,"Blue":0,"Yellow":0,"Black":0},'Blue',[],False,False)
Paris = city('Paris',{'Red':0,"Blue":0,"Yellow":0,"Black":0},'Blue',[],False,False)
#Yellow cities
Miami= city('Miami',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Yellow',[],False,False)
Los_Angeles = city('Los Angeles',{'Red':0,"Blue":0,"Yellow":0,"Black":0},'Yellow',[],False,False)
Mexico_City = city('Mexico City',{'Red':0,"Blue":0,"Yellow":0,"Black":0},'Yellow',[],False,False)
Bogota = city('Bogota',{'Red':0,"Blue":0,"Yellow":0,"Black":0},'Yellow',[],False,False)
Lima = city('Lima',{'Red':0,"Blue":0,"Yellow":0,"Black":0},'Yellow',[],False,False)
Santiago = city('Santiago',{'Red':0,"Blue":0,"Yellow":0,"Black":0},'Yellow',[],False,False)
Buenos_Aires = city('Buenos Aires',{'Red':0,"Blue":0,"Yellow":0,"Black":0},'Yellow',[],False,False)
Sao_Paulo = city('Sao Paulo',{'Red':0,"Blue":0,"Yellow":0,"Black":0},'Yellow',[],False,False)
Lagos = city('Lagos',{'Red':0,"Blue":0,"Yellow":0,"Black":0},'Yellow',[],False,False)
Kinshasa = city('Kinshasa',{'Red':0,"Blue":0,"Yellow":0,"Black":0},'Yellow',[],False,False)
Johannesburg = city('Johannesburg',{'Red':0,"Blue":0,"Yellow":0,"Black":0},'Yellow',[],False,False)
Khartoum = city('Kartoum',{'Red':0,"Blue":0,"Yellow":0,"Black":0},'Yellow',[],False,False)
#Black cities
Algiers = city('Algiers',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Black',[],False,False)
Baghdad = city('Baghdad',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Black',[],False,False)
Cairo = city('Cairo',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Black',[],False,False)
Istanbul = city('Istanbul',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Black',[],False,False)
Moscow = city('Moscow',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Black',[],False,False)
Tehran = city('Tehran',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Black',[],False,False)
Riyadh = city('Riyadh',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Black',[],False,False)
Delhi = city('Delhi',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Black',[],False,False)
Mumbai = city('Mumbai',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Black',[],False,False)
Kolkota = city('Kolkota',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Black',[],False,False)
Chennai = city('Chennai',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Black',[],False,False)
Karachi = city('Karachi',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Black',[],False,False)
#Red Cities
Bangkok = city('Bangkok',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Red',[],False,False)
Beijing = city('Beijing',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Red',[],False,False)
Ho_Chi_Minh_City = city('Ho Chi Minh City',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Red',[],False,False)
Hong_Kong= city('Hong Kong',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Red',[],False,False)
Jakarta = city('Jakarta',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Red',[],False,False)
Manila = city('Manila',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Red',[],False,False)
Osaka = city('Osaka',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Red',[],False,False)
Seoul = city('Seoul',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Red',[],False,False)
Shanghai = city('Shanghai',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Red',[],False,False)
Sydney = city('Sydney',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Red',[],False,False)
Taipei = city('Taipei',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Red',[],False,False)
Tokyo = city('Tokyo',{'Red':0,'Blue':0,'Yellow':0,'Black':0},'Red',[],False,False)

#Assigning Connections
Atlanta.connections = [Chicago,Washington,Miami]
Chicago.connections = [Atlanta,San_Francisco,Montreal,Los_Angeles,Mexico_City]
Washington.connections = [Atlanta,Montreal,New_York,Miami]
New_York.connections = [Montreal,Washington,Madrid,London]
San_Francisco.connections = [Los_Angeles,Chicago,Tokyo,Manila]
Montreal.connections = [Chicago,Washington,New_York]
Madrid.connections = [New_York,London,Paris,Algiers,Sao_Paulo]
London.connections = [New_York,Essen,Paris,Madrid]
Essen.connections = [London,St_Petersburg,Milan,Paris]
St_Petersburg.connections = [Essen,Istanbul,Moscow]
Milan.connections = [Essen,Istanbul,Paris]
Paris.connections = [London,Essen,Milan,Algiers,Madrid]
Miami.connections = [Washington,Bogota,Mexico_City,Atlanta]
Los_Angeles.connections = [Sydney,San_Francisco,Chicago,Mexico_City]
Mexico_City.connections = [Los_Angeles,Chicago,Miami,Bogota,Lima]
Bogota.connections = [Miami,Sao_Paulo,Buenos_Aires,Lima,Mexico_City]
Lima.connections = [Mexico_City,Bogota,Santiago]
Santiago.connections = [Lima]
Buenos_Aires.connections = [Bogota,Sao_Paulo]
Sao_Paulo.connections = [Bogota,Buenos_Aires,Madrid,Lagos]
Lagos.connections = [Sao_Paulo,Kinshasa,Khartoum]
Kinshasa.connections = [Lagos,Khartoum,Johannesburg]
Johannesburg.connections = [Kinshasa,Khartoum]
Khartoum.connections = [Lagos,Kinshasa,Johannesburg,Cairo]
Algiers.connections = [Madrid,Paris,Istanbul,Cairo]
Baghdad.connections = [Istanbul,Tehran,Karachi,Riyadh,Cairo,]
Cairo.connections = [Khartoum,Algiers,Istanbul,Baghdad,Riyadh]
Istanbul.connections = [Milan,St_Petersburg,Moscow,Baghdad,Cairo,Algiers]
Moscow.connections = [St_Petersburg,Tehran,Istanbul]
Tehran.connections = [Moscow,Delhi,Karachi,Baghdad]
Riyadh.connections = [Cairo,Baghdad,Karachi]
Delhi.connections = [Tehran,Kolkota,Chennai,Mumbai,Karachi]
Mumbai.connections = [Chennai,Delhi,Karachi]
Kolkota.connections = [Delhi,Hong_Kong,Bangkok,Chennai]
Chennai.connections = [Delhi,Kolkota,Bangkok,Jakarta,Mumbai]
Karachi.connections = [Baghdad,Tehran,Delhi,Mumbai,Riyadh]
Bangkok.connections = [Kolkota,Hong_Kong,Ho_Chi_Minh_City,Jakarta,Chennai]
Beijing.connections = [Seoul,Shanghai]
Ho_Chi_Minh_City.connections = [Bangkok,Manila,Jakarta,Hong_Kong]
Jakarta.connections = [Sydney,Ho_Chi_Minh_City,Chennai]
Manila.connections = [Taipei,Sydney,Ho_Chi_Minh_City,San_Francisco,Hong_Kong]
Osaka.connections = [Tokyo,Taipei]
Seoul.connections = [Beijing,Shanghai,Tokyo]
Shanghai.connections = [Beijing,Seoul,Tokyo,Taipei,Hong_Kong]
Sydney.connections = [Jakarta,Manila,Los_Angeles]
Taipei.connections = [Osaka,Shanghai,Hong_Kong,Manila]
Tokyo.connections = [Seoul,Shanghai,Osaka,San_Francisco]




#Classes
class pawn:
    players = []
    def __init__(self,hand = None,location = Atlanta,moves = 4, role = ''):
        self.location = location
        self.hand = hand
        if self.hand == None:
            self.hand = []          #list of card objects
        self.moves= moves
        self.role = role
        pawn.players.append(self)

    def pickup_cube(self,color = None):
        if color == None:
            color = self.location.color
        if self.location.cube[color] != 0 and not cure[self.location.color]:
            self.location.cube[self.location.color] -= 1
            self.moves -= 1
            self.check_moves()
        elif self.location.cube[color] == 0:
             print("The city is not infected.")
        else:
            self.location.cube[color] = 0
            self.moves -= 1
            self.check_moves()

    def cure(self,color):
        same_color = 0
        if not cure[color]:
            for card in self.hand:
                if card.color == color:
                    same_color += 1
            if same_color >= 5:
                 cure[color]=True
                 self.moves -=1
                 self.check_moves()
            else:
                 print("You do not have enough cards")
        else:
            print("That color is already cured")
            
    def give(self,other,card):
        if self.location == other.location:
            if self.location.name == card.name:
                if card in self.hand:
                    self.hand.remove(card)
                    other.hand.append(card)
                    self.moves -= 1
                    other.hand.check_cards()
                else:
                    print('You do not have that card.')
            else:
                print("You are not in the city of the card you want to give.")
        else:
            print("You are not in the same city to trade.")

    def take(self,other,card):
        if self.location == other.location:
            if self.location.name == card.name or other.role == 'Researcher':
                if card in other.hand:
                    self.hand.append(card)
                    other.hand.append(card)
                    self.moves -= 1
                    self.hand.check_cards()
                else:
                    print('The other player does not have ' + card.name)
            else:
                print('You are not in the city of the card you want to take')
        else:
            print('You are not in the same city as the other player.')
            
        
    def build_research(self):
        valid = False
        if not self.location.research_station:
            for card in self.hand:
                if self.location.name == card.name:
                    valid = True
                    city = card
            if valid:
                if research_stations > 0:
                    research_stations -= 1
                    self.location.research_station = True
                    self.hand.remove(city)
                    self.moves-=1
                    self.check_moves()
                else:
                    print('You do not have any more research stations to build.\n The limit is six')
            else:
                print("You do not have the card to build the research station.")
        else:
            print("There is already a reseach station there.")
            

    def move(self,destination):
        if destination in self.location.connections:
            self.location = destination
            self.moves -= 1
            self.check_moves()
        elif destination.research_station and self.location.research_station:
            self.location = destination
            self.moves -=1
            self.check_moves()
        else:
            print("You are not able to move there.")

    def card_move(self,destination,using):
        if using in self.hand:
            if destination.name == using.name:
                self.location = destination
                self.moves -= 1
                self.check_moves()
                self.hand.remove(using)
            elif self.location.name == using.name:
                self.location = destination
                self.moves -= 1
                self.check_moves()
                self.hand.remove(using)
            else:
                print('You can not move there using that card.')
        else:
            print('You do not have that card')
            

    def add_card(self,number=2):
        for a in range(number):
            self.hand.append(player_deck.deal())
            print('You were dealt ' + self.hand[-1].name)

    def check_moves(self):
        if self.moves ==0:
            self.add_card()
            self.moves = 4

    def check_cards(self):
        while len(self.hand) > 7:
            print("You have too many cards.")
            print("Your cards are :")
            for card in hand:
                print(card + " : " + card.color)
            dispose = input("What card would you like to discard?")
            self.hand.remove(dispose)

    def look_at_hand(self):
        print('The follwing cards are in you hand.\n')
        for card in self.hand:
            print(card.name + ' '*(25-len(card.name)) + card.color)
        if len(self.hand) == 0:
            print('You do not have any cards')
        
    def look_at_location(self):
        print('You are in ' + self.location.name+'\n')

    def where_can_I_go(self):
        print('You can move to: ')
        for city in self.location.connections:
            print(city.name + " "*(25-len(city.name)) +city.color)
        
    def info(self):
        self.look_at_hand()
        self.look_at_location()
        self.where_can_I_go()
        print('You have ', self.moves, ' moves left.')

    def use_airlift(self,movee,destination):
        if airlift in self.hand:
            self.hand.remove(airlift)
            movee.location = destination
        else:
            print('You do not have the Airlift Card.')

    #def use_one_quiet_night(self):

    def use_government_grant(self,target):
        if government_grant in self.hand:
            if not target.research_station:
                target.research_station = True
                self.hand.remove(government_grant)
            else:
                print('There is already a research station in ' + target.name)
        else:
            print('You do not have the Government Grant Card')

    def use_forcast(self):
        forecasted = []
        print('The next cities to be infected are:')
        for a in range(6):
            forecasted.append(infection_deck.cards.pop())
            print(i + ' ' + next[i].name)
        order = input('Enter the order you want the cards to be pulled in. (ex. 326145)')
        for ch in order:
            infection_deck.cards.forecasted[int(ch)]

    def use_resilient_population(self,city):
        if resilient_population in self.hand:
            if city in infection_deck.discarded:
                infection_deck.append(city)
                infection_deck.discarded.remove(city)
            else:
                print(city.name + 'has not been called yet')
        print('You do not have the Resilient Population card.')        
            
        
            
class medic(pawn):
    role = 'Medic'
    def __init__(self):
        pawn.__init__(self)
        self.role = 'medic'
        
    def cure(self,color):
        if not cure[color]:
            for card in self.hand:
                if card.color == color:
                    same_color += 1
            if same_color >= 5:
                 cure[color]=True
                 self.moves -=1
                 self.check_moves()
                 for key in self.location.cube:
                     if cure[key]:
                         self.location.cube[key]=0
            else:
                 print("You do not have enough cards")
        else:
            print("That color is already cured")
            
    def move(self,destination):
        if destination in self.location.connections:
            self.location = destination
            self.moves -= 1
            self.check_moves()
            for key in self.location.cube:
                if cure[key]:
                    self.location.cube[key]=0
        elif destination.research_station and self.location.research_station:
            self.location = destination
            self.moves -=1
            self.check_moves()
            for key in self.location.cube:
                if cure[key]:
                    self.location.cube[key]=0
        else:
            print("You are not able to move there.")

    def card_move(self,destination,using):
        if destination.name == using.name:
            self.location = destination;
            self.moves -= 1
            self.check_moves()
            self.hand.remove(using)
            for key in self.location.cube:
                if cure[key]:
                    self.location.cube[key]=0
        elif self.location == using:
            self.location = destination
            self.moves -= 1
            self.check_moves()
            self.hand.remove(using)
            for key in self.location.cube:
                if cure[key]:
                    self.location.cube[key]=0
        else:
            print('You are not able to move there.')
        
            
class quarintine(pawn):
    role = 'Quarintine'
    def __init__(self):
        pawn.__init__(self)
        self.role = "quarintine"
    def protect(self):
        for city in self.location.connections:
            city.protected = True
            
class ops(pawn):
    role = 'Ops'
    def __init__(self):
        pawn.__init__(self)
        self.role = "ops"
    def build_research(self):
        if self.position.reasearch_station:
            print('There is already a research station here.')
        elif research_stations == 0:
            print('You cannot build any more research stations.')
        else:
            research_stations -= 1 
            self.position.research_station = True
            self.moves -= 1
            self.check_moves()
        
    def research_move(self,destination,card):
        if self.postion.reasearch_station:
            self.position = destination
            self.moves -= 1
            self.check_moves()
            self.hand.remove(card)
        else:
            print('You must be on a research station to do that.')
        
class dispatcher(pawn):
    role = 'Dispatcher'
    def __init__(self):
        pawn.__init__(self)
        self.role = "dispactcher"
    def move_other(self,other,destination):
        if destination in other.location.connections:
            other.location = destination
            self.moves -= 1
        else:
            print('The other person cannont move there.')

    def teleport(self,travler,destination):
        self.moves -= 1
        travler.location = destination.location
        self.checkmoves()

class researcher(pawn):
    role = 'Researcher'
    def __init__(self):
        pawn.__init__(self)
        self.role = "researcher"


class scientist(pawn):
    role = "Scientist"
    def __init__(self):
        pawn.__init__(self)
        self.role = "scientist"
    def cure(self,color):
        if not(cure(color)):
            for card in hand:
                if card.color == color:
                    same_color += 1
            if same_color >= 4:
                 cure[color]=True
                 self.moves -=1
                 self.check_moves()
            else:
                 print("You do not have enough cards")
        else:
            print("That color is already cured")
        

class contingency_planner(pawn):
    role = 'Contingency Planner'
    def __init__(self):
        pawn.__init__(self)
        self.role="contingency_planner"
        self.saved= None 

    def save_card(self,card):
        if card in event_cards:
            if card in player_deck.discarded:
                if self.saved ==None:
                    self.saved = card
                    player_deck.discarded.remove(card)
                    self.moves -= 1
                    self.check_moves()
                else:
                    print('You are already have a card saved')
            else:
                print('That card is not in the discard pile.')

    def use_airlift(self,movee,destination):
        if airlift in self.hand:
            self.hand.remove(airlift)
            movee.location = destination
        elif self.saved == airlift:
            self.saved = None
            movee.location = destination
        else:
            print('You do not have the Airlift Card.')

    #def use_one_quiet_night(self):

# finish saved check
    def use_government_grant(self,target):
        if government_grant in self.hand:
            if not target.research_station:
                target.research_station = True
                self.hand.remove(government_grant)
            else:
                print('There is already a research station in ' + target.name)
        else:
            print('You do not have the Government Grant Card')

    def use_forcast(self):
        forecasted = []
        print('The next cities to be infected are:')
        for a in range(6):
            forecasted.append(infection_deck.cards.pop())
            print(i + ' ' + next[i].name)
        order = input('Enter the order you want the cards to be pulled in. (ex. 326145)')
        for ch in order:
            infection_deck.cards.forecasted[int(ch)]

    def use_resilient_population(self,city):
        if resilient_population in self.hand:
            if city in infection_deck.discarded:
                infection_deck.append(city)
                infection_deck.discarded.remove(city)
            else:
                print(city.name + 'has not been called yet')
        print('You do not have the Resilient Population card.')   
        
                
            



class deck():
    decks = []
    def __init__(self,name,cards,discarded,removed=None):
        self.name = name
        self.discarded = discarded
        self.cards = cards
        self.removed = removed
        deck.decks.append(self)

    def deal(self):
        a = self.cards.pop()
        self.discarded.append(a)
        return a

    def shuffle_all(self):
        self.cards = self.cards + self.discarded
        self.discarded.clear()
        random.shuffle(self.cards)
        

    def shuffle_in(self):
        random.shuffle(self.discarded)
        self.cards = self.cards+self.discarded
        self.discarded.clear()

    def look_at_cards(self):
        for a in self.cards:
            print(a.name)
        print(len(self.cards))

    def check_discarded(self):
        print('The following cards are in the discard pile.')
        for card in self.discarded:
            for player in pawn.players:
                for a in player.hand:
                    if a == card:
                        break
                else:
                    print(card.name)

    def bottom_deal(self):
        a = self.cards.pop(0)
        self.discarded.append(a)
        return a

                        
            
        

class card():
    cards = []
    def __init__(self,name,color):
        self.name = name
        self.color = color
        card.cards.append(self)



#Creating cards
resilient_population = card('Resilient Population','Event Card')
airlift=card('Airlift','Event Card')
government_grant = card('Government Grant','Event Card')
one_quiet_night = card('One Quiet Night','Event Card')
forecast = card('Forecast','Event Card')
atlanta = card('Atlanta','Blue')
chicago = card('Chicago','Blue')
washington = card('Washington','Blue')
new_york = card('New York', 'Blue')
san_francisco = card('San Francisco','Blue')
montreal = card('Montreal','Blue')
madrid = card('Madrid','Blue')
london = card('London','Blue')
essen = card('Essen','Blue')
st_petersburg = card('St Petersburg','Blue')
milan = card('Milan','Blue')
paris = card('Paris', 'Blue')
miami = card('Miami', 'Yellow')
los_angeles = card('Los Angeles','Yellow')
mexico_city = card('Mexico City','Yellow')
bogota = card('Bogota', 'Yellow')
lima = card('Lima','Yellow')
santiago = card('Santiago','Yellow')
buenos_aires = card('Buenos Aires', 'Yellow')
sao_paulo = card('Sao Paulo','Yellow')
lagos = card('Lagos','Yellow')
kinshasa = card('Kinshasa', 'Yellow')
johannesburg =  card('Johannesburg', 'Yellow')
kartoum = card('Kartoum','Yellow')
algiers = card('Algiers','Black')
baghdad = card('Baghdad','Black')
cairo = card('Cairo','Black')
istanbul = card('Istanbul','Black')
moscow = card('Moscow','Black')
tehran = card('Tehran','Black')
riyadh = card('Riyadh','Black')
delhi = card('Delhi', 'Black')
mumbai = card('Mumbai','Black')
kolkota = card('Kolkota','Black')
chennai = card('Chennai','Black')
karachi = card('Karachi','Black')
bangkok = card('Bangkok','Red')
beijing = card('Beijing','Red')
ho_chi_minh_city = card('Ho Chi Minh City','Red')
hong_kong = card('Hong Kong','Red')
jakarta = card('Jakarta','Red')
manila = card('Manila','Red')
osaka = card('Osaka','Red')
seoul = card('Seoul','Red')
shanghai = card('Shanghai','Red')
sydney = card('Sydney','Red')
taipei = card('Taipei','Red')
tokyo = card('Tokyo','Red')

event_cards = [resilient_population,airlift,government_grant,one_quiet_night,forecast]

#Creating Decks
infection_deck = deck('Infection Deck',city.cities,[],[])
player_deck = deck('Player Deck',card.cards,[],[])

options = [medic,ops,quarintine,dispatcher,contingency_planner,scientist]


def infect(number_cities = 2,num_cubes = 1):
    infected = []
    for i in range(number_cities):
        a = infection_deck.deal()
        infected.append(a)
        for b in range(num_cubes):
            a.add_cube(a.color)
    with Suppressor():
        return infected

def intial_infect():
    intial = []
    numbers = ['three','two','one']
    for a in range(3):
        with Suppressor():
            intial.append(infect(3,3-a))
    for a in range(3):
        print('The follwing cities got ',numbers[a],' cubes:')
        for b in intial[a]:
            print(b.name)
    
def epidemic():
    global Epidemic
    Epidemic +=1
    a = infection_deck.bottom_deal()
    for b in range(3):
        a.add_cube(a.color)
    infection_deck.shuffle_in()
    
            
            
        

def set_up_game():
    infection_deck.shuffle_all()
    player_deck.shuffle_all()
    num_players = int(input('How many players are there?'))
    while num_players > 4 or num_players < 1:
        print(num_players,' is not a valid number of players.')
        print('There can be 1 - 4 players.')
        num_players = int(input('How many players are there?'))
    for player in range(num_players):
        print('The following roles are available.')
        for i in range(len(options)):
            print(i,': ',options[i].role)
        choice = int(input('Please type the number of the role you would like.'))
        options[choice]()
        pawn.players[player].add_card()
        options.remove(options[choice])
    intial_infect();
    
            
            
            

'''
To Do
Contingency info
Quarintine info
epidemic function + cards
GUI
reset outbreaked value

'''


#Testing Suite
def check_decks():
    for a in deck.decks:
        a.look_at_cards()
    for a in infection_deck.cards:
        for b in player_deck.cards:
            if a.name == b.name:
                infection_deck.cards.remove(a)
                player_deck.cards.remove(b)    
    for a in deck.decks:
        a.look_at_cards()

