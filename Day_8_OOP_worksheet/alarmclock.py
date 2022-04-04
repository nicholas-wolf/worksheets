class Alarm_Clock:
    def __init__(self, current_time, alarm_time, alarm_on_off):
        self.current_time = current_time
        self.alarm_on_off = alarm_on_off
        self.alarm_time = alarm_time
        self.alarm_bool = False

    def display_time(self):
        print(self.current_time)

    def input_current_time(self):
        self.current_time = input("Enter time: ")
        print("Time changed to: ", self.current_time)


    def input_alarm_on_off(self):
        self.alarm_on_off = input("Turn alarm on or off?")
        if self.alarm_on_off == "on":
            print("ALARM ON") 
            self.alarm_bool = True

        else:
            print("ALARM OFF")
            self.alarm_bool = False

    def input_alarm_time(self):
        self.alarm_time = input("Enter alarm time: ")
        print("Alarm set to:", self.alarm_time)    


