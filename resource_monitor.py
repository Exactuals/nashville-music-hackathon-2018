from stoppable_thread import StoppableThread


class ResourceManager(StoppableThread):
    def __init__(self, target_lib_call, arg1):
        super(ResourceManager, self).__init__()
        self.target_function = target_lib_call
        self.arg1 = arg1

        self.results = None

    def startup(self):
        # Overload the startup function
        print("Calling the Target Function...")

    def cleanup(self):
        # Overload the cleanup function
        print("Function Call Complete")

    def mainloop(self):
        # Start the library Call
        self.target_function(self.arg1)

        # Kill the thread when complete
        self.stop()


