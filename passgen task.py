{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "186b3019",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter password length: 4\n",
      "Choose character set for password from these : \n",
      "         1. Digits\n",
      "         2. Letters\n",
      "         3. Special characters\n",
      "         4. Exit\n",
      "Pick a number 1\n",
      "Pick a number 4\n",
      "The random password is oeQn\n"
     ]
    }
   ],
   "source": [
    "#!/usr/bin/env python\n",
    "# coding: utf-8\n",
    "\n",
    "# In[1]:\n",
    "\n",
    "\n",
    "\n",
    "import string\n",
    "import random\n",
    " \n",
    "# Getting password length\n",
    "length = int(input(\"Enter password length: \"))\n",
    " \n",
    "print('''Choose character set for password from these : \n",
    "         1. Digits\n",
    "         2. Letters\n",
    "         3. Special characters\n",
    "         4. Exit''')\n",
    " \n",
    "characterList = \"\"\n",
    " \n",
    "# Getting character set for password\n",
    "while(True):\n",
    "    choice = int(input(\"Pick a number \"))\n",
    "    if(choice == 1):\n",
    "         \n",
    "        # Adding letters to possible characters\n",
    "        characterList += string.ascii_letters\n",
    "    elif(choice == 2):\n",
    "         \n",
    "        # Adding digits to possible characters\n",
    "        characterList += string.digits\n",
    "    elif(choice == 3):\n",
    "         \n",
    "        # Adding special characters to possible\n",
    "        # characters\n",
    "        characterList += string.punctuation\n",
    "    elif(choice == 4):\n",
    "        break\n",
    "    else:\n",
    "        print(\"Please pick a valid option!\")\n",
    " \n",
    "password = []\n",
    " \n",
    "for i in range(length):\n",
    "   \n",
    "    # Picking a random character from our \n",
    "    # character list\n",
    "    randomchar = random.choice(characterList)\n",
    "     \n",
    "    # appending a random character to password\n",
    "    password.append(randomchar)\n",
    " \n",
    "# printing password as a string\n",
    "print(\"The random password is \" + \"\".join(password))\n",
    "\n",
    "\n",
    "# In[ ]:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "43c17513",
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
