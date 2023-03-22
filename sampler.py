import time
from pad import Pad
from settings import Settings
import functions as f

class Sampler():
    def __init__(self):
        
        self.s = Settings()
            
        self.wb1 = Pad(self.s, self.s.files['dp1'])
        self.wb2 = Pad(self.s, self.s.files['dp2'])
        self.wb3 = Pad(self.s, self.s.files['dp3'])
        self.wb4 = Pad(self.s, self.s.files['dp4'])
        self.wb5 = Pad(self.s, self.s.files['dp5'])
        self.kick = Pad(self.s, self.s.files['kick1'])
        self.snare = Pad(self.s, self.s.files['snare1'])
        self.hihat = Pad(self.s, self.s.files['hihat1'])
        self.od1 = Pad(self.s, self.s.files['od1'])
        self.od2 = Pad(self.s, self.s.files['od2'])
        self.od3 = Pad(self.s, self.s.files['od3'])
        self.od4 = Pad(self.s, self.s.files['od4'])
        self.od5 = Pad(self.s, self.s.files['od5'])
        self.od6 = Pad(self.s, self.s.files['od6'])
        self.od7 = Pad(self.s, self.s.files['od7'])
        self.od8 = Pad(self.s, self.s.files['od8'])
        self.dr1 = Pad(self.s, self.s.files['dr1'])
        self.da1 = Pad(self.s, self.s.files['da1'])
        self.da2 = Pad(self.s, self.s.files['da2'])
        self.da3 = Pad(self.s, self.s.files['da3'])

        self.jd_kick1 = Pad(self.s, self.s.files['jd_kick1'])
        self.jd_snare1 = Pad(self.s, self.s.files['jd_snare1'])
        self.jd_hat1 = Pad(self.s, self.s.files['jd_hat1'])

        self.bank0 = [None, None, None, None,
                None, None, None, None,
                self.da1, self.da2, self.da3, None,
                None, None, None, None]

        self.bank1 = [None, None, None, None,
                self.wb4, self.wb5, None, None,
                self.da1, self.da2, self.da3, None,
                self.dr1, self.jd_kick1, self.jd_snare1, self.jd_hat1]
        self.bank2 = [None, None, None, None,
                None, None, None, None,
                self.od1, self.od2, self.od3, self.od4,
                None, self.kick, self.snare, self.hihat]
        self.bank3 = [None, None, None, None,
                self.kick, self.kick, None, None,
                self.snare, self.snare, self.snare, self.snare,
                self.hihat, self.hihat, self.hihat, self.hihat]

        self.pads = self.bank0

    def run(self):
        while self.s.run:
            try:
                data = f.read_serial_data()
                for i in range(16):
                    f.pads_status_update(data, self.s, i)
                    f.on_pads(self.pads, data, self.s, i)

                if self.s.pads_status[3] == False:
                    f.pad_select(self.s, i)

                if self.s.bank == 0:
                    self.pads = self.bank0
                if self.s.bank == 1:
                    self.pads = self.bank1
                    self.s.group1 = self.s.dp
                if self.s.bank == 2:
                    self.pads = self.bank2
                    self.s.group1 = self.s.od
                if self.s.bank == 3:
                    self.pads = self.bank3
                
                f.on_press(self.s, 2, f.bank_select, None)
                f.on_press(self.s, 7, f.rate_upper, self.pads)
                f.on_press(self.s, 6, f.rate_lower, self.pads)
                f.on_press(self.s, 0, f.update_pads, self.pads)
                f.on_press(self.s, 4, f.vol_lower, self.pads)
                f.on_press(self.s, 5, f.vol_upper, self.pads)

#                f.on_press(self.s, 13, self.jd_kick1.play, None)
                
            except FileNotFoundError:
                print('Controller is not connected')
                print('conect controller')
            except OSError:
                print('oserror')
            except SyntaxError:
                print('SyntaxError')
                print('reading data issue')
            except IndexError:
                print('IndexError')
            except UnicodeDecodeError:
                print('UnicodeDecodeError')
#            except AttributeError:
#                print('AttributeError')
