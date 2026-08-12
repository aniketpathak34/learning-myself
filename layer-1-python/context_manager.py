from contextlib import contextmanager
class MyManager:

    def __enter__(self):
         print("SETUP - entering")
         return self

    def printer(self):
         print("-==----------------")

    def __exit__(self, exc_type, exc, tb):
         print("CLEANUP - exiting")



# with MyManager() as m:
#     m.printer()
#     print("hi how are you")
#     raise ValueError("boom")

@contextmanager
def my_manager():
     print("entering")
     try:
          yield
     finally:
          print("clean up happend")


with my_manager() as m:
    print("hi how are you")
    raise ValueError("boom")