# Vibe Coding
# Super_Advanced_Calculator_fixed.py
# Cleaned & more robust version of the Super Advanced Calculator

import tkinter as tk
from tkinter import messagebox
import math
import ast
import operator
import random

# ---------------- Safe evaluator ----------------
math_map = {
    'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
    'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
    'sqrt': math.sqrt, 'log': math.log10, 'ln': math.log,
    'pow': math.pow, 'abs': abs, 'round': round
}

allowed_operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

class EvalError(Exception):
    pass

def safe_eval(expr):
    try:
        node = ast.parse(expr, mode='eval')
        return _eval_node(node.body)
    except Exception as e:
        raise EvalError(str(e))

def _eval_node(node):
    if isinstance(node, ast.Constant):  # Python 3.8+
        if isinstance(node.value, (int, float)):
            return node.value
        raise EvalError('Invalid constant')
    if isinstance(node, ast.Num):  # older versions
        return node.n
    if isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type in allowed_operators:
            left = _eval_node(node.left)
            right = _eval_node(node.right)
            return allowed_operators[op_type](left, right)
        raise EvalError('Operator not allowed')
    if isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type in allowed_operators:
            operand = _eval_node(node.operand)
            return allowed_operators[op_type](operand)
        raise EvalError('Unary operator not allowed')
    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name):
            fname = node.func.id
            if fname in math_map:
                args = [_eval_node(a) for a in node.args]
                return math_map[fname](*args)
        raise EvalError('Function not allowed')
    raise EvalError('Invalid expression')

# ---------------- Rounded-ish Button (Canvas) ----------------
class RoundedButton(tk.Canvas):
    def __init__(self, master, text="", command=None,
                 width=70, height=50,
                 bg="#141414", fg="#A8FFF0",
                 font=("Segoe UI", 10, "bold")):

        super().__init__(master, width=width, height=height,
                         bg=master.cget("bg"), highlightthickness=0)

        self.text = text
        self.command = command
        self.width = width
        self.height = height
        self.bg_color = bg
        self.fg_color = fg
        self.font = font

        self._draw_button()

        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _draw_button(self):
        self.create_rectangle(
            5, 5, self.width - 5, self.height - 5,
            outline="", fill=self.bg_color, tags="bg"
        )

        self.create_text(
            self.width // 2, self.height // 2,
            text=self.text, fill=self.fg_color,
            font=self.font, tags="text"
        )

    def _on_press(self, event):
        self.move("text", 0, 2)
        self.move("bg", 0, 2)

    def _on_release(self, event):
        self.move("text", 0, -2)
        self.move("bg", 0, -2)
        if self.command:
            self.command()
# ---------------- Main App ----------------
class SuperCalc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Super Advanced Calculator')
        self.geometry('480x680')
        self.configure(bg='#0D0D0D')
        self.memory = 0.0
        self.history = []
        self._create_ui()
        self.bind_keys()

    def _create_ui(self):
        top = tk.Frame(self, bg='#0D0D0D')
        top.pack(fill='x', padx=12, pady=(12,0))
        title = tk.Label(top, text='Super Calculator', fg='#E6FFFF', bg='#0D0D0D', font=('Segoe UI', 14, 'bold'))
        title.pack(side='left')
        theme_btn = tk.Button(top, text='Theme', command=self.toggle_theme, bg='#141414', fg='#00FFE8')
        theme_btn.pack(side='right')

        disp_frame = tk.Frame(self, bg='#0D0D0D')
        disp_frame.pack(fill='x', padx=12, pady=12)
        self.display_var = tk.StringVar()
        display = tk.Entry(disp_frame, textvariable=self.display_var, font=('Consolas', 28), bd=0, justify='right')
        display.pack(fill='x', ipady=18, padx=6, pady=6)
        display.configure(bg='#101214', fg='#DFFFEF', insertbackground='#DFFFEF')
        self.display = display

        self.preview_var = tk.StringVar()
        preview = tk.Label(disp_frame, textvariable=self.preview_var, anchor='e', bg='#0D0D0D', fg='#7EF0E0', font=('Consolas', 10))
        preview.pack(fill='x')

        buttons_frame = tk.Frame(self, bg='#0D0D0D')
        buttons_frame.pack(padx=12, pady=8)

        layout = [
            ['MC','MR','M+','M-','(',')','⌫','C'],
            ['sin','cos','tan','sqrt','^','log','ln','%'],
            ['7','8','9','÷','pi','e','Ans','Hist'],
            ['4','5','6','×','!','±','mod','Rand'],
            ['1','2','3','-','EXP','Copy','Mode','='],
            ['0','00','.','+']
        ]

        for r, row in enumerate(layout):
            rowf = tk.Frame(buttons_frame, bg='#0D0D0D')
            rowf.pack(fill='x')
            for label in row:
                cmd = lambda x=label: self.on_button(x)
                btn = RoundedButton(rowf, text=label, command=cmd, width=62, height=50, bg='#141414', fg='#A8FFF0')
                btn.pack(side='left', padx=6, pady=6)

        self.history_win = None

    def bind_keys(self):
        for k in '0123456789.+-*/()':
            self.bind(k, lambda e, ch=k: self._insert(ch))
        self.bind('<Return>', lambda e: self._equal())
        self.bind('<BackSpace>', lambda e: self._backspace())
        self.bind('<Escape>', lambda e: self._clear())

    def _insert(self, ch):
        self.display.insert(tk.END, ch)
        self._try_preview()

    def _backspace(self):
        cur = self.display.get()
        if cur:
            self.display_var.set(cur[:-1])
            self._try_preview()

    def _clear(self):
        self.display_var.set('')
        self.preview_var.set('')

    def _try_preview(self):
        expr = self.display.get()
        if not expr:
            self.preview_var.set('')
            return
        try:
            safe_expr = expr.replace('×','*').replace('÷','/').replace('^','**')
            val = safe_eval(safe_expr)
            self.preview_var.set(str(val))
        except Exception:
            self.preview_var.set('')

    def on_button(self, label):
        if label in {'0','1','2','3','4','5','6','7','8','9','.', '00'}:
            if label == '00':
                self.display.insert(tk.END, '00')
            else:
                self.display.insert(tk.END, label)
            self._try_preview()
            return
        if label in {'+','-','×','÷','*','/','(',')','^','%','mod'}:
            mapping = {'×':'*','÷':'/','mod':'%'}
            self.display.insert(tk.END, mapping.get(label, label))
            self._try_preview()
            return
        if label == 'C':
            self._clear(); return
        if label == '⌫':
            self._backspace(); return
        if label == '=':
            self._equal(); return
        if label == 'Ans':
            if self.history:
                self.display.insert(tk.END, str(self.history[-1][1])); return
        if label == 'Copy':
            self.clipboard_clear(); self.clipboard_append(self.display.get()); return
        if label == 'Hist':
            self.show_history(); return
        if label == 'pi':
            self.display.insert(tk.END, str(math.pi)); return
        if label == 'e':
            self.display.insert(tk.END, str(math.e)); return
        if label == '±':
            cur = self.display.get()
            if cur.startswith('-'):
                self.display_var.set(cur[1:])
            else:
                self.display_var.set('-'+cur)
            return
        if label == 'Rand':
            self.display.insert(tk.END, str(random.random())); return
        if label == 'sqrt':
            self.display.insert(tk.END, 'sqrt('); return
        if label in {'sin','cos','tan','log','ln'}:
            self.display.insert(tk.END, f"{label}("); return
        if label == 'EXP':
            self.display.insert(tk.END, 'e'); return
        if label == 'MC':
            self.memory = 0.0; return
        if label == 'MR':
            self.display.insert(tk.END, str(self.memory)); return
        if label == 'M+':
            try:
                val = float(safe_eval(self.display.get().replace('×','*').replace('÷','/').replace('^','**')))
                self.memory += val
            except Exception:
                pass
            return
        if label == 'M-':
            try:
                val = float(safe_eval(self.display.get().replace('×','*').replace('÷','/').replace('^','**')))
                self.memory -= val
            except Exception:
                pass
            return
        if label == 'Mode':
            messagebox.showinfo('Mode', 'More modes coming soon'); return
        # fallback:
        self.display.insert(tk.END, label)

    def _equal(self):
        expr = self.display.get()
        if not expr.strip():
            return
        try:
            safe_expr = expr.replace('×','*').replace('÷','/').replace('^','**')
            val = safe_eval(safe_expr)
            self.history.append((expr, val))
            self.display_var.set(str(val))
            self.preview_var.set('')
        except EvalError:
            self.display_var.set('Error')
        except Exception:
            self.display_var.set('Error')

    def show_history(self):
        if self.history_win and tk.Toplevel.winfo_exists(self.history_win):
            self.history_win.lift(); return
        hw = tk.Toplevel(self); hw.title('History'); hw.geometry('360x420'); hw.configure(bg='#0D0D0D')
        self.history_win = hw
        lb = tk.Listbox(hw, bg='#101214', fg='#A8FFF0', font=('Consolas', 12)); lb.pack(fill='both', expand=True, padx=8, pady=8)
        for expr, val in reversed(self.history[-200:]): lb.insert(tk.END, f"{expr} = {val}")
        def use_selected():
            sel = lb.curselection()
            if sel:
                text = lb.get(sel[0]); expr = text.split(' = ')[0]; self.display_var.set(expr); hw.destroy()
        btn = tk.Button(hw, text='Use Selected', command=use_selected, bg='#141414', fg='#00FFE8'); btn.pack(pady=6)

    def toggle_theme(self):
        cur = self.cget('bg')
        if cur == '#0D0D0D':
            self.configure(bg='#F5F5F5'); self._set_widgets_bg('#FFFFFF','#0B3B3B')
        else:
            self.configure(bg='#0D0D0D'); self._set_widgets_bg('#0D0D0D','#A8FFF0')

    def _set_widgets_bg(self, bg, fg):
        for w in self.winfo_children():
            try:
                w.configure(bg=bg)
            except Exception:
                pass

if __name__ == '__main__':
    app = SuperCalc()
    app.mainloop()
