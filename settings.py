from functions import create_state_list

class Settings():
    def __init__(self):

        self.run = True
        self.files = {
                'dp1' : 'audio/wb/sample1_92bpm.wav',
                'dp2' : 'audio/wb/sample2_92bpm.wav',
                'dp3' : 'audio/wb/sample3_92bpm.wav',
                'dp4' : 'audio/wb/sample4_92bpm.wav',
                'dp5' : 'audio/wb/sample5_92bpm.wav',
                'kick1': 'audio/kick1.wav',
                'snare1' : 'audio/snare.wav',
                'hihat1' : 'audio/hihat.wav',
                'od1' : 'audio/oddisse1.wav',
                'od2' : 'audio/oddisse2.wav',
                'od3' : 'audio/oddisse3.wav',
                'od4' : 'audio/oddisse4.wav',
                'od5' : 'audio/oddisse5.wav',
                'od6' : 'audio/oddisse6.wav',
                'od7' : 'audio/oddisse7.wav',
                'od8' : 'audio/oddisse8.wav',
                'dr1' : 'audio/drum_loop1_110bpm_pt.wav',
                'da1' : 'audio/dangelo_higher1.wav',
                'da2' : 'audio/dangelo_higher2.wav',
                'da3' : 'audio/dangelo_higher3.wav',
                'jd_kick1':'audio/jd/kicks/kick1.wav',
                'jd_snare1':'audio/jd/snares/snare1.wav',
                'jd_hat1':'audio/jd/percs/hat1.wav',
                }
        self.sens = 270
        self.buffer_size = 256
        self.rate = 44100
        self.group1 = [4, 5, 8, 9, 10]
        self.dp = [4,5,8,9,10]
        self.od = [8,9,10,11]
        self.bank = 0
#        self.trigger = True
#        self.trigger2 = True
#        self.trigger3 = True
        self.run_GUI = True

        self.pads_status = create_state_list()
        self.triggers    = create_state_list()
        self.selected_pad = 0
