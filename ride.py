class demo:
    def run(self):
        print("i can run from demo")
class sample(demo):
    def run(self):
        print("running from sample now")
a = sample()
a.run()
