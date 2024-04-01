from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def btn_sapxep_click(self, **event_args):
    if not self.txt_nhap.text:
      alert("Bạn chưa nhập dãy số.")
      return
    number_list = [int(num) for num in self.txt_nhap.text.split()]
  
    sorted_list = self.bubble_sort(number_list)
    
    self.txt_xuat.text = ' '.join(map(str, sorted_list))
    
  def bubble_sort(self, arr):
    n = len(arr)
    for i in range(n):
      for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
          arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
