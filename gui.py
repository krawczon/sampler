from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class DataLayout(GridLayout):
    def __init__(self, sampler, pos):
        super().__init__()

        self.sampler = sampler
        self.pos = pos
        self.cols = 2
        self.rows = 4
        self.size = (300, 400)
        self.labels = []
        for i in range(8):
            label = Label(text = str(i))
            self.labels.append(label)
            self.add_widget(self.labels[i])

        self.name_labels()

    def update(self):
        self.labels[5].text = str(self.sampler.s.bank)
        self.labels[1].text = str(self.sampler.s.selected_pad)
        if self.sampler.pads[self.sampler.s.selected_pad] != None:
            self.labels[3].text = str(self.sampler.pads[self.sampler.s.selected_pad].rate)
            self.labels[7].text = str(round(10/self.sampler.pads[self.sampler.s.selected_pad].volume, 2))
        else:
            self.labels[3].text = 'n/a'
            self.labels[7].text = 'n/a'

    def name_labels(self):
        self.labels[0].text = 'pad nr'
        self.labels[2].text = 'sample rate'
        self.labels[4].text = 'suond bank'
        self.labels[6].text = 'volume'

class Screen(Widget):
    def __init__(self, sampler):
        super().__init__()

        self.sampler = sampler
        self.pad_matrix = []
        self.create_pad_matrix()
        self.data_layout = DataLayout(self.sampler, pos = (400, 100))
        self.add_widget(self.data_layout)
        self.name_pads()

        Clock.schedule_interval(self.update, 0)

        self.trigger = True
        self.new_selected_pad = self.sampler.s.selected_pad
        self.new_bank = self.sampler.s.bank

    def update(self, event):
        self.mode_button()
        if self.sampler.s.pads_status[3] == False:
            self.trigger = True
            self.name_pads()
        self.data_layout.update()
        self.close_app()
        for i in range(16):
            if self.sampler.s.pads_status[i]:
                self.pad_matrix[i].state = 'down'
            else:
                self.pad_matrix[i].state = 'normal'

#        self.pad_matrix[self.sampler.s.selected_pad].background_normal = ''
        if self.new_bank != self.sampler.s.bank:
            self.color_active_pads()
            self.new_bank = self.sampler.s.bank

        if self.new_selected_pad == self.sampler.s.selected_pad:
            self.pad_matrix[self.sampler.s.selected_pad].background_color = [0, 1, 1, 1]
       
        
        if self.new_selected_pad != self.sampler.s.selected_pad:
            self.pad_matrix[self.new_selected_pad].background_color = [1, 1, 1, 1]
            self.new_selected_pad = self.sampler.s.selected_pad

            
    def create_pad_matrix(self):
        posx = 0
        posy = 400
        for i in range(4):
            for i in range(4):
                button = Button(pos = (posx, posy))
                self.pad_matrix.append(button)
                posx += 100
            posx = 0
            posy -= 100

        for i in range(len(self.pad_matrix)):
            self.add_widget(self.pad_matrix[i])

        self.pad_matrix[3].text = 'mode'

    def close_app(self):
        if self.pad_matrix[3].state == 'down':
            if self.pad_matrix[12].state == 'down':
                self.sampler.s.run = False
                print('closing')
                App.get_running_app().stop()
                Window.close()

    def mode_button(self):
        if self.sampler.s.pads_status[3] and self.trigger:
            self.trigger = False
            for i in range(16):
                if i != 3:
                    self.pad_matrix[i].text = ''
            self.pad_matrix[2].text = 'select bank'
            self.pad_matrix[6].text = 'rate -'
            self.pad_matrix[7].text = 'rate +'
            self.pad_matrix[0].text = 'update'
            self.pad_matrix[12].text = 'quit'
            self.pad_matrix[4].text = 'vol -'
            self.pad_matrix[5].text = 'vol +'
            
    def name_pads(self):
        counter = 0
        for i in range(16):
            if i != 3:
                self.pad_matrix[i].text = str(i)
            counter += 1

    def color_active_pads(self):
        for i in range(16):
            if self.sampler.pads[i] != None:
                self.pad_matrix[i].background_color = (0.5,0.5,0.5,1)
            else:
                self.pad_matrix[i].background_color = (1,1,1,1)
