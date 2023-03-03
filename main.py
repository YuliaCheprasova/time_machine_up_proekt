import datetime
class wish():
    """The class that generates wish of a person through dialogue"""
    def subject(self) -> str:
        """The method that determines a subject of sending"""
        print('I want to send (write who or what) ')
        who = input()
        return who
    def place(self, who: str) -> str:
        """The method that determines a place of sending"""
        print('I want to send a ', who, ' to (write anywhere in the world) ')
        where = input()
        return where
    def time(self, who: str, where: str) -> int:
        """The method that determines the date of sending
        and calculates the difference between it and the present time"""
        while (1):
            print(
                'I want to send a ', who,' to ', where, ' in (write the date you want in the '
                                                        'year-month-date format, for example, 2028-06-09) ')
            when = input()
            when = datetime.datetime.strptime(when, '%Y-%m-%d')
            when = when.date()
            now = datetime.datetime.now()
            now = now.date()
            tdelta = when - now
            tdelta = tdelta.days
            if tdelta <= 0:
                print(
                    "You may have entered a past date, please note that the machine "
                    "can only move objects into the future! Try again, please ")
            else:
                return tdelta
class time_machine():
    """The class that simulates actions of the time machine"""
    def request(self, who: str, where: str, tdelta: int):
        """The method that generates the sending message"""
        print('I am sending a ', who, ' to ', where,' ', str(tdelta), ' days forward')
    def result(self):
        """The method that sends message about successful sending"""
        print('Sending was successful')

def __main__():
    print("Pay attention! The time machine moves objects only into the future")
    a = wish()
    b = time_machine()
    who = a.subject()
    where = a.place(who)
    when = a.time(who, where)
    b.request(who, where, when)
    b.result()

help(wish)