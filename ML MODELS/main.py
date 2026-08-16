import customtkinter as ctk
from colorama import Fore, Style, init
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Initialize colorama
init(autoreset=True)

# Set CustomTkinter theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# ==========================================
# MODEL CALCULATION (OLS LINEAR REGRESSION)
# ==========================================
X = [1, 2, 3, 4, 5]
Y = [30, 40, 50, 60, 70]

x_mean = sum(X) / len(X)
y_mean = sum(Y) / len(Y)

numerator = sum((X[i] - x_mean) * (Y[i] - y_mean) for i in range(len(X)))
denominator = sum((X[i] - x_mean) ** 2 for i in range(len(X)))

b1 = numerator / denominator
b0 = y_mean - b1 * x_mean

# GUI SETUP
root = ctk.CTk()
root.title("Salary Prediction ML Model")
root.geometry("560x650")

container = ctk.CTkFrame(root, corner_radius=0)
container.pack(fill="both", expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

frames = {}

def show_frame(page_name):
    frame = frames[page_name]
    frame.tkraise()

# ==========================================
# PAGE 1: LANDING PAGE
# ==========================================
landing_frame = ctk.CTkFrame(container, corner_radius=0)
frames["LandingPage"] = landing_frame
landing_frame.grid(row=0, column=0, sticky="nsew")

title_label = ctk.CTkLabel(landing_frame, text="Salary Predictor ML Model", font=("Segoe UI", 22, "bold"))
title_label.pack(pady=(25, 2))

subtitle = ctk.CTkLabel(landing_frame, text="Simple Linear Regression Project", font=("Segoe UI", 12, "italic"), text_color="gray")
subtitle.pack(pady=(0, 20))

card1 = ctk.CTkFrame(landing_frame, corner_radius=12)
card1.pack(padx=30, pady=8, fill="x")
ctk.CTkLabel(card1, text="📌 Model Purpose", font=("Segoe UI", 13, "bold")).pack(anchor="w", padx=20, pady=(12, 4))
ctk.CTkLabel(card1, text="Predicts employee salary using Ordinary Least Squares\n(OLS) regression based on years of experience.", font=("Segoe UI", 11), justify="left", text_color=("gray20", "gray80")).pack(anchor="w", padx=20, pady=(0, 12))

card2 = ctk.CTkFrame(landing_frame, corner_radius=12)
card2.pack(padx=30, pady=8, fill="x")
ctk.CTkLabel(card2, text="⚡ Technical Specs", font=("Segoe UI", 13, "bold")).pack(anchor="w", padx=20, pady=(12, 4))
specs_text = "• Algorithm: Simple Linear Regression\n• Math Formula: Y = b0 + b1*X\n• Feature (X): Experience (Years)\n• Target (Y): Salary (Thousands)"
ctk.CTkLabel(card2, text=specs_text, font=("Segoe UI", 11), justify="left", text_color=("gray20", "gray80")).pack(anchor="w", padx=20, pady=(0, 12))

launch_btn = ctk.CTkButton(landing_frame, text="Start Prediction →", font=("Segoe UI", 13, "bold"), height=42, corner_radius=8, command=lambda: show_frame("ModelPage"))
launch_btn.pack(pady=25, ipadx=10)

# ==========================================
# PAGE 2: SALARY PREDICTION & GRAPH ON DEMAND
# ==========================================
model_frame = ctk.CTkFrame(container, corner_radius=0)
frames["ModelPage"] = model_frame
model_frame.grid(row=0, column=0, sticky="nsew")

title = ctk.CTkLabel(model_frame, text="Linear Regression - Salary Prediction\nY = b0 + b1*X", font=("Segoe UI", 18, "bold"), text_color="#1976D2")
title.pack(pady=(15, 5))

info_text = f"b0 = {b0:.2f}\nb1 = {b1:.2f}\nEquation: Y = {b0:.2f} + {b1:.2f}X"
info_label = ctk.CTkLabel(model_frame, text=info_text, font=("Segoe UI", 11), text_color="#2E7D32", justify="center")
info_label.pack(pady=2)

input_label = ctk.CTkLabel(model_frame, text="Enter Years of Experience:", font=("Segoe UI", 12))
input_label.pack(pady=4)

entry = ctk.CTkEntry(model_frame, font=("Segoe UI", 14), width=180, height=35, justify="center")
entry.pack(pady=4)

# Global tracking variables for prediction state
current_exp = None
current_sal = None

def predict():
    global current_exp, current_sal
    try:
        current_exp = float(entry.get())
        current_sal = b0 + b1 * current_exp
        result_label.configure(text=f"Y = b0 + b1*X\nPredicted Salary (y) = {current_sal:.2f} thousand")
        graph_button.pack(pady=8)  # Reveal graph button after successful prediction
        print(Fore.GREEN + Style.BRIGHT + f"[PREDICTION SUCCESS] X: {current_exp} yrs -> Y: {current_sal:.2f}k")
    except ValueError:
        result_label.configure(text="⚠️ Please enter a valid number")
        print(Fore.RED + Style.BRIGHT + "[ERROR] Invalid input entered.")

predict_button = ctk.CTkButton(model_frame, text="Predict Salary", command=predict, font=("Segoe UI", 12, "bold"), height=36, corner_radius=8)
predict_button.pack(pady=10)

result_label = ctk.CTkLabel(model_frame, text="Y = b0 + b1*X\nPredicted Salary (y) = ", font=("Segoe UI", 13, "bold"), text_color=("#059669", "#34D399"))
result_label.pack(pady=5)

# Matplotlib Figure & Frame Setup (Hidden Initially)
graph_container = ctk.CTkFrame(model_frame, corner_radius=8)
fig = Figure(figsize=(4.8, 2.5), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=graph_container)
canvas.get_tk_widget().pack(fill="both", expand=True, padx=5, pady=5)

def toggle_graph():
    if graph_container.winfo_ismapped():
        graph_container.pack_forget()
        graph_button.configure(text="View Graph Representation 📊")
    else:
        # Plot regression line & prediction point
        ax.clear()
        ax.scatter(X, Y, color='#1976D2', label='Training Data', zorder=3)
        
        line_x = [min(X)-0.5, max(X)+0.5]
        if current_exp is not None:
            line_x = [min(min(X)-0.5, current_exp-0.5), max(max(X)+0.5, current_exp+0.5)]
        line_y = [b0 + b1 * x for x in line_x]
        
        ax.plot(line_x, line_y, color='#059669', linewidth=2, label='Regression Line')
        
        if current_exp is not None and current_sal is not None:
            ax.scatter([current_exp], [current_sal], color='red', s=70, zorder=4, label=f'Point ({current_exp:.1f}, {current_sal:.1f}k)')
            ax.axvline(x=current_exp, color='gray', linestyle='--', alpha=0.5)
            ax.axhline(y=current_sal, color='gray', linestyle='--', alpha=0.5)

        ax.set_title("Salary vs Experience Plot", fontsize=9, fontweight='bold')
        ax.set_xlabel("Experience (Years)", fontsize=8)
        ax.set_ylabel("Salary (Thousands)", fontsize=8)
        ax.legend(loc='upper left', fontsize=7)
        ax.grid(True, linestyle=':', alpha=0.6)
        fig.tight_layout()
        canvas.draw()
        
        graph_container.pack(pady=8, padx=20, fill="x")
        graph_button.configure(text="Hide Graph Representation ✖")

# Graph Button (Appears only after predicting)
graph_button = ctk.CTkButton(
    model_frame,
    text="View Graph Representation 📊",
    command=toggle_graph,
    font=("Segoe UI", 11, "bold"),
    fg_color="#4F46E5",
    hover_color="#4338CA",
    height=34,
    corner_radius=8
)

back_button = ctk.CTkButton(
    model_frame,
    text="← Back to Overview",
    font=("Segoe UI", 11),
    fg_color="transparent",
    border_width=1,
    command=lambda: show_frame("LandingPage")
)
back_button.pack(pady=(10, 15))

show_frame("LandingPage")
root.mainloop()
