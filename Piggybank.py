import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import *
from kivy.uix.accordion import *
from kivy.uix.layout import *
from kivy.uix.gridlayout import *
from kivy.uix.boxlayout import *
from kivy.graphics import Color
from kivy.uix.widget import *
from kivy.uix.button import Button
from kivy.uix.scrollview import *
from kivy.factory import Factory
from random import random
from kivy.graphics import *
from kivy.properties import *
from kivy.uix.textinput import TextInput
from kivy.uix.tabbedpanel import *
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import *
from kivy.uix.switch import *
from kivy.uix.spinner import Spinner
from functools import partial
from kivy.core.image import *
from os.path import join
from kivy.uix.label import *
from kivy.clock import *
from kivy.base import *
from kivy.uix.dropdown import DropDown
import copy
from kivy.uix.checkbox import *
import time
import cPickle as pickle
import random
from kivy.uix.progressbar import *
from kivy.uix.bubble import *
from kivy.uix.floatlayout import *
import math
from kivy.uix.popup import *
from kivy.config import Config

# This is where I create a large majority of my GUI layout for the
#program, I specify many unnamed classes that kivy can interpret
#and build the program

#A note on styling: Some of these lines are way over 80 charachters
#because kivy does not support mutiline input in the load string
Builder.load_string("""
<MenuScreen>:
    GridLayout:
        rows: 4
        orientation: 'vertical'
        
        GridLayout:
            cols: 3
            size_hint: (1,.3)
            
            Image:
                source: 'C:/Users/Public/Documents/piggy-bank.png'
                keep_data: True
                size_hint: (.2,1)
            
            Label:
                text: 'PiggyBank'
                color: (1,0,.5,1)
                font_size: 28
                bold: True
            
            Image:
                source: 'C:/Users/Public/Documents/piggy-bank.png'
                keep_data: True
                size_hint: (.2,1)
            
        StatusAndProgressWrapper:
            size_hint: (1,1.2)
        
        GridLayout:
            rows: 2
            cols: 2
            
            BudgetHelperButton:
                text: 'Budget'
                on_press: root.manager.current = 'budget'
                background_color: (1,0,.6,1)
                font_size: 14
                
            Button:
                text: 'Status Detail'
                on_press: root.manager.current = 'status'
                background_color: (1,0,.6,1)
                font_size: 14
            Button:
                text: 'History'
                on_press: root.manager.current = 'data'
                background_color: (1,0,.6,1)
                font_size:14
            Button:
                text: 'Ledger'
                on_press: root.manager.current = 'revenue'
                background_color: (1,0,.6,1)
                font_size:14
        QuitButton:
            size_hint:(1,.25)
            background_color: (1,0,.6,1)
            font_size:14

<BudgetScreen>:
    GridLayout:
        rows: 5
        
        GridLayout:
            rows: 1
            size_hint: (1,.1)

            Button:
                text: 'Back'
                on_press: root.manager.current = 'menu'
            Button:
                text: 'Configure Budget'
                on_press: root.manager.current = 'configure budget'
        
        Label:
            text: '[size=22][b]Monthly Budget[/b][/size]'
            markup: True
            size_hint: (1,.1)
                
        MyBudgetGraphWrapper:
            size_hint:(1,.6)
        
        MyRevenueStateLabelWrapper:
            size_hint: (1,.1)
        
        GridLayout:
            rows: 1
            size_hint: (1,.1)
            
            Button:
                text: 'My Goals'
                on_press: root.manager.current = 'goals'
            Button:
                text: 'Configure Revenue'
                on_press: root.manager.current = 'configure revenue'

<ConfigureBudgetScreen>
    GridLayout:
        orientation: 'vertical'
        rows: 3
            
        GridLayout:
            size_hint:(1,.1)
            orientation: 'horizontal'
            rows: 1
                
            Button:
                text: 'Back'
                on_press: root.manager.current = 'budget'
                    
            Button:
                text: 'Main Menu'
                on_press: root.manager.current = 'menu'
        MyBudgetLayout:
            size_hint:(1,.8)
            cols:2
                        
        MySaveButton:
            text: 'Save Changes'
            size_hint: (1,.1)
            on_press: root.manager.current = 'budget'

<ConfigureRevenueScreen>
    GridLayout:
        rows: 3
        
        GridLayout:
            size_hint: (1,.1)
            rows: 1
            
            Button:
                text: 'Back'
                on_press: root.manager.current = 'budget'
            Button:
                text: 'Main Menu'
                on_press: root.manager.current = 'menu'
                
        MyConfigureRevenueLayout:
            size_hint: (1,.8)
            
        MyConfigureRevenueSubmitButton:
            size_hint: (1,.1)
            text: 'Save Changes'
            on_press: root.manager.current = 'budget'
                     
<ConfigureGoalsScreen>
    GridLayout:
        orientation: 'vertical'
        rows: 3
            
        GridLayout:
            size_hint:(1,.1)
            orientation: 'horizontal'
            rows: 1
                
            Button:
                text: 'Back'
                on_press: root.manager.current = 'budget'
                    
            Button:
                text: 'Main Menu'
                on_press: root.manager.current = 'menu'
        MyGoalsLayout:
            size_hint:(1,.8)
            cols:2
                        
        MySaveGoalsButton:
            text: 'Save Changes'
            size_hint: (1,.1)
            on_press: root.manager.current = 'budget'
            
<DataScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        GridLayout:
            rows: 1
            size_hint: (1, .1)
        
            LineGraphButton:
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'

        Accordion:
            orientation: 'vertical'
                    
            AccordionItem:
                background_selected:
                    'C:/Users/Public/Documents/pink_background.jpg'
                title: 'This Month'
                GridLayout:
                    orientation: 'vertical'
                    rows: 3
                    
                    Label:
                        bold: True
                        text: 'Progress This Month'
                        font_size: 13
                        size_hint: (1,.1)
                    MonthlyGraphWrapper:
                        size_hint:(1,.8)
                    Label:
                        size_hint:(1,.1)
                        text:'0      3     6     9     12    15    18    21   24    27    30    33     '
                    
            AccordionItem:
                background_selected:
                    'C:/Users/Public/Documents/pink_background.jpg'
                title: 'This Year'
                GridLayout:
                    orientation: 'vertical'
                    rows: 3
                    
                    Label:
                        bold: True
                        text: 'Progress this Year'
                        font_size:13
                        size_hint: (1,.1)
                        
                    YearlyGraphWrapper:
                        size_hint: (1,.8)
                    Label:
                        size_hint: (1,.1)
                        text: 'Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec    '
    
<RevenueScreen>:
    GridLayout:
        orientation: 'vertical'
        rows: 3
        
        GridLayout:
            rows: 1
            size_hint:(1,.1)
            
            Button:
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'
            Button:
                text: 'Add new'
                on_press: root.manager.current = 'new revenue'
        MyScrollBox:
        
        GridLayout:
            rows: 1
            size_hint:(1,.1)
            
            ChangeViewButton:
                text: 'View Revenue'
            ChangeViewButton:
                text: 'View Expenditures'
            ChangeViewButton:
                text: 'View All'
            
<AddNewRevenueScreen>:
    GridLayout:
        orientation: 'vertical'
        rows: 2
        
        GridLayout:
            size_hint:(1,.1)
            orientation: 'horizontal'
            rows: 1
            
            MyRevenueBackButton:
                text: 'Back'
                on_press: root.manager.current = 'revenue'
                
            MyRevenueBackButton:
                text: 'Main Menu'
                on_press: root.manager.current = 'menu'
        GridLayout:
            rows: 2
            
            GridLayout:
                cols:2
                
                Label:
                    text: 'Revenue or Expense'
                    
                MyTypeSpinnerWrapper:
                
                Label:
                    text: 'Category'
                    
                MyCategorySpinnerWrapper:
                    
                Label:
                    text: 'Currency Used'
                    
                MyCurrencySpinnerWrapper:
                
                Label:
                    text: 'Amount (0.00)'
                    
                MyAmountTextInputWrapper:
                
                Label:
                    text: 'Description'
                MyDescriptionTextInputWrapper:
                
                Label:
                    text: 'Date (MM/DD/YYYY)'
                MyDateTextInputWrapper:
                    
            MySubmitButton:
                on_press: root.manager.current = 'revenue'

<StatusScreen>:
    GridLayout:
        rows: 2
        
        Button:
            size_hint: (1,.1)
            text: 'Back to main menu'
            on_press: root.manager.current = 'menu'
            
        MyStatusDetailWrapper:

""")

# Declare screens
class MenuScreen(Screen):
    pass

class BudgetScreen(Screen):
    pass

class DataScreen(Screen):
    pass

class RevenueScreen(Screen):
    pass

class AddNewRevenueScreen(Screen):
    pass

class ConfigureBudgetScreen(Screen):
    pass

class ConfigureRevenueScreen(Screen):
    pass

class ConfigureGoalsScreen(Screen):
    pass

class StatusScreen(Screen):
    pass

#When the line graph back button is pressed,
#the little position bubbles go away
class LineGraphButton(Button):
    def on_press(self,**kwargs):
        yearlyGraph.dispatch('on_update')
        monthlyGraph.dispatch('on_update')
        pass

#A wrapper for the monthly graph that creates a
#global to be accessed by other parts of the
#program, thus so it can update continuously
class MonthlyGraphWrapper(BoxLayout):
    def __init__(self,**kwargs):
        super(MonthlyGraphWrapper,self).__init__(**kwargs)
        global monthlyGraph
        monthlyGraph = LineGraph('month')
        self.add_widget(monthlyGraph)

#Same for yearly graph
class YearlyGraphWrapper(BoxLayout):
    def __init__(self,**kwargs):
        super(YearlyGraphWrapper,self).__init__(**kwargs)
        global yearlyGraph
        yearlyGraph = LineGraph('year')
        self.add_widget(yearlyGraph)

#This class is used to draw all four line graphs,
#two each for yearly and monthly
class LineGraph(Widget):
    def __init__(self,stamp,**kwargs):
        super(LineGraph,self).__init__(**kwargs)
        self.dataList = []
        self.maxAmts = []
        self.stamp = stamp
        self.window_size = 350
        self.margin = self.window_size/11
        self.months = ['Jan','Feb','March','April','May',
                       'Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        if self.stamp == 'month': self.numericSpacing = 3
        else: self.numericSpacing = 1
        if self.stamp == 'month':
                self.offset = self.window_size*.25
        else: self.offset = self.window_size/10
        self.on_draw()
        self.register_event_type('on_draw')
        self.register_event_type('on_update')
    
    #Draws the line graph   
    def on_draw(self):
        typeList = ['Expense','Revenue']
        numLists, amtLists = [[],[]], [[],[]]
        self.canvas.clear()
        self.maxAmts = []
        window_size = self.window_size
        self.drawBackground()
        self.drawAxis() #Draws the axis before drawing graph
        for types in xrange(len(typeList)):
            self.dataList = []
            pointsList, amountList = [], []
            self.makeList(types)
            #Check to make sure there is data to graph
            if len(self.dataList) == 0: continue
            myDict = self.makeDict(types)
            numericList = [key for key in myDict]
            numericList = sorted(numericList)
            for element in numericList:
                amountList.append(myDict[element])
            maxAmount = max(amountList)
            self.maxAmts.append(maxAmount)
            if len(self.maxAmts) == 0: continue
            numLists[types], amtLists[types] = numericList, amountList
        self.drawLine(numLists,amtLists)

                    
    #Draws the graph axis on the bottom of the screen
    def drawAxis(self):
        with self.canvas:
            window = self.window_size
            Color(.6,0,.2)
            margin = self.margin
            if self.stamp == 'month':
                offset = window*.25
            else: offset = window/10
            Line(points=[margin,offset,window+margin,offset]
                 ,width=4,cap='square',joint='miter',close=False)
            for x in xrange(1,13):
                Color(.8,0,.4)
                hash_size = .025*window
                Line(points=[margin*(x),offset+hash_size,margin*(x),
                             offset-hash_size],width=2)
    
    def drawBackground(self):
        window_size = self.window_size
        with self.canvas:
            Color(.5,0,.5)
            if self.stamp == 'month': #Custom accordion background
                Rectangle(
                    source='C:/Users/Public/Documents/dark_pink_background.jpg',
                    size=(window_size+100,window_size+75),pos=(0,window_size/10))
            else:
                Rectangle(
                    source='C:/Users/Public/Documents/dark_pink_background.jpg',
                    pos=(0,0), size=(window_size+100,window_size+75))
    
    #Puts together the data list
    def makeList(self,types):
        typeList = ['Expense','Revenue']
        theList = revenuesAndExpedenturesList.getList()
        currentTime = time.localtime()
        if self.stamp == 'month':
            for element in theList:
                (year,month) = element.getMonthAndYear()
                if (year == currentTime[0] and month == currentTime[1]
                    and element.getType()== typeList[types]):
                    self.dataList.append(element) 
        elif self.stamp == 'year':
            for element in theList:
                (year,month) = element.getMonthAndYear()
                if (year == currentTime[0]
                    and element.getType()== typeList[types]):
                    self.dataList.append(element)
    
    #Helper function that makes the data dictionary to be analyzed
    def makeDict(self,types):
        myDict = dict()
        if self.stamp == 'month':
            for element in self.dataList:
                day = element.getDay()
                amount = element.getAmount()
                if day in myDict: myDict[day] += amount
                else: myDict[day] = amount
        elif self.stamp == 'year':
            for element in self.dataList:
                (year,month) = element.getMonthAndYear()
                amount = element.getAmount()
                if month in myDict: myDict[month] += amount
                else: myDict[month] = amount
        return myDict
    
    #Draws the line on the line graph
    def drawLine(self,numLists,amtLists):
        window_size = self.window_size
        typeList = ['Expense','Revenue']
        for types in xrange(len(typeList)):
            numericList = numLists[types]
            amountList = amtLists[types]
            if numericList == [] or amountList == []: continue
            for index in xrange(len(amountList)):
                amountList[index] = ((float(amountList[index])
                                /(max(self.maxAmts)))*window_size+self.offset)
            for index in xrange(len(numericList)):
                numericList[index] = (float(numericList[index]-1)
                                *self.margin/self.numericSpacing+self.margin)
            pointsList = amountList + numericList
            pointsList[::2] = numericList
            pointsList[1::2] = amountList
            with self.canvas:
                if typeList[types] == 'Revenue': Color(0,1,0,.9)
                if typeList[types] == 'Expense': Color(1,0,0,.9)
                Line(points=pointsList,width=3,cap='square',
                     joint='miter',close=False)
        
    #Event handler that allows the bubbles to appear           
    def on_touch_down(self,touch):
        self.clear_widgets()
        try:
            touchLabel = Bubble(pos=(touch.x-50,touch.y),size=(100,50))
            maxAmt = max(self.maxAmts)
            y_pos = maxAmt*(touch.y - self.offset)/float(self.window_size)
            x_pos =  (touch.x-self.margin)*self.numericSpacing/self.margin
            if x_pos < 0 or y_pos < 0:
                return
            if self.stamp == 'year':
                x_pos = self.months[int(x_pos/self.numericSpacing)]
            else:
                x_pos = int(x_pos)
            touchLabel.add_widget(BubbleButton(text=( "(" + str(x_pos) +
                                                     " , $%0.2f)"%y_pos)))
            self.add_widget(touchLabel)
        except:
            return
    
    #Clears all the little bubbles  
    def on_update(self):
        self.clear_widgets()

#Wraps the label on the graph screen that needs to be
#updated continuously to match the current state
class MyRevenueStateLabelWrapper(BoxLayout):
    def __init__(self,**kwargs):
        super(MyRevenueStateLabelWrapper,self).__init__(**kwargs)
        global myRevenueStateLabel
        myRevenueStateLabel = MyRevenueStateLabel()
        self.add_widget(myRevenueStateLabel)

#Shows how the revenue is currently being calculated       
class MyRevenueStateLabel(Label):
    def __init__(self,**kwargs):
        super(MyRevenueStateLabel,self).__init__(**kwargs)
        self.register_event_type('on_update')
        self.font_size = 14
        self.bold = True
        
    def on_update(self):
        state = monthlyRevenue.getToggle()
        revenue = monthlyRevenue.getRevenue()
        if state == 'Calc':
            self.text = ("Based off last month's revenue of $"
                         + ('%0.2f') % (revenue))
        elif state == 'Set':
            self.text = ("Based off a set revenue of $"
                         + ('%0.2f') % (revenue))

#Wraps the status detail screen layout because it
#has to continuously be updated
class MyStatusDetailWrapper(BoxLayout):
    def __init__(self,**kwargs):
        super(MyStatusDetailWrapper,self).__init__(**kwargs)
        global myStatusDetailLayout
        myStatusDetailLayout = MyStatusDetailLayout()
        self.add_widget(myStatusDetailLayout)

#Holds the details of each occupied category as
#specified by the budget and current state,
#is displayed on the status detail screen
class MyStatusDetailLayout(GridLayout):
    def __init__(self,**kwargs):
        super(MyStatusDetailLayout,self).__init__(**kwargs)
        self.register_event_type('on_update')
        self.cols = 1
        self.categoryList = set(["Work","Entertainment","Medical",
                               "Food","Transportation","Utilities",
                               "Charity","Other"])
        self.createDetails()
        self.add_widget(OverflowDetails())
    
    #Used to update the screen   
    def on_update(self):
        self.clear_widgets()
        self.createDetails()
        self.add_widget(OverflowDetails())
    
    #Creates the details about each category and adds it to
    #the layout
    def createDetails(self):
        theList = getAllPercentages.getPercentages()
        for key in theList:
            if key not in self.categoryList:
                continue
            value = theList[key]
            if value == 0:
                continue
            self.add_widget(CategoryDetails(key))        

#Shows the details of a single category for display on
#the status detail screen
class CategoryDetails(GridLayout):
    def __init__(self,name,**kwargs):
        super(CategoryDetails,self).__init__(**kwargs)
        self.cols = 3
        percentages = getAllPercentages.getPercentages()
        percentage = percentages[name]
        revenue = monthlyRevenue.getRevenue()
        if percentage == 0: return
        else: amtToBeSpent = revenue*percentage
        totalSpent = self.getTotalSpent(name)
        spentPercentage = totalSpent/amtToBeSpent
        if totalSpent > amtToBeSpent: myColor = (1,0,0,1)
        else: myColor = (0,1,0,1)
        self.add_widget(Label(text=(str(name) + " spent:\n%"
            + ("%0.2f")%(spentPercentage*100)+ " or\n$"+ str(totalSpent)
            + " out of $" + ("%0.2f")%(amtToBeSpent)),size_hint=(.8,1),
                        text_size=(150,None),bold=True,color=myColor))
        progress = ProgressBar()
        if totalSpent >= (amtToBeSpent):
            progress.max = amtToBeSpent
            progress.value = amtToBeSpent
            overflowAmounts.addAmt(totalSpent - amtToBeSpent)
        else:
            progress.max = amtToBeSpent
            progress.value = totalSpent
        self.add_widget(progress)
        
    def getTotalSpent(self,name):
        totalSpent = 0
        theList = revenuesAndExpedenturesList.getList()
        currentTime = time.localtime()
        for element in theList:
            (year,month) = element.getMonthAndYear()
            if ((currentTime[1] == month) and (currentTime[0] == year)
                and (element.getCategory() == name)):
                totalSpent += element.getAmount()
        return totalSpent

#Shows the details about how much "unrestricted funds" are
#available after subtracting any individual overflow from
#each category
class OverflowDetails(Label):
    def __init__(self,**kwargs):
        super(OverflowDetails,self).__init__(**kwargs)
        self.font_size = 14
        self.bold = True
        self.color = (.5,1,1,1)
        theList = getAllPercentages.getPercentages()
        amtToBeSpent = monthlyRevenue.getRevenue()
        if amtToBeSpent == 0:
            self.text = "No revenue available"
            return
        totalOccupiedPercentage = 0
        for element in theList:
            totalOccupiedPercentage += float(theList[element])
        funds = (1-totalOccupiedPercentage)*amtToBeSpent
        funds -= overflowAmounts.getAmt()
        funds = float(funds)
        percentage = float(funds)/amtToBeSpent
        overflowAmounts.clearAmt()
        percentage = percentage*100
        if funds < 0:
            self.text = (
                "Unrestricted Funds Available: None." +
                "\nYou have spent into your budget by: $%0.2f"
                % abs(funds))
            self.color = (1,0,0,1)
            return
        self.text = ("Unresricted Funds Available: \n$"
                     + ('%0.2f')%funds + " or %" +('%0.2f')%percentage
                     + " of budget")
        self.color = (0,1,0,1)

#Wraps the status info and progress bar on the main screen in
#a global that can be altered by other parts of the program
class StatusAndProgressWrapper(BoxLayout):
    def __init__(self,**kwargs):
        super(StatusAndProgressWrapper,self).__init__(**kwargs)
        global statusAndProgress
        statusAndProgress = StatusAndProgress()
        self.add_widget(statusAndProgress)

#Holds the status info and progress bar in a set layout
class StatusAndProgress(GridLayout):
    def __init__(self,**kwargs):
        super(StatusAndProgress,self).__init__(**kwargs)
        self.cols = 1
        self.on_update()
        self.register_event_type('on_update')
        
    def on_update(self):
        self.clear_widgets()
        self.add_widget(MyStatusLabel())
        self.add_widget(MyBudgetProgressBar(size_hint=(1,.2)))

#Shows how much of the current revenue stream you have spent this month
#on the main screen
class MyBudgetProgressBar(ProgressBar):
    def __init__(self,**kwargs):
        super(MyBudgetProgressBar,self).__init__(**kwargs)
        try:
            self.max = float(monthlyRevenue.getRevenue())
        except:
            self.max = 1
        value = self.getValue()
        if value > self.max:
            self.value = self.max
        else:
            self.value = value
        
    def getValue(self):
        theList = revenuesAndExpedenturesList.getList()
        currentTime = time.localtime()
        totalSpent = 0
        for index in xrange(len(theList)):
            element = theList[index]
            (year,month) = element.getMonthAndYear()
            if (currentTime[1] == month) and (currentTime[0] == year):
                totalSpent += element.getAmount()
        return totalSpent

#Holds the layout for the budget screen, including
#each input label and way of getting information from the user
class MyBudgetLayout(GridLayout):
    def __init__(self,**kwargs):
        super(MyBudgetLayout,self).__init__(**kwargs)
        self.add_widget(Label(text="Add work\nAmount (0.00)"))
        global workPercentage
        workPercentage = MyWorkTextInput()
        self.add_widget(workPercentage)
        self.add_widget(Label(text="Add entertainment\nAmount (0.00)"))
        global entertainmentPercentage
        entertainmentPercentage = MyEntertainmentTextInput()
        self.add_widget(entertainmentPercentage)
        self.add_widget(Label(text="Add medical\nAmount (0.00)"))
        global medicalPercentage
        medicalPercentage = MyMedicalTextInput()
        self.add_widget(medicalPercentage)
        self.add_widget(Label(text="Add utilities\nAmount (0.00)"))
        global utilitiesPercentage
        utilitiesPercentage = MyUtilitiesTextInput()
        self.add_widget(utilitiesPercentage)
        self.add_widget(Label(text="Add charity\nAmount (0.00)"))
        global charityPercentage
        charityPercentage = MyCharityTextInput()
        self.add_widget(charityPercentage)
        self.add_widget(Label(text="Add food\nAmount (0.00)"))
        global foodPercentage
        foodPercentage = MyFoodTextInput()
        self.add_widget(foodPercentage)
        self.add_widget(Label(text="Add transportation\nAmount (0.00)"))
        global transportationPercentage
        transportationPercentage = MyTransportationTextInput()
        self.add_widget(transportationPercentage)
        self.add_widget(Label(text="Add other\nAmount (0.00)"))
        global otherPercentage
        otherPercentage = MyOtherTextInput()
        self.add_widget(otherPercentage)

#Draws the graph when the budget has been changed
class BudgetHelperButton(Button):
    def on_press(self,**kwargs):
        myBudgetGraph.drawGraph()

#Wraps the budget graph in order to access it from
#other parts of the program
class MyBudgetGraphWrapper(BoxLayout):
    def __init__(self,**kwargs):
        super(MyBudgetGraphWrapper,self).__init__(**kwargs)
        global myBudgetGraph
        myBudgetGraph = MyBudgetGraph()
        self.add_widget(myBudgetGraph)

#Holds the budget graph       
class MyBudgetGraph(Widget):
    def __init__(self,**kwargs):
        super(MyBudgetGraph,self).__init__(**kwargs)
        self.color = [(1.,0,.5),(1.,0,1.),(.5,0,1.),(0,0,1.),(0,.5,1.),
                (0,1.,1.),(0,1.,.7),(0,.9,0),(.6,1.,0),(1.,1.,0),
                (1.,.5,0),(1.,0,0),(.5,.5,.5)]
        self.windowSize = myGraphInfo.getWindowSize()
        self.windowSize = self.windowSize[1]
    
    #Draws the graph and all of the bubble labels    
    def drawGraph(self):
        getAllPercentages.setGoalsPercentages()
        getAllPercentages.setCategoryPercentages()
        self.clear_widgets()
        labelLayout = FloatLayout()
        self.canvas.clear()
        windowSize = self.windowSize
        percentages = getAllPercentages.getPercentages()
        with self.canvas:
            totalPercentage = 0
            for key in percentages: totalPercentage += float(percentages[key])
            if totalPercentage >= 1:
                self.overBudget(totalPercentage)
                return
            currentAngle, num = 0, 0
            color = self.color
            Color(.2,.2,.2)
            Ellipse(size=(windowSize/2,windowSize/2),pos=(
                windowSize/4-.15*windowSize,windowSize/4))
            for key in percentages:
                if percentages[key] == 0: continue
                currentColor = color[num]
                Color(*currentColor)
                currentPercentage = 360*float(percentages[key])
                Ellipse(size=(windowSize/2,windowSize/2)
                        ,pos=(windowSize/4-.15*windowSize,windowSize/4),
                        angle_start=currentAngle,
                        angle_end=(currentAngle+currentPercentage))
                halfwayAngle = currentAngle+currentPercentage/2
                bubble = self.makeBubble(halfwayAngle,key,currentColor)
                labelLayout.add_widget(bubble)
                currentAngle = (currentAngle+currentPercentage)
                num += 1
            self.add_widget(labelLayout)
            myRevenueStateLabel.dispatch('on_update')
    
    #Event handler for the bubbles on the graph, makes a popup appear that
    #states the amount and percent of that category
    def on_amount(self,bubble,key, currentColor,bubblebutton):
        myParent = bubble.parent
        myParent.remove_widget(bubble)
        percentages = getAllPercentages.getPercentages()
        amount = percentages[key]
        revenue = monthlyRevenue.getRevenue()
        myColor = (currentColor[0],currentColor[1],currentColor[2],1)
        info = (key +
            (" has been alloted\n" +
            "$%0.2f or " %(float(amount*revenue))+"%"+
            ("%0.2f of budget.")%float(amount*100))
            + "\nTouch  here to continue.")
        infoButton = Button(text=info,color = myColor,background_color=myColor,
            background_normal='C:/Users/Public/Documents/vintage-black-pattern.jpg')
        popup = Popup(title=(key + " Information"),
                      content=infoButton,size_hint=(.7,.4))
        infoButton.bind(on_press=popup.dismiss)
        popup.open()
        myParent.add_widget(bubble)
    
    #Makes a popup occur if the percentage alloted is
    #greater than 1, thus the graph can't be drawn and
    #the user is notified
    def overBudget(self,totalPercentage):
        windowSize = myGraphInfo.getWindowSize()
        windowSize = windowSize[1]
        myRevenueStateLabel.dispatch('on_update')
        budgetContent = Button(text=("""You have overbudgeted by
            $%0.2f
            \nPlease decrease your budget\nor increase revenue.
            \nClick here to continue.""")%(
        float(totalPercentage-1)*monthlyRevenue.getRevenue()),font_size=10,
        background_color=(0,1,1,1))
        popup = Popup(title="Overbudget Notice",
            content= budgetContent,size_hint=(.5,.3))
        budgetContent.bind(on_press=popup.dismiss)
        budgetContent.bind(on_press=self.parent.parent.remove_widget(popup))
        Color(.2,.2,.2)
        Ellipse(size=(windowSize/2,windowSize/2),
                pos=(windowSize/4-.15*windowSize,windowSize/4))
        popup.open()
    
    #Helper function to make a bubble label   
    def makeBubble(self,halfwayAngle,key,currentColor):
        windowSize = self.windowSize
        x = windowSize/2-.3*windowSize
        y = windowSize/2
        #Calculate the position from center that the bubbles are
        deltax = (windowSize/4-25)*math.cos(2*3.1415
                    -(halfwayAngle*(3.1415)/180 - (3.1415)/2))
        deltay = (windowSize/4-25)*math.sin(2*3.1415
                    -(halfwayAngle*(3.1415)/180 - (3.1415)/2))
        bubble = Bubble(pos=(x+deltax+50,y+deltay),size=(100,50))
        if len(key) >= 15:
            button = BubbleButton(text=(key[:(len(key)/2)] + "\n" +
                        key[(len(key)/2):]), color=(currentColor[0],
                        currentColor[1], currentColor[2],1))
            button.bind(on_release=partial(self.on_amount,bubble,
                                                key,currentColor))
            bubble.add_widget(button)
        else:
            button = BubbleButton(text=(key), color=(currentColor[0],
                                    currentColor[1],currentColor[2],1))
            button.bind(on_release=partial(self.on_amount,
                                            bubble,key,currentColor))
            bubble.add_widget(button)
        return bubble
        
#Displays your current status on the main screen            
class MyStatusLabel(Label):
    def __init__(self, **kwargs):
        super(MyStatusLabel,self).__init__(**kwargs)
        self.markup = True
        timeTuple = time.localtime()
        self.categoryCounts = dict({"Work":0,"Entertainment":0,"Medical":0,
                               "Food":0,"Transportation":0,"Utilities":0,
                               "Charity":0,"Other":0})
        daysOfWeek = ["Monday", "Tuesday", "Wedensday",
                      "Thursday","Friday","Saturday","Sunday"]
        months = ["January","February","March","April","May","June","July",
                  "August","September","October","November","December"]
        self.text = ("[size=22][color=ffffff][b]"
                     + str(daysOfWeek[timeTuple[6]]) + " "
                     + str(months[timeTuple[1]-1]) + " " +
                     str(timeTuple[2]) + ", " + str(timeTuple[0])
                     + "[/color][/b][/size]"+ "\n" + self.getStatus())
        self.text_size=(410,None)
        self.font_size = 14
        self.bind(on_ref_press=self.on_question)
    
    #Gets the current user status information    
    def getStatus(self):
        try:
            revenue = float(monthlyRevenue.getRevenue())
            x = 1/revenue
        except: return ("[color=ff6699]Current Status:" +
                        "[/color][color=99ccff]N/A[/color]")
        withinBudget = "[color=33ff99]Within Budget[/color]"
        theList = revenuesAndExpedenturesList.getList()
        currentTime = time.localtime()
        totalSpent = 0
        categoryCounts = self.categoryCounts
        for index in xrange(len(theList)):
            element = theList[index]
            (year,month) = element.getMonthAndYear()
            if (currentTime[1] == month) and (currentTime[0] == year):
                amount = element.getAmount()
                totalSpent += amount
                category = element.getCategory()
                for key in categoryCounts:
                    if category == key: categoryCounts[key] += amount
        if totalSpent > revenue:
            withinBudget = "[color=ff3333]Over Budget[/color]"
        badCategories, savings = [], []
        percentages = getAllPercentages.getPercentages()
        for key in percentages:
            if key not in categoryCounts: savings.append(key)
            total = percentages[key]*revenue
            if key in categoryCounts:
                if categoryCounts[key] > total:
                    badCategories.append(key)
        return self.getStatus2(badCategories,savings,withinBudget,)
    
    #Takes the above info and converts it into a label
    def getStatus2(self,badCategories,savings,withinBudget):   
        reccomendations = ""
        if len(badCategories) == 0:
            reccomendations = "[color=33ff99]Keep up the good work![/color]"
        else:
            if withinBudget == "[color=33ff99]Within Budget[/color]":
                reccomendations += "[color=99ccff]Modify budget\n[/color]"
            reccomendations += "[color=ff3333]Stop spending from categories:\n"
            for index in xrange(len(badCategories)-1):
                reccomendations += (badCategories[index] + ",  ")
            reccomendations += badCategories[len(badCategories)-1]
            reccomendations += "[/color]"
        if len(savings) == 0: savedCategories = "[color=99ccff]Nothing[/color]"
        else:
            savedCategories = "[color=33ff99]"
            for index in xrange(len(savings)-1):
                savedCategories += (savings[index] + ",  ")
            savedCategories += savings[len(savings)-1]
            savedCategories +="[/color]"
        return ("[color=ff6699][b]Current Status: [/b][/color]" + withinBudget
            + "[color=ff6699][b]\nRecommendations: [/b][/color][color=99ccff]"+
            "[ref=q](whats this?)\n[/ref][/color]" + reccomendations +
            "[color=ff6699][b]\nCurrently Saving For: \n[/b][/color]"
            + savedCategories)
    
    #Event handler that displays reccomendation info when
    #'whats this?' is pressed
    def on_question(instance,value,self):
        info = """[color=ff3399]
        What do the recccomendations mean?
        1) Keep up the good work! -
        Means that you are within the overall
        budget, and also within budget for
        each category.
        You are doing great!
        2) Modify Budget - Means that you are
        within the overall budget, but are
        over budget in one or more categories.
        It is reccomended that you modify your
        budget to accomadate the extra spending.
        3) Stop spending from categories: ... -
        Means that you are over budget in one
        or more categories. It is reccomended
        you reduce your spending in those
        categories.
        
        Touch here to continue....[/color]"""
        statusContent = Button(text=info,
            background_normal=
                'C:/Users/Public/Documents/vintage-black-pattern.jpg',
            background_color=(1,1,1,.5),markup=True)
        popup = Popup(title="Reccommendations Info",
                      content=statusContent,size_hint=(.8,.8))
        statusContent.bind(on_press=popup.dismiss)
        popup.open()

#Changes the current view of the ledger
class ChangeViewButton(Button):
    def on_press(self, **kwargs):
        if self.text == "View Revenue":
            status.changeStatus(True, False)
        elif self.text == "View Expenditures":
            status.changeStatus(False, True)
        else:
            status.changeStatus(True, True)
        scroller.dispatch('on_submit')

#The following classes all pertain to the input
#revenue screen, each wrapper was individually done seperate
#because each has its own special event
###################################################################

class MyTypeSpinnerWrapper(BoxLayout):
    def __init__(self,**kwargs):
        super(MyTypeSpinnerWrapper, self).__init__(**kwargs)
        global typeSpinner
        typeSpinner = MyTypeSpinner()
        self.add_widget(typeSpinner)
        
class MyCurrencySpinnerWrapper(BoxLayout):
    def __init__(self,**kwargs):
        super(MyCurrencySpinnerWrapper, self).__init__(**kwargs)
        global currencySpinner
        currencySpinner = MyCurrencySpinner()
        self.add_widget(currencySpinner)
        
class MyCategorySpinnerWrapper(BoxLayout):
    def __init__(self,**kwargs):
        super(MyCategorySpinnerWrapper, self).__init__(**kwargs)
        global categorySpinner
        categorySpinner = MyCategorySpinner()
        self.add_widget(categorySpinner)

class MyAmountTextInputWrapper(BoxLayout):
    def __init__(self,**kwargs):
        super(MyAmountTextInputWrapper, self).__init__(**kwargs)
        global amountTextInput
        amountTextInput = MyAmountTextInput()
        self.add_widget(amountTextInput)
        
class MyDateTextInputWrapper(BoxLayout):
    def __init__(self,**kwargs):
        super(MyDateTextInputWrapper, self).__init__(**kwargs)
        global dateTextInput
        dateTextInput = MyDateTextInput()
        self.add_widget(dateTextInput)        

class MyDescriptionTextInputWrapper(BoxLayout):
    def __init__(self,**kwargs):
        super(MyDescriptionTextInputWrapper, self).__init__(**kwargs)
        global descriptionTextInput
        descriptionTextInput = MyDescriptionTextInput()
        self.add_widget(descriptionTextInput)

####################################################################

#Wraps the scroller for data access inside the revenue
#input screen
class MyScrollBox(BoxLayout):
    def __init__(self,**kwargs):
        super(MyScrollBox, self).__init__(**kwargs)
        global scroller
        scroller = MyScrollScreen()
        self.add_widget(scroller)

#Gets the scroll view as seen in the input revenue screen
#adjusts when new inputs and expenses are made
class MyScrollScreen(ScrollView):
    def __init__(self,**kwargs):
        self.scroll_friction = 2
        super(MyScrollScreen, self).__init__(**kwargs)
        layout = self.getLayout()
        self.add_widget(layout)
        self.register_event_type('on_submit')
    
    def on_submit(self):
        self.clear_widgets()
        layout = self.getLayout()
        self.add_widget(layout)
        return True
    
    def getLayout(self):
        layout = GridLayout(orientation= 'vertical',cols=1,
                            row_default_height=120,size_hint_y=None)        
        layout.bind(minimum_height=layout.setter('height'))
        modListLength = revenuesAndExpedenturesList.getLength()
        for i in xrange(modListLength):
            color = (5,0,0,2)
            label = revenuesAndExpedenturesList.getIndex(i)
            if label.type == 'Revenue':
                color = (0,5,0,2)
            elif (label.type == 'Select') or (label.type == None):
                continue 
            if ((status.getStatus('Expense') == False)
                and (label.type == 'Expense')):
                continue
            elif  ((status.getStatus('Revenue') == False)
                and (label.type == 'Revenue')):
                continue
            myInfo = label.getLabel()
            myInfo.color = color
            layout.add_widget(myInfo)
        return layout

#Superclass created to be inherited from for each of
#the spinners in the input revenue screen
class MySpinner(Spinner):
    def __init__(self,**kwargs):
        super(MySpinner, self).__init__(**kwargs)
        self.text = 'Select'
        self.register_event_type('on_submit')
        self.bind(text = self.show_selected_value)
        self.background_color = (0,1,1,1)
  
    def on_submit(self):
        self.text = 'Select'
        return True
    
    #Meant to be overridden
    def show_selected_value(self, blah, text):
        pass

#The following are mySpinner subclasses used in the input revenue
#screen to collect data from the user. All are similar but
#submit different values
##################################################################

class MyCategorySpinner(MySpinner):
    def __init__(self,**kwargs):
        super(MyCategorySpinner,self).__init__(**kwargs)
        self.values = ('Work','Entertainment','Food','Medical','Charity',
                       'Transportation','Utilities','Other')
    
    def show_selected_value(self, blah, text):
        submitInfo.addCategory(text)

class MyTypeSpinner(MySpinner):
    def __init__(self,**kwargs):
        super(MyTypeSpinner,self).__init__(**kwargs)
        self.values = ('Revenue','Expense')
    
    def show_selected_value(self, blah, text):
        submitInfo.addType(text)

class MyCurrencySpinner(MySpinner):
    def __init__(self,**kwargs):
        super(MyCurrencySpinner,self).__init__(**kwargs)
        self.values = ('Cash','Credit','Bank Account','DinEx','Giftcard')  
    
    def show_selected_value(self, blah, text):
        submitInfo.addCurrency(text)

######################################################################

#The following is a superclass used throughout my program
#to be used as a blueprint for a usable textbox
class MyTextInput(TextInput):
    def __init__(self,**kwargs):
        super(MyTextInput, self).__init__(**kwargs)
        self.multiline = False
        self.text = ''
        self.bind(on_text_validate=partial(self.on_text,self))
        self.register_event_type('on_submit')
    
    def on_submit(self):
        self.text = ''
        return True
    
    def on_text(self,instance,value, **kwargs):
        pass

#The following are subclasses of myTextInput that
#are used to collect information on the input
#revenue screen and budget screen.
#They are all similar but submit
#different data.
##############################################################

class MyDateTextInput(MyTextInput):
    def on_text(self,instance,value, **kwargs):
        text = self.text
        submitInfo.addDate(text)
 
class MyAmountTextInput(MyTextInput):
    def on_text(self,instance,value, **kwargs):
        text = self.text
        submitInfo.addAmount(text)

class MyDescriptionTextInput(MyTextInput):
    def on_text(self,instance,value, **kwargs):
        text = self.text
        submitInfo.addDescription(text)
   
class MyWorkTextInput(MyTextInput):
    def on_text(self,instance,value,**kwargs):
        myBudgetInfo.enterWork(self.text)
        
class MyEntertainmentTextInput(MyTextInput):
    def on_text(self,instance,value,**kwargs):
        myBudgetInfo.enterEntertainment(self.text) 
 
class MyMedicalTextInput(MyTextInput):
    def on_text(self,instance,value,**kwargs):
        myBudgetInfo.enterMedical(self.text) 
 
class MyUtilitiesTextInput(MyTextInput):
    def on_text(self,instance,value,**kwargs):
        myBudgetInfo.enterUtilities(self.text)    

class MyCharityTextInput(MyTextInput):
    def on_text(self,instance,value,**kwargs):
        myBudgetInfo.enterCharity(self.text)
        
class MyFoodTextInput(MyTextInput):
    def on_text(self,instance,value,**kwargs):
        myBudgetInfo.enterFood(self.text)
        
class MyTransportationTextInput(MyTextInput):
    def on_text(self,instance,value,**kwargs):
        myBudgetInfo.enterTransportation(self.text)

class MyOtherTextInput(MyTextInput):
    def on_text(self,instance,value,**kwargs):
        myBudgetInfo.enterOther(self.text)  

#################################################################

#Button on budget screen that saves all the data that was just input
#to the screen and then clears it
class MySaveButton(Button):
    def on_press(self,**kwargs):
        savedBudgetInfo.update(myBudgetInfo.getWork(),
                               myBudgetInfo.getEntertainment(),
                               myBudgetInfo.getCharity(),
                               myBudgetInfo.getMedical(),
                               myBudgetInfo.getUtilities(),
                               myBudgetInfo.getOther(),
                               myBudgetInfo.getFood(),
                               myBudgetInfo.getTransportation())
        getAllPercentages.setCategoryPercentages()
        #redraw the graph
        myBudgetGraph.drawGraph()
        statusAndProgress.dispatch('on_update')
        myStatusDetailLayout.dispatch('on_update')

#Button on goals screen that saves the data,
#and intentionally does not delete it so the user
#can easily alter it
class MySaveGoalsButton(Button):
    def on_press(self,**kwargs):
        savedGoalsInfo.setInfo(myGoalsInfo.getGoalsInfo())
        getAllPercentages.setGoalsPercentages()
        #redraw the graph
        myBudgetGraph.drawGraph()
        statusAndProgress.dispatch('on_update')
        myStatusDetailLayout.dispatch('on_update')

#Holds the layout for the goals screen        
class MyGoalsLayout(GridLayout):
    def __init__(self,**kwargs):
        super(MyGoalsLayout,self).__init__(**kwargs)
        labelLayout = BoxLayout(orientation='vertical', size_hint = (.3,1))
        for index in xrange(5):
            labelLayout.add_widget(Label(text = (
                "Enter\nGoal " + str(index+1) + "\nInfo")))
        self.add_widget(labelLayout)
        infoLayout = GridLayout(cols = 1)
        infoLayout.add_widget(MyGoalsInput(0))
        infoLayout.add_widget(MyGoalsInput(1))
        infoLayout.add_widget(MyGoalsInput(2))
        infoLayout.add_widget(MyGoalsInput(3))
        infoLayout.add_widget(MyGoalsInput(4))
        self.add_widget(infoLayout)

#Holds the input section for each goal      
class MyGoalsInput(GridLayout):
    def __init__(self,number,**kwargs):
        super(MyGoalsInput,self).__init__(**kwargs)
        self.cols = 3
        self.add_widget(MyGoalsNameTextInput(number))
        self.add_widget(MyGoalsAmountTextInput(number))
        self.add_widget(MyGoalsDateTextInput(number))

#The following three functions are used to store text
#input on the goals screen
##########################################################

class MyGoalsNameTextInput(MyTextInput):
    def __init__(self,number,**kwargs):
        super(MyGoalsNameTextInput,self).__init__(**kwargs)
        self.number = number
        names = savedGoalsInfo.getGoalNames()
        self.text = str(names[number])
    
    def on_text(self, instance, value, **kwargs):
        myGoalsInfo.addName(self.number,self.text)
        
class MyGoalsAmountTextInput(MyTextInput):
    def __init__(self,number,**kwargs):
        super(MyGoalsAmountTextInput,self).__init__(**kwargs)
        self.number = number
        amounts = savedGoalsInfo.getGoalAmounts()
        self.text = str(amounts[number])
        
    def on_text(self, instance,value,**kwargs):
        myGoalsInfo.addAmount(self.number,self.text)
        
class MyGoalsDateTextInput(MyTextInput):
    def __init__(self,number,**kwargs):
        super(MyGoalsDateTextInput,self).__init__(**kwargs)
        self.number = number
        dates = savedGoalsInfo.getGoalDates()
        self.text = str(dates[number])
        
    def on_text(self, instance,value,**kwargs):
        myGoalsInfo.addDate(self.number,self.text)

#################################################################       

#Manages the screen switching      
class MyScreenManager(ScreenManager):
    def __init__(self,**kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        
#Button that quits the program and saves the data if pressed
#(otherwise no data will be saved)
class QuitButton(Button):
    def __init__(self,**kwargs):
        super(QuitButton, self).__init__(**kwargs)
        self.text = 'Save and Quit'
    
    def on_press(self,**kwargs):
        currentData.storeInfo(myGraphInfo,getAllPercentages,monthlyRevenue,
                savedGoalsInfo,savedBudgetInfo,revenuesAndExpedenturesList)
        Writer.writeToFile()
        exit()
        
#Submits the data in the "add new revenue screen"
class MySubmitButton(Button):
    def __init__(self,**kwargs):
        super(MySubmitButton, self).__init__(**kwargs)
        self.size_hint = (1,.15)
        self.text = 'Submit'
    
    #Inputs the data to a stored list, oraganizes that data,
    #and clears the input revenue screen again
    def on_press(self, **kwargs):
        infoObject = RevenuesAndExpedentures(submitInfo.getType(),
            submitInfo.getCategory(),submitInfo.getCurrency(),
            submitInfo.getAmount(), submitInfo.getDescription(),
            submitInfo.getDate())
        revenuesAndExpedenturesList.addItem(infoObject)
        revenuesAndExpedenturesList.organize()
        status.changeStatus(True,True)
        self.dispatchAll()
        self.submitAll()
    
    #Sends the data out to the list
    def submitAll(self):
        submitInfo.addDate(None)
        submitInfo.addAmount(None)
        submitInfo.addDescription(None)
        submitInfo.addCategory(None)
        submitInfo.addCurrency(None)
        submitInfo.addType(None)
    
    #Clears the screen and updates the rest of the
    #program to accomadate the new data
    def dispatchAll(self):
        scroller.dispatch('on_submit')
        amountTextInput.dispatch('on_submit')
        dateTextInput.dispatch('on_submit')
        descriptionTextInput.dispatch('on_submit')
        typeSpinner.dispatch('on_submit')
        categorySpinner.dispatch('on_submit')
        currencySpinner.dispatch('on_submit')
        statusAndProgress.dispatch('on_update')
        myStatusDetailLayout.dispatch('on_update')
        monthlyGraph.dispatch('on_draw')
        yearlyGraph.dispatch('on_draw')
        
#Button on the add revenue screen that deletes what was
#currently input, and returns the scroll screen to the
#original configuration. Meant to simulate how a
#real app would be configured
class MyRevenueBackButton(Button):
    def on_press(self, **kwargs):
        submitInfo.addDate(None)
        submitInfo.addAmount(None)
        submitInfo.addDescription(None)
        status.changeStatus(True,True)
        scroller.dispatch('on_submit')

#This class is meant to store input revenue information
#temporarily while the user types
class SubmitInfo(object):
    def __init__(self):
        self.description = None
        self.date = None
        self.type = None
        self.category = None
        self.currency = None
        self.amount = None
        pass
    
    def addDescription(self,desc):
        self.description = desc
        
    def getDescription(self):
        return self.description
        
    def addDate(self,date):
        self.date = date
    
    def getDate(self):
        return self.date
      
    def addType(self,myType):
        self.type = myType
        
    def getType(self):
        return self.type
    
    def addCategory(self, category):
        self.category = category
    
    def getCategory(self):
        return self.category
        
    def addCurrency(self,currency):
        self.currency = currency
    
    def getCurrency(self):
        return self.currency
       
    def addAmount(self,amount):
        self.amount = amount
        
    def getAmount(self):
        return self.amount

#The following class encapsulates all the information
#needed about each ledger item, and ouputs it
#in various useful ways
class RevenuesAndExpedentures(object):
    def __init__(self,myType,category,currency,amount,description, date):
        self.date = date
        self.dateNumeric = 0
        self.dateYear = 0
        self.dateMonth = 0
        self.dateDay = 0
        try:
            date = date.split("/")
            if len(date) == 3: #Has three components, month, date, and year
                (date[0], date[1], date[2]) = (date[2],date[0],date[1])
                self.dateYear = int(date[0])
                self.dateMonth = int(date[1])
                self.dateDay = int(date[2])
                if len(date[1]) == 1:
                    date[1] = "0" + date[1]
                if len(date[2]) == 1:
                    date[2] = "0" + date[2]
                date = "".join(date)
                self.dateNumeric = int(date)
        except: pass
        self.description = description
        try: self.amount = float(amount)
        except: self.amount = 0.00
        if self.amount < 0: self.amount = 0.00
        self.currency = currency
        self.category = category
        self.type = myType
    
    def getMonthAndYear(self):
        return (self.dateYear, self.dateMonth)
    
    def getDay(self):
        return self.dateDay
    
    def getDateNumeric(self):
        return self.dateNumeric
    
    def getType(self):
        return self.type
    
    def getAmount(self):
        return self.amount
    
    def getCategory(self):
        return self.category
       
    def getLabel(self):
        label = Label()
        label.markup = True
        windowSize = myGraphInfo.getWindowSize()
        label.text_size=(400,None)
        labelText = (("""
        [b]Type:[/b] %s  [b]Date:[/b] %s
        [b]Amount:[/b] $%0.2f  [b]Currency Type:[/b] %s
        [b]Category:[/b] %s
        [b]Description:[/b] %s
        [b][ref=remove](Remove)[/b][/ref]
        """) % (self.type, self.date, self.amount,
                 self.currency, self.category, self.description))
        label.text = labelText
        label.size_hint_y = None
        def on_remove(instance,value):
            revenuesAndExpedenturesList.removeItem(self)
            scroller.dispatch('on_submit')
        label.bind(on_ref_press=on_remove)
        return label
    
    def __str__(self):
        if (self.date != None and self.description != None and
            self. amount != None and self.currency != None and
            self.category != None and self.type != None):
            return ("Object: " + self.date + " " + self.description + " "
                    + str(self. amount) + " " + self.currency + " " +
                    self.category + " " + self.type)
        else:
            return "Element is empty"

#The following is the list of the obove objects
#for semi-permanent storage
class RevenuesAndExpedenturesList(object):
    def __init__(self):
        self.theList = list()
        
    def addItem(self,item):
        self.theList.append(item)
        
    def getList(self):
        return self.theList
    
    def removeItem(self,item):
        if item in self.theList:
            self.theList.remove(item)
            
    def getLength(self):
        return len(self.theList)
    
    def getIndex(self,index):
        return self.theList[index]
    
    def numericCompare(self, element1, element2):
        return element2.getDateNumeric() - element1.getDateNumeric()
    
    def organize(self):
        self.theList.sort(cmp=self.numericCompare)
    
    def __str__(self):
        try:
            return (str(self.theList[0]) + "  " + str(self.theList[1])
                    + " ....")
        except:
            return "0 or 1 elements in this list"

#The following  is meant to store input budget information
#temporarily while the user types
class MyBudgetInfo(object):
    def __init__(self):
        self.work = 0
        self.entertainment = 0
        self.food = 0
        self.medical = 0
        self.charity = 0
        self.utilities = 0
        self.transportation = 0
        self.other = 0
        
    def enterWork(self,percentage):
        self.work = percentage
    
    def getWork(self):
        return self.work
        
    def enterEntertainment(self,percentage):
        self.entertainment = percentage
    
    def getEntertainment(self):
        return self.entertainment
        
    def enterFood(self,percentage):
        self.food = percentage
    
    def getFood(self):
        return self.food
        
    def enterMedical(self, percentage):
        self.medical = percentage
    
    def getMedical(self):
        return self.medical
        
    def enterOther(self,percentage):
        self.other = percentage
    
    def getOther(self):
        return self.other
        
    def enterCharity(self,percentage):
        self.charity = percentage
    
    def getCharity(self):
        return self.charity
        
    def enterTransportation(self,percentage):
        self.transportation = percentage
    
    def getTransportation(self):
        return self.transportation
        
    def enterUtilities(self,percentage):
        self.utilities = percentage
        
    def getUtilities(self):
        return self.utilities

#The following is the semi-permanent storage of
#the above information, used for access
class SavedBudgetInfo(object):
    def __init__(self):
        self.work = 0
        self.entertainmnet = 0
        self.charity = 0
        self.other = 0
        self.utilities = 0
        self.transportation = 0
        self.food = 0
        self.medical = 0
        
    def update(self,work,entertainment,charity,medical,
               utilities,other,food,transportation):
        self.work = work
        self.entertainment = entertainment
        self.charity = charity
        self.medical = medical
        self.utilities = utilities
        self.other = other
        self.food = food
        self.transportation = transportation
        
    def getBudget(self):
        try: work = float(self.work)
        except: work = 0
        try: entertainment = float(self.entertainment)
        except: entertainment = 0
        try: charity = float(self.charity)
        except: charity = 0
        try: medical = float(self.medical)
        except: medical = 0
        try: utilities = float(self.utilities)
        except: utilities = 0
        try: other = float(self.other)
        except: other = 0
        try: food = float(self.food)
        except: food = 0
        try: transportation = float(self.transportation)
        except: transportation = 0
        return [work,entertainment,charity,medical,utilities,
                other,food,transportation]

#The following simply stores whether the user wants
#to view only revenue or only expenses on the budget screen
class ExpenseAndRevenueStatus(object):
    def __init__(self):
        self.expense = True
        self.revenue = True
        
    def changeStatus(self, rev_status, exp_status):
        self.revenue = rev_status
        self.expense = exp_status
        
    def getStatus(self,rev_or_exp):
        if rev_or_exp == 'Revenue':
            return self.revenue
        elif rev_or_exp == 'Expense':
            return self.expense

#Stores the information about each current goal
class SavedGoalsInfo(object):
    #Format information for display
    def __init__(self):
        self.goalNames = ['Name','Name','Name','Name','Name']
        self.goalAmounts = ['Amount (0.00)','Amount (0.00)',
                            'Amount (0.00)','Amount (0.00)','Amount (0.00)']
        self.goalDates = ['Date(MM/DD/YYYY)','Date(MM/DD/YYYY)',
            'Date(MM/DD/YYYY)','Date(MM/DD/YYYY)','Date(MM/DD/YYYY)']
    
    #Sets the current goal info        
    def setInfo(self, goals):
        currentTime = time.localtime()
        self.goalNames = ['','','','','']
        self.goalAmounts = ['','','','','']
        self.goalDates = ['','','','','']
        for index in xrange(0,5):
            (self.goalNames[index], self.goalAmounts[index],
             self.goalDates[index]) = goals[index]
    
    def getGoalNames(self):
        return self.goalNames
    
    def getGoalAmounts(self):
        return self.goalAmounts
    
    def getGoalDates(self):
        return self.goalDates
               
    def getNameDate(self, number):
        return str(self.goalNames[number]) + " " + str(self.goalDates[number])
    
    def getDateNumerics(self,number):
        date = self.goalDates[number]
        try:
            date = date.split("/")
            if len(date) == 3: #Has three components, month, date, and year
                (date[0], date[1], date[2]) = (
                    int(date[2]),int(date[0]),int(date[1]))
        except:
            date = 0
        return date
    
    def getAmount(self, number):
        amount = self.goalAmounts[number]
        try:
            amount = float(amount)
        except:
            amount = 0
        return amount
    
    def __str__(self):
        return (str(self.goalNames) + str(self.goalDates)
                + str(self.goalAmounts))

#The following takes information from all the different
#sources and gets the percentages of each goal or budget item
#to be displayed on the graph. Will return a dictionary of
#all these items
class GetAllPercentages(object):
    def __init__(self):
        self.percentages = dict()
    
    #Sets the category percentages when they are entered   
    def setCategoryPercentages(self):
        try:
            revenue = float(monthlyRevenue.getRevenue())
        except:
            return
        if revenue == 0:
            self.clearPercentages()
            return
        budget = savedBudgetInfo.getBudget()
        for index in xrange(len(budget)):
            if budget[index] < 0: budget[index] = 0
        self.percentages["Work"] = budget[0]/revenue
        self.percentages["Entertainment"] = budget[1]/revenue
        self.percentages["Charity"] = budget[2]/revenue
        self.percentages["Medical"] = budget[3]/revenue
        self.percentages["Utilities"] = budget[4]/revenue
        self.percentages["Other"] = budget[5]/revenue
        self.percentages["Food"] = budget[6]/revenue
        self.percentages["Transportation"] = budget[7]/revenue
    
    #Defines the goals percentages when they are entered 
    def setGoalsPercentages(self):
        self.percentages = dict()
        self.setCategoryPercentages()
        try: initialRevenue = float(monthlyRevenue.getRevenue())
        except: return
        if initialRevenue == 0:
            self.clearPercentages()
            return
        timeTuple = time.localtime()
        for index in xrange(0,5):
            if (savedGoalsInfo.getAmount(index) != 0):
                revenue = initialRevenue
                goalTime = savedGoalsInfo.getDateNumerics(index)
                if (type(goalTime[0]) != int or type(goalTime[1]) != int or
                    type(goalTime[2]) != int): continue
                timeDifference = 1
                timeYear = timeTuple[0]
                timeMonth = timeTuple[1]
                if timeYear < goalTime[0] - 1:
                    while timeYear <= goalTime[0]:
                        if timeMonth == 11:
                            timeMonth = 1
                            timeYear += 1
                        timeMonth += 1
                        timeDifference += 1
                    timeDifference += goalTime[1]
                elif timeYear < goalTime[0]:
                    timeDifference = 12 - timeMonth
                    timeDifference += goalTime[1] + 1
                elif timeYear == goalTime[0]:
                    timeDifference = goalTime[1]-timeMonth + 1
                revenue = revenue*timeDifference
                info = savedGoalsInfo.getNameDate(index)
                amount = savedGoalsInfo.getAmount(index)
                if amount < 0: continue
                self.percentages[info] = amount/revenue
    
    def clearPercentages(self):
        d = self.percentages
        for key in d:
            d[key] = 0
    
    #Returns the entire percentage list                             
    def getPercentages(self):
        return self.percentages

#Stores information about the current monthly revenue
#and allows for new calculations
class MonthlyRevenue(object):
    def __init__(self):
        self.setRevenue = 1000.00
        self.calcRevenue = 0
        self.toggle = 'Set'
        self.tempRevenue = 0
    
    def fixRevenue(self,revenue):
        try:
            self.setRevenue = float(revenue)
        except:
            pass
        
    def fixTempRevenue(self,revenue):
        self.tempRevenue = revenue
        
    def getTempRevenue(self):
        return self.tempRevenue
    
    def getSetRevenue(self):
        return self.setRevenue
        
    def getRevenue(self):
        self.calculateNewRevenue()
        if self.toggle == 'Set':
            return self.setRevenue
        elif self.toggle == 'Calc':
            return self.calcRevenue
    
    def getToggle(self):
        return self.toggle
    
    def toggleRevenue(self,setOrCalculatedRev):
        self.toggle = setOrCalculatedRev
    
    #Calculates new revenue based on last month's revenue    
    def calculateNewRevenue(self):
        theList = revenuesAndExpedenturesList.getList()
        totalAmount = 0
        for index in xrange(len(theList)):
            element = theList[index]
            (year,month) = element.getMonthAndYear()
            currentTime = time.localtime()
            countYear = False
            if (currentTime[1] == 1) and (month == 12) and (
                currentTime[0] == year):
                countYear = True
            countMonth = int(currentTime[1]) - month
            if (element.getType() == "Revenue") and (
                countYear == True or countMonth == 1):
                amount = element.getAmount()
                totalAmount += amount
        self.calcRevenue = totalAmount

#Blueprint for the layout of the configure revenue screen                  
class MyConfigureRevenueLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyConfigureRevenueLayout, self).__init__(**kwargs)
        label = Label(
            text="[color=00ffff][b]Check if revenue is set[/b][/color]",
            markup=True,font_size=20)
        self.add_widget(label)
        global toggleCheckBox
        toggleCheckBox = ToggleCheckBox()
        self.add_widget(toggleCheckBox)
        self.cols = 1
        self.add_widget(Label(
            text="[color=00ffff][b]Enter Monthly Revenue:[/b][/color]",
            markup=True,font_size=20))
        self.add_widget(MyConfigureRevenueTextInput())

#Text box that dispatches the input
#of set revenue from the user
class MyConfigureRevenueTextInput(MyTextInput):
    def __init__(self,**kwargs):
        super(MyConfigureRevenueTextInput,self).__init__(**kwargs)
        self.text = str(monthlyRevenue.getSetRevenue())
        self.font_size = 18
    
    def on_text(self,instance, value,**kwargs):
        monthlyRevenue.fixTempRevenue(self.text)

#Toggles whether the revenue is set or calculated
#on the configure revenue screen
class ToggleCheckBox(CheckBox):
    def __init__(self,**kwargs):
        super(ToggleCheckBox, self).__init__(**kwargs)
        self.register_event_type('on_checkbox_active')
        self.register_event_type('on_update')
        self.bind(active=self.on_checkbox_active)
        
    def on_checkbox_active(self,checkbox, value):
        if value:
            monthlyRevenue.toggleRevenue("Set")
        else:
            monthlyRevenue.toggleRevenue("Calc")
    
    def on_update(self):
        if monthlyRevenue.getToggle() == "Set":
            self.active = True
        elif monthlyRevenue.getToggle() == "Calc":
            self.active = False

#Submits the current revenue configuration on the screen
class MyConfigureRevenueSubmitButton(Button):
    def on_press(self,**kwargs):
        monthlyRevenue.fixRevenue(monthlyRevenue.getTempRevenue())
        getAllPercentages.setGoalsPercentages()
        getAllPercentages.setCategoryPercentages()
        #redraw the graph
        myBudgetGraph.drawGraph()
        #adjust the progress on the main screen
        statusAndProgress.dispatch('on_update')
        myStatusDetailLayout.dispatch('on_update')

#Holds temporary data about the goals, in order for them
#to be submitted
class MyGoalsInfo(object):
    def __init__(self):
        self.goalNames = ['','','','','']
        self.goalDates = ['','','','','']
        self.goalAmounts = ['','','','','']
        
    def addName(self, number,name):
        self.goalNames[number] = name
    
    def addDate(self,number,date):
        self.goalDates[number] = date
    
    def addAmount(self,number,amount):
        self.goalAmounts[number] = amount
            
    def getGoalsInfo(self):
        goals = dict()
        #################### Name, amount, date ##################
        for index in xrange(0,5):
            goals[index] = (self.goalNames[index],self.goalAmounts[index],
                            self.goalDates[index])
        return goals

#Used for storage of the current window size,
#because the app will be altered depending on the size
#of the window.
class MyGraphInfo(object):
    def __init__(self):
        #default window size, will change if window is different
        self.windowSize = [600,600]
        
    def setWindowSize(self, size):
        self.windowSize = size
        
    def getWindowSize(self):
        return self.windowSize

#This class stores all of all the important data in the
#program. It is used for pickling, so that when my program
#closes all of the data is restored upon startup
class CurrentData(object):
    def __init__(self):
        self.graphInfo = MyGraphInfo()
        self.percentages = GetAllPercentages()
        self.revenue = MonthlyRevenue()
        self.savedGoals = SavedGoalsInfo()
        self.savedBudget = SavedBudgetInfo()
        self.rev_and_exp = RevenuesAndExpedenturesList()
        
    def storeInfo(self,a,b,c,d,e,f):
        self.graphInfo = a
        self.percentages = b
        self.revenue = c
        self.savedGoals = d
        self.savedBudget = e
        self.rev_and_exp = f
        
    def recoverInfo(self):
        infoList = [self.graphInfo,self.percentages,self.revenue,
                    self.savedGoals,self.savedBudget,self.rev_and_exp]
        return infoList

#Used for writing to the pickle data file        
class Writer(object):
    def __init__(self):
        pass
    
    @classmethod
    def writeToFile(self):
        try:
            f = open("C:/Users/Public/Documents/piggybankData.p","wb")
            pickle.dump(currentData,f)
        except:
            print "Cannot write to file..."

#Holds the amount of overflow spending from each category,
#used for status details
class OverflowAmounts(object):
    def __init__(self):
        self.amt = 0
        
    def addAmt(self, amt):
        self.amt += amt
        
    def getAmt(self):
        theList = revenuesAndExpedenturesList.getList()
        extra = 0
        for element in theList:
            if (element.getType() == 'Expense'
                and element.getCategory() == None):
                extra += element.getAmount()
        return self.amt + extra
    
    def clearAmt(self):
        self.amt = 0

##################################Main starter class#######################
class TestApp(App): 
    
    #KIVY PROGRAM BUILDER FILE --
    #DOES THESE ACTIONS BEFORE STARTING THE PROGRAM
    def build(self):
        #Settings
        self.icon = 'C:/Users/Public/Documents/piggy-bank.png'
        self.title = 'PiggyBank'
        Config.set('graphics','width','420')
        Config.set('graphics','height','600')
        sm = MyScreenManager(transition=SlideTransition())
        
        #Set up global information objects -- MUST be done
        #in the builder file only
        global overflowAmounts
        overflowAmounts = OverflowAmounts()
        global myGraphInfo
        global getAllPercentages
        global monthlyRevenue
        global myGoalsInfo
        global savedGoalsInfo
        global myBudgetInfo
        global savedBudgetInfo
        global status
        global submitInfo
        global revenuesAndExpedenturesList
        myGraphInfo = MyGraphInfo()
        getAllPercentages = GetAllPercentages()
        monthlyRevenue = MonthlyRevenue()
        myGoalsInfo = MyGoalsInfo()
        savedGoalsInfo = SavedGoalsInfo()
        myBudgetInfo = MyBudgetInfo()
        savedBudgetInfo = SavedBudgetInfo()
        status = ExpenseAndRevenueStatus()
        submitInfo = SubmitInfo()
        revenuesAndExpedenturesList = RevenuesAndExpedenturesList()
        
        self.setInstructions()
        global isNew #To tell if a pickle file was detected
        #Set up data persistence using a pickle file
        global currentData
        try:
            currentData = pickle.load(
                open("C:/Users/Public/Documents/piggybankData.p","rb"))
            print "loaded file succcessfully"
            objectsList = currentData.recoverInfo()
            myGraphInfo = objectsList[0]
            getAllPercentages = objectsList[1]
            monthlyRevenue = objectsList[2]
            savedGoalsInfo = objectsList[3]
            savedBudgetInfo = objectsList[4]
            revenuesAndExpedenturesList = objectsList[5]
            isNew = False
        except:
            currentData = CurrentData()
            isNew = True
        #Set up screens
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(BudgetScreen(name='budget'))
        sm.add_widget(DataScreen(name='data'))
        sm.add_widget(ConfigureBudgetScreen(name = 'configure budget'))
        sm.add_widget(ConfigureRevenueScreen(name = 'configure revenue'))
        sm.add_widget(ConfigureGoalsScreen(name = 'goals'))
        sm.add_widget(StatusScreen(name='status'))
        revenueScreen = RevenueScreen(name='revenue')
        sm.add_widget(revenueScreen)
        addNewRevenueScreen = AddNewRevenueScreen(name='new revenue')
        sm.add_widget(addNewRevenueScreen)
        return sm
    
    #Holds the instructions to be displayed upon startup
    def setInstructions(self):
        self.instructions = """
            [color=ff3399][b]Hi There![/b]
            Welcome to PiggyBank, the smart money
            management app for the dreamer in us all.
            [b]Instructions:[/b] To start, enter into the
            two features listed below:
            [b]-Ledger:[/b] This is where you will enter your
                daily revenues and expenses as they occur.
            [b]-Budget:[/b] This is where you will create
                your monthly budget. To start, enter the
                amounts you estimate you spend on each
                category each month under the "Configure
                Budget" screen. Then, you may determine
                how to determine your monthly revenue
                under "Configure Revenue": either
                calculated by last month's revenues or a
                set input. Finally, you may allot your
                remaining budget for any future goals you
                may have under "my goals", e.g. that
                vacation you always wanted. Dream on!
            [b]And thats it![/b] You are on your way to
            achieving your goals. See the main screen,
            status details screen, and history screen
            to monitor your progress. Have fun!
            
                Touch here to continue[/color]
            """
    
    #ACTIONS THAT OCCUR UPON STARTUP
    def on_start(self):
        myGraphInfo.setWindowSize(self.root.size)
        statusAndProgress.dispatch('on_update')
        myStatusDetailLayout.dispatch('on_update')
        toggleCheckBox.dispatch('on_update')
        monthlyGraph.dispatch('on_draw')
        yearlyGraph.dispatch('on_draw')
        if isNew == False:
            budget = savedBudgetInfo.getBudget()
            #budget order: work,entertainment,
            #charity,medical,utilities,other,food,transportation
            workPercentage.text = str(budget[0])
            entertainmentPercentage.text = str(budget[1])
            charityPercentage.text = str(budget[2])
            medicalPercentage.text = str(budget[3])
            utilitiesPercentage.text = str(budget[4])
            otherPercentage.text = str(budget[5])
            foodPercentage.text = str(budget[6])
            transportationPercentage.text = str(budget[7])
        if isNew == True:
            #If a new user is detected, an intro screen pops up
            #to introduce them to the program
            instructions = self.instructions
            label = Button(text=instructions,markup=True,
                    background_normal=
                    'C:/Users/Public/Documents/vintage-black-pattern.jpg',
                    background_color=(1,1,1,.5))
            popup = Popup(title="Welcome to PiggyBank!",
                    content=label,size_hint=(.9,.9))
            label.bind(on_press=popup.dismiss)
            popup.open()
            
    #I left the following function in as a comment, uncomment it and then
    #the program will always store your data, even if you dont press save
    #and simply X-out of the program. I decided my current way was more
    #ideal in case the user did not want to save.
       
    #def on_stop(self):
        #currentData.storeInfo(myGraphInfo,getAllPercentages,monthlyRevenue,
                    #savedGoalsInfo,savedBudgetInfo,revenuesAndExpedenturesList)
        #Writer.writeToFile()

#Kivy requires that you register all your classes so that
#it can recognize them
Factory.register('MyScrollScreen', cls=MyScrollScreen)
Factory.register('MyTextInput',cls=MyTextInput)
Factory.register('MyScreenManager',cls=MyScreenManager)
Factory.register('MySubmitButton',cls=MySubmitButton)
Factory.register('SubmitInfo',cls=SubmitInfo)
Factory.register('MyDateTextInput',cls=MyDateTextInput)
Factory.register('MyAmountTextInput',cls=MyAmountTextInput)
Factory.register('MyDescriptionTextInput',cls=MyDescriptionTextInput)
Factory.register('MyRevenueBackButton',cls=MyRevenueBackButton)
Factory.register('MySpinner',cls=MySpinner)
Factory.register('MyCurrencySpinner',cls=MyCurrencySpinner)
Factory.register('MyTypeSpinner',cls=MyTypeSpinner)
Factory.register('MyCategorySpinner',cls=MyCategorySpinner)
Factory.register('RevenuesAndExpedentures',cls=RevenuesAndExpedentures)
Factory.register('RevenuesAndExpedenturesList',
                 cls=RevenuesAndExpedenturesList)
Factory.register('QuitButton',cls=QuitButton)
Factory.register('MyScrollBox',cls=MyScrollBox)
Factory.register('MyAmountTextInputWrapper',cls=MyAmountTextInputWrapper)
Factory.register('MyDateTextInputWrapper',cls=MyDateTextInputWrapper)
Factory.register('MyDescriptionTextInputWrapper',
                 cls=MyDescriptionTextInputWrapper)
Factory.register('MyTypeSpinnerWrapper',cls=MyTypeSpinnerWrapper)
Factory.register('MyCurrencySpinnerWrapper',cls=MyCurrencySpinnerWrapper)
Factory.register('MyCategorySpinnerWrapper',cls=MyCategorySpinnerWrapper)
Factory.register('ChangeViewButton', cls=ChangeViewButton)
Factory.register('ExpenseAndRevenueStatus', cls=ExpenseAndRevenueStatus)
Factory.register('MyStatusLabel', cls=MyStatusLabel)
Factory.register('ConfigureBudgetScreen',cls=ConfigureBudgetScreen)
Factory.register('ConfigureRevenueScreen',cls=ConfigureRevenueScreen)
Factory.register('ConfigureGoalsScreen',cls=ConfigureGoalsScreen)
Factory.register('MyBudgetGraph',cls=MyBudgetGraph)
Factory.register('MyBudgetInfo', cls=MyBudgetInfo)
Factory.register('MyBudgetLayout', cls=MyBudgetLayout)
Factory.register('MyOtherTextInput', cls=MyOtherTextInput)
Factory.register('MyWorkTextInput',cls = MyWorkTextInput)
Factory.register('MyEntertainmentTextInput',cls=MyEntertainmentTextInput)
Factory.register('MyCharityTextInput',cls=MyCharityTextInput)
Factory.register('MyTransportationTextInput',cls=MyTransportationTextInput)
Factory.register('MyUtilitiesTextInput',cls=MyUtilitiesTextInput)
Factory.register('MyFoodTextInput',cls=MyFoodTextInput)
Factory.register('MyMedicalTextInput',cls=MyMedicalTextInput)
Factory.register('MySaveButton',cls=MySaveButton)
Factory.register('SavedGoalsInfo',cls=SavedGoalsInfo)
Factory.register('MyGoalsInfo',cls=MyGoalsInfo)
Factory.register('MyGoalsLayout',cls=MyGoalsLayout)
Factory.register('MySaveGoalsButton',cls=MySaveGoalsButton)
Factory.register('MonthlyRevenue',cls=MonthlyRevenue)
Factory.register('GetAllPercentages',cls=GetAllPercentages)
Factory.register('MyGoalsDateTextInput', cls=MyGoalsDateTextInput)
Factory.register('MyGoalsNameTextInput', cls=MyGoalsNameTextInput)
Factory.register('MyGoalsAmountTextInput', cls=MyGoalsAmountTextInput)
Factory.register('MyConfigureRevenueLayout', cls=MyConfigureRevenueLayout)
Factory.register('MyConfigureRevenueSubmitButton',
                 cls=MyConfigureRevenueSubmitButton)
Factory.register('ToggleCheckBox',cls=ToggleCheckBox)
Factory.register('MyConfigureRevenueTextInput',
                 cls=MyConfigureRevenueTextInput)
Factory.register('MyGraphInfo',cls=MyGraphInfo)
Factory.register('BudgetHelperButton',cls=BudgetHelperButton)
Factory.register('MyBudgetGraphWrapper',cls=MyBudgetGraphWrapper)
Factory.register('CurrentData',cls=CurrentData)
Factory.register('Writer',cls=Writer)
Factory.register('MyBudgetProgressBar',cls=MyBudgetProgressBar)
Factory.register('StatusAndProgress',cls=StatusAndProgress)
Factory.register('StatusAndProgressWrapper',cls=StatusAndProgressWrapper)
Factory.register('StatusScreen',cls=StatusScreen)
Factory.register('MyStatusDetailLayout',cls=MyStatusDetailWrapper)
Factory.register('MyStatusDetailWrapper',cls=MyStatusDetailWrapper)
Factory.register('CategoryDetails',cls=CategoryDetails)
Factory.register('MyRevenueStateLabel',cls=MyRevenueStateLabel)
Factory.register('MyRevenueStateLabelWrapper',cls=MyRevenueStateLabelWrapper)
Factory.register('OverflowDetails',cls=OverflowDetails)
Factory.register('MonthlyGraphWrapper',cls=MonthlyGraphWrapper)
Factory.register('YearlyGraphWrapper',cls=YearlyGraphWrapper)
Factory.register('LineGraph',cls=LineGraph)
Factory.register('LineGraphButton',cls=LineGraphButton)

if __name__ == '__main__':
    TestApp().run()