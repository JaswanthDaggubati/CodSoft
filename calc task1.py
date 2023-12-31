{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fd2d4062",
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import *\n",
    "import math\n",
    "root=Tk()\n",
    "root.title(\"jaswanth calculator\")\n",
    "e=Entry(root,borderwidth=10,width=20)\n",
    "m=e.get()\n",
    "e.grid(row=0,column=0,columnspan=3)\n",
    "\n",
    "def button_add():\n",
    "    f_num=e.get()\n",
    "    global first\n",
    "    global jaswanth\n",
    "    jaswanth=\"addition\"\n",
    "    e.delete(0,END)\n",
    "    first=float(f_num)\n",
    "def button_sub():\n",
    "    f_num=e.get()\n",
    "    global first\n",
    "    global jaswanth\n",
    "    jaswanth=\"subtraction\"\n",
    "    e.delete(0,END)\n",
    "    first=float(f_num)\n",
    "def button_mull():   \n",
    "    f_num=e.get()\n",
    "    global first\n",
    "    global jaswanth\n",
    "    jaswanth=\"multiplication\"\n",
    "    e.delete(0,END)\n",
    "    first=float(f_num)\n",
    "def button_div():\n",
    "    f_num=e.get()\n",
    "    global first\n",
    "    global jaswanth\n",
    "    jaswanth=\"division\"\n",
    "    e.delete(0,END)\n",
    "    first=float(f_num)\n",
    "def button_clear():\n",
    "    e.delete(0,END)\n",
    "def button_dot():\n",
    "    present = e.get()\n",
    "    if '.' not in present:\n",
    "        e.delete(0, END)\n",
    "        e.insert(0, present + '.')\n",
    "    jaswanth=\"dot\"\n",
    "def button_press(num):\n",
    "    present=e.get()\n",
    "    e.delete(0,END)\n",
    "    e.insert(0,str(present)+str(num))\n",
    "def button_equal():\n",
    "    s_num=e.get()\n",
    "    e.delete(0,END)\n",
    "    if jaswanth==\"addition\":\n",
    "        e.insert(0,first+float(s_num))\n",
    "    if jaswanth==\"subtraction\":\n",
    "        e.insert(0,first-float(s_num))\n",
    "    if jaswanth==\"multiplication\":\n",
    "        e.insert(0,first*float(s_num))\n",
    "    if jaswanth==\"division\":\n",
    "        e.insert(0,first/float(s_num))\n",
    "    if jaswanth==\"dot\":\n",
    "        e.insert(0,first + \".\" )\n",
    "\n",
    "button1=Button(root,text=\"1\",padx=40,pady=20,bg=\"#58FC00\",command=lambda:button_press(1))\n",
    "button2=Button(root,text=\"2\",padx=40,pady=20,bg=\"#58FC00\",command=lambda:button_press(2))\n",
    "button3=Button(root,text=\"3\",padx=40,pady=20,bg=\"#58FC00\",command=lambda:button_press(3))\n",
    "button4=Button(root,text=\"4\",padx=40,pady=20,bg=\"#58FC00\",command=lambda:button_press(4))\n",
    "button5=Button(root,text=\"5\",padx=40,pady=20,bg=\"#58FC00\",command=lambda:button_press(5))\n",
    "button6=Button(root,text=\"6\",padx=40,pady=20,bg=\"#58FC00\",command=lambda:button_press(6))\n",
    "button7=Button(root,text=\"7\",padx=40,pady=20,bg=\"#58FC00\",command=lambda:button_press(7))\n",
    "button8=Button(root,text=\"8\",padx=40,pady=20,bg=\"#58FC00\",command=lambda:button_press(8))\n",
    "button9=Button(root,text=\"9\",padx=40,pady=20,bg=\"#58FC00\",command=lambda:button_press(9))\n",
    "button0=Button(root,text=\"0\",padx=40,pady=20,bg=\"#58FC00\",command=lambda:button_press(0))\n",
    "button_add=Button(root,text=\"+\",padx=40,pady=20,bg=\"#58FC00\",command=button_add)\n",
    "button_sub=Button(root,text=\"-\",padx=40,pady=20,bg=\"#58FC00\",command=button_sub)\n",
    "button_mull=Button(root,text=\"*\",padx=40,pady=20,bg=\"#58FC00\",command=button_mull)\n",
    "button_div=Button(root,text=\"/\",padx=40,pady=20,bg=\"#58FC00\",command=button_div)\n",
    "button_dot=Button(root,text=\".\",padx=41,pady=20,bg=\"#58FC00\",command=button_dot)\n",
    "button_equal=Button(root,text=\"=\",padx=40,pady=20,bg=\"#58FC00\",command=button_equal)\n",
    "#button_fdi=Button(root,text=\"%\",padx=40,pady=20,bg=\"#58FC00\",command=button_fdi)\n",
    "button_clear=Button(root,text=\"Clear\",padx=30,pady=20,bg=\"#58FC00\",command=button_clear)\n",
    "\n",
    "button1.grid(row=3,column=0)\n",
    "button2.grid(row=3,column=1)\n",
    "button3.grid(row=3,column=2)\n",
    "button4.grid(row=2,column=0)\n",
    "button5.grid(row=2,column=1)\n",
    "button6.grid(row=2,column=2)\n",
    "button7.grid(row=1,column=0)\n",
    "button8.grid(row=1,column=1)\n",
    "button9.grid(row=1,column=2)\n",
    "button_add.grid(row=3,column=3)\n",
    "button_sub.grid(row=2,column=3)\n",
    "button_mull.grid(row=1,column=3)\n",
    "button_div.grid(row=0,column=3)\n",
    "button_dot.grid(row=4,column=1)\n",
    "button_equal.grid(row=4,column=3)\n",
    "#button_fdi.grid(row=0,column=2)\n",
    "button_clear.grid(row=4,column=2)\n",
    "button0.grid(row=4,column=0)\n",
    "\n",
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "750e1b7f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1b6565a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
