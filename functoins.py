{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "583b21f6-c0a3-4127-b19f-dedcbf016a9f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello students\n",
      "ganesh ganesh ganesh ganesh ganesh \n"
     ]
    }
   ],
   "source": [
    "#functions:\n",
    "#pre defind functions\n",
    "#user defind functions\n",
    "\n",
    "#user defind functions:\n",
    "#def functionname(parameters):\n",
    "   #return value\n",
    "#1. no arg pass no return value \n",
    "#2.agr pass with return value\n",
    "#3. arg pass without return value\n",
    "#4. no arg for return values\n",
    "def hi(): #callee \n",
    "    print(\"hello students\") #responses of callee\n",
    "    print(\"ganesh \"*5)\n",
    "hi() #caller"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "cd744f85-ca37-4199-a845-a42d050923a2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the money:  22\n",
      "enter the money:  25\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "total amount: 47\n"
     ]
    }
   ],
   "source": [
    "#function with parameters\n",
    "def add(student1, student2):\n",
    "    return student1 + student2\n",
    "student1=int(input(\"enter the money: \"))\n",
    "student2=int(input(\"enter the money: \"))\n",
    "total= add(student1, student2)\n",
    "print(\"total amount:\", total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b5bc9707-5892-4423-a217-8952796d8c44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the money:  22\n",
      "enter the money:  12\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "total: 34\n"
     ]
    }
   ],
   "source": [
    "#function with parameters/return value\n",
    "def add(student1, student2):\n",
    "    print(\"total:\", student1 + student2)\n",
    "student1=int(input(\"enter the money: \"))\n",
    "student2=int(input(\"enter the money: \"))\n",
    "add(student1, student2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "3170e322-3934-4452-ba8b-e6c02f2bd3ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "value in the function is 3.14159\n"
     ]
    }
   ],
   "source": [
    "# no_arguments_return_value.py\n",
    "def value():\n",
    "    return 3.14159\n",
    "result=value()\n",
    "print(\"value in the function is\", result)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "d4a74556-b7dc-4db9-820d-8e3e8e0b48ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your name:  ganesh\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "wellcome  ganesh\n"
     ]
    }
   ],
   "source": [
    "def get_name():\n",
    "    name= input(\"enter your name: \")\n",
    "    return name\n",
    "username=get_name()\n",
    "print(\"wellcome \", username)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "04e33abf-3cd6-4501-bfe2-8b2da2cdfe57",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "118\n"
     ]
    }
   ],
   "source": [
    "a=100\n",
    "def value(a):\n",
    "    return a+18\n",
    "op=value(a)\n",
    "print(op)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "a850dcba-cd33-44ff-8bf8-2435ec8aaeb8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name: ganesh\n",
      "age: 20\n",
      "name: mark\n",
      "age: 0\n",
      "name: unknown\n",
      "age: 33\n",
      "name: unknown\n",
      "age: 0\n"
     ]
    }
   ],
   "source": [
    "def info(name='unknown', age=0):\n",
    "    print(\"name:\",name)\n",
    "    print(\"age:\", age)\n",
    "info(\"ganesh\", 20)\n",
    "info(\"mark\")\n",
    "info(age=33)\n",
    "info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "6347fa7b-8148-44d6-b34c-0fd7a4b75329",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a: 12\n",
      "enter b: 13\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sum= 25\n",
      "diff= -1\n",
      "pro= 156\n",
      "div= 0.9230769230769231\n"
     ]
    }
   ],
   "source": [
    "def cal(a,b):\n",
    "    return a+b, a-b, a*b, a/b\n",
    "a=int(input(\"enter a:\"))\n",
    "b=int(input(\"enter b:\"))\n",
    "sum, diff, pro, div= cal(a,b)\n",
    "print(\"sum=\", sum)\n",
    "print(\"diff=\", diff)\n",
    "print(\"pro=\", pro)\n",
    "print(\"div=\", div)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "4670b12e-a130-4e4a-a01b-33fafe20c3cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a: 12\n",
      "enter b: 23\n",
      "enter c: 10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "min= 10\n",
      "max= 23\n"
     ]
    }
   ],
   "source": [
    "#write a function..........\n",
    "def cal(a,b,c):\n",
    "    return max(a,b,c), min(a,b,c)\n",
    "a=int(input(\"enter a:\"))\n",
    "b=int(input(\"enter b:\"))\n",
    "c=int(input(\"enter c:\"))\n",
    "min, max=cal(a,b,c)\n",
    "print(\"min=\", min)\n",
    "print(\"max=\", max)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d10dcf5-dce6-48d2-99b5-c43759f9cf66",
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
