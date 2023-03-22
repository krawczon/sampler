import serial
port = '/dev/tty.wchusbserialfa130'
uart = serial.Serial(port, 115200)

def on_pads(pads, data, s, index):
    if pads[index] != None and s.pads_status[3] == False:
        if s.pads_status[index] and s.triggers[index] == False:
            s.triggers[index] = True
            if index in s.group1:
                for i in range(len(s.group1)):
                    pads[s.group1[i]].stop()
            pads[index].play()
            print('pad', index+1)
        if s.pads_status[index] == False:
            s.triggers[index] = False

def pads_status_update(data, s, i):
    if data[i] > s.sens:
        s.pads_status[i] = True
    if data[i] < s.sens - 20:
        s.pads_status[i] = False

def read_serial_data():
    pads_data = uart.readline()
    pads_data = pads_data.decode()
    data = eval(pads_data)
    return data

def create_state_list():
    pads_status = []
    for i in range(16):
        pads_status.append(False)
    return pads_status

def close_connection():
    uart.close()
    print('connection closed')

def mode(data, s, pad_number):
    if data[pad_number] > s.sens:
        if s.pads_status[0] == True and s.trigger:
            s.trigger = False
            print('ok')
    if data[pad_number] < s.sens -20:
        s.trigger = True

def on_press(s, pad_number, event, args):
    if s.pads_status[3]:
        pads = args
        if s.pads_status[pad_number]:
            if s.triggers[pad_number] == False:
                s.triggers[pad_number] = True
                event(s, args)
        if s.pads_status[pad_number] == False:
            s.triggers[pad_number] = False

def vol_lower(*args):
    s = args[0]
    pads = args[1]
    if pads[s.selected_pad].volume <= 10:
        pads[s.selected_pad].volume += 1

def vol_upper(*args):
    s = args[0]
    pads = args[1]
    if pads[s.selected_pad].volume > 0:
        pads[s.selected_pad].volume -= 1

def rate_upper(*args):
    s = args[0]
    pads = args[1]
    pads[s.selected_pad].rate += 1000
    print(pads[s.selected_pad].rate)

def rate_lower(*args):
    s = args[0]
    pads = args[1]
    pads[s.selected_pad].rate -= 1000
    print(pads[s.selected_pad].rate)

def bank_select(*args):
    s = args[0]
    if s.bank >= 3:
        s.bank = 0
    else:
        s.bank += 1
    print('bank', s.bank, 'selected')

def update_pads(*args):
    print('updated')
    s = args[0]
    pads = args[1]
    if pads[s.selected_pad] != None:
        pads[s.selected_pad].update()

def pad_select(s, i):
    if s.pads_status[i] == True:
        s.selected_pad = i
