import tkinter as tk


class RailwayDashboard:

    def __init__(self, root):

        self.root = root
        self.root.title("Smart Railway Level Crossing Safety System")
        self.root.geometry("1250x720")
        self.root.resizable(False, False)
        self.root.configure(bg="#101820")

        # ==========================================================
        # SYSTEM STATE
        # ==========================================================

        self.running = False

        self.train_detected = False
        self.gates_closed = False
        self.train_crossing = False
        self.train_passed = False

        # ==========================================================
        # TRAIN
        # ==========================================================

        # Train starts very far from crossing
        self.train_x = -330

        self.train_speed = 3

        # ==========================================================
        # LOCATIONS
        # ==========================================================

        # Detection 1 is FAR before Gate 1
        self.detection1_x = 250

        # Gate positions
        self.gate1_x = 535
        self.gate2_x = 745

        # Detection 2 is after Gate 2
        self.detection2_x = 810

        # ==========================================================
        # COLORS
        # ==========================================================

        self.bg = "#101820"
        self.panel = "#18242F"
        self.panel2 = "#202F3B"

        self.text = "#EAF2F8"
        self.subtext = "#9FB3C8"

        self.green = "#27AE60"
        self.red = "#E74C3C"
        self.yellow = "#F1C40F"
        self.blue = "#3498DB"

        self.rail = "#BFC9CA"
        self.road = "#3B4147"

        # ==========================================================
        # HEADER
        # ==========================================================

        header = tk.Frame(
            root,
            bg="#16232D",
            height=70
        )
        header.pack(fill="x")

        tk.Label(
            header,
            text="SMART RAILWAY LEVEL CROSSING",
            font=("Segoe UI", 23, "bold"),
            fg=self.text,
            bg="#16232D"
        ).pack(
            side="left",
            padx=25,
            pady=14
        )

        self.header_status = tk.Label(
            header,
            text="● SYSTEM READY",
            font=("Segoe UI", 12, "bold"),
            fg=self.green,
            bg="#16232D"
        )
        self.header_status.pack(
            side="right",
            padx=25
        )

        # ==========================================================
        # MAIN
        # ==========================================================

        main = tk.Frame(
            root,
            bg=self.bg
        )

        main.pack(
            fill="both",
            expand=True,
            padx=18,
            pady=15
        )

        # ==========================================================
        # LEFT DASHBOARD
        # ==========================================================

        left = tk.Frame(
            main,
            bg=self.panel,
            width=870,
            height=500
        )

        left.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        left.pack_propagate(False)

        tk.Label(
            left,
            text="LIVE CROSSING SIMULATION",
            font=("Segoe UI", 14, "bold"),
            fg=self.text,
            bg=self.panel
        ).pack(
            anchor="w",
            padx=18,
            pady=(12, 5)
        )

        self.canvas = tk.Canvas(
            left,
            width=830,
            height=420,
            bg="#26343D",
            highlightthickness=0
        )

        self.canvas.pack(
            padx=15,
            pady=5
        )

        self.draw_environment()

        # ==========================================================
        # RIGHT MONITOR
        # ==========================================================

        right = tk.Frame(
            main,
            bg=self.panel,
            width=300
        )

        right.pack(
            side="right",
            fill="y"
        )

        right.pack_propagate(False)

        tk.Label(
            right,
            text="SYSTEM MONITOR",
            font=("Segoe UI", 14, "bold"),
            fg=self.text,
            bg=self.panel
        ).pack(
            anchor="w",
            padx=15,
            pady=(12, 10)
        )

        self.train_status = self.create_card(
            right,
            "TRAIN STATUS",
            "NO TRAIN",
            self.green
        )

        self.position_status = self.create_card(
            right,
            "TRAIN POSITION",
            "STANDBY",
            self.subtext
        )

        self.gate_status = self.create_card(
            right,
            "GATE STATUS",
            "OPEN",
            self.green
        )

        self.warning_status = self.create_card(
            right,
            "WARNING",
            "SAFE",
            self.green
        )

        self.buzzer_status = self.create_card(
            right,
            "BUZZER",
            "OFF",
            self.subtext
        )

        self.countdown_status = self.create_card(
            right,
            "DETECTION",
            "STANDBY",
            self.subtext
        )

        # ==========================================================
        # MESSAGE
        # ==========================================================

        tk.Label(
            right,
            text="SYSTEM MESSAGE",
            font=("Segoe UI", 10, "bold"),
            fg=self.subtext,
            bg=self.panel
        ).pack(
            anchor="w",
            padx=15,
            pady=(15, 3)
        )

        self.message_label = tk.Label(
            right,
            text="System ready. Waiting for train.",
            font=("Segoe UI", 10),
            fg=self.text,
            bg=self.panel2,
            anchor="w",
            justify="left",
            wraplength=260,
            height=4
        )

        self.message_label.pack(
            fill="x",
            padx=15
        )

        # ==========================================================
        # BUTTONS
        # ==========================================================

        button_frame = tk.Frame(
            right,
            bg=self.panel
        )

        button_frame.pack(
            fill="x",
            padx=15,
            pady=15
        )

        tk.Button(
            button_frame,
            text="▶ START TRAIN",
            command=self.start_train,
            font=("Segoe UI", 10, "bold"),
            bg="#2471A3",
            fg="white",
            activebackground="#2980B9",
            relief="flat",
            padx=8,
            pady=8,
            cursor="hand2"
        ).pack(
            fill="x",
            pady=3
        )

        tk.Button(
            button_frame,
            text="● SIMULATE DETECTION",
            command=self.trigger_detection1,
            font=("Segoe UI", 9, "bold"),
            bg="#7D6608",
            fg="white",
            activebackground="#9A7D0A",
            relief="flat",
            padx=8,
            pady=8,
            cursor="hand2"
        ).pack(
            fill="x",
            pady=3
        )

        tk.Button(
            button_frame,
            text="↻ RESET SYSTEM",
            command=self.reset_system,
            font=("Segoe UI", 9, "bold"),
            bg="#566573",
            fg="white",
            activebackground="#707B7C",
            relief="flat",
            padx=8,
            pady=8,
            cursor="hand2"
        ).pack(
            fill="x",
            pady=3
        )

        # ==========================================================
        # START ANIMATION
        # ==========================================================

        self.root.after(
            30,
            self.update_simulation
        )

    # ==============================================================
    # CARD
    # ==============================================================

    def create_card(
        self,
        parent,
        title,
        value,
        color
    ):

        frame = tk.Frame(
            parent,
            bg=self.panel2,
            height=58
        )

        frame.pack(
            fill="x",
            padx=15,
            pady=4
        )

        frame.pack_propagate(False)

        tk.Label(
            frame,
            text=title,
            font=("Segoe UI", 8, "bold"),
            fg=self.subtext,
            bg=self.panel2
        ).pack(
            anchor="w",
            padx=10,
            pady=(6, 0)
        )

        value_label = tk.Label(
            frame,
            text=value,
            font=("Segoe UI", 12, "bold"),
            fg=color,
            bg=self.panel2
        )

        value_label.pack(
            anchor="w",
            padx=10
        )

        return value_label

    # ==============================================================
    # ENVIRONMENT
    # ==============================================================

    def draw_environment(self):

        # Background
        self.canvas.create_rectangle(
            0,
            0,
            830,
            420,
            fill="#26343D",
            outline=""
        )

        # Grass
        self.canvas.create_rectangle(
            0,
            80,
            830,
            250,
            fill="#31443D",
            outline=""
        )

        # Road
        self.canvas.create_rectangle(
            0,
            180,
            830,
            320,
            fill=self.road,
            outline=""
        )

        # Road markings
        for x in range(0, 830, 80):

            self.canvas.create_rectangle(
                x,
                245,
                x + 45,
                250,
                fill="#D5D8DC",
                outline=""
            )

        # ==========================================================
        # RAILS
        # ==========================================================

        self.canvas.create_rectangle(
            0,
            200,
            830,
            206,
            fill=self.rail,
            outline=""
        )

        self.canvas.create_rectangle(
            0,
            290,
            830,
            296,
            fill=self.rail,
            outline=""
        )

        # Sleepers
        for x in range(0, 830, 35):

            self.canvas.create_rectangle(
                x,
                194,
                x + 12,
                302,
                fill="#795548",
                outline=""
            )

        # ==========================================================
        # CROSSING
        # ==========================================================

        self.canvas.create_rectangle(
            self.gate1_x,
            175,
            self.gate2_x,
            320,
            outline=self.yellow,
            width=2
        )

        self.canvas.create_text(
            (self.gate1_x + self.gate2_x) / 2,
            165,
            text="LEVEL CROSSING",
            fill=self.yellow,
            font=("Segoe UI", 10, "bold")
        )

        # ==========================================================
        # FIRST DETECTION
        # ==========================================================

        self.canvas.create_line(
            self.detection1_x,
            80,
            self.detection1_x,
            350,
            fill=self.yellow,
            width=2,
            dash=(8, 5)
        )

        self.canvas.create_text(
            self.detection1_x,
            65,
            text="DETECTION 1",
            fill=self.yellow,
            font=("Segoe UI", 9, "bold")
        )

        self.canvas.create_text(
            self.detection1_x,
            370,
            text="APPROACH",
            fill=self.yellow,
            font=("Segoe UI", 8)
        )

        # ==========================================================
        # SECOND DETECTION
        # ==========================================================

        self.canvas.create_line(
            self.detection2_x,
            80,
            self.detection2_x,
            350,
            fill=self.blue,
            width=2,
            dash=(8, 5)
        )

        self.canvas.create_text(
            self.detection2_x,
            65,
            text="DETECTION 2",
            fill=self.blue,
            font=("Segoe UI", 9, "bold")
        )

        self.canvas.create_text(
            self.detection2_x,
            370,
            text="EXIT",
            fill=self.blue,
            font=("Segoe UI", 8)
        )

        # ==========================================================
        # GATES
        # ==========================================================

        self.gate1_bar = self.canvas.create_line(
            self.gate1_x,
            360,
            self.gate1_x - 100,
            225,
            fill=self.green,
            width=10
        )

        self.gate2_bar = self.canvas.create_line(
            self.gate2_x,
            360,
            self.gate2_x - 100,
            225,
            fill=self.green,
            width=10
        )

        self.canvas.create_text(
            self.gate1_x,
            395,
            text="GATE 1",
            fill=self.text,
            font=("Segoe UI", 9, "bold")
        )

        self.canvas.create_text(
            self.gate2_x,
            395,
            text="GATE 2",
            fill=self.text,
            font=("Segoe UI", 9, "bold")
        )

        # ==========================================================
        # SIGNALS
        # ==========================================================

        self.signal1_red = self.canvas.create_oval(
            self.gate1_x - 30,
            100,
            self.gate1_x - 5,
            125,
            fill="#641E16",
            outline=""
        )

        self.signal1_green = self.canvas.create_oval(
            self.gate1_x + 5,
            100,
            self.gate1_x + 30,
            125,
            fill=self.green,
            outline=""
        )

        self.signal2_red = self.canvas.create_oval(
            self.gate2_x - 30,
            100,
            self.gate2_x - 5,
            125,
            fill="#641E16",
            outline=""
        )

        self.signal2_green = self.canvas.create_oval(
            self.gate2_x + 5,
            100,
            self.gate2_x + 30,
            125,
            fill=self.green,
            outline=""
        )

        # Train
        self.train_parts = []

        self.draw_train()

    # ==============================================================
    # TRAIN
    # ==============================================================

    def draw_train(self):

        for item in self.train_parts:

            self.canvas.delete(item)

        self.train_parts = []

        x = self.train_x
        y = 215

        # Locomotive
        self.train_parts.append(
            self.canvas.create_rectangle(
                x,
                y,
                x + 120,
                y + 60,
                fill="#34495E",
                outline="#ECF0F1",
                width=2
            )
        )

        # Front
        self.train_parts.append(
            self.canvas.create_polygon(
                x + 120,
                y,
                x + 145,
                y + 15,
                x + 145,
                y + 60,
                x + 120,
                y + 60,
                fill="#2C3E50",
                outline="#ECF0F1"
            )
        )

        # Coaches
        for i in range(2):

            coach_x = x + 145 + i * 75

            self.train_parts.append(
                self.canvas.create_rectangle(
                    coach_x,
                    y + 5,
                    coach_x + 70,
                    y + 60,
                    fill="#5D6D7E",
                    outline="#ECF0F1"
                )
            )

            for w in range(3):

                self.train_parts.append(
                    self.canvas.create_rectangle(
                        coach_x + 8 + w * 20,
                        y + 14,
                        coach_x + 20 + w * 20,
                        y + 30,
                        fill="#85C1E9",
                        outline=""
                    )
                )

        # Engine window
        self.train_parts.append(
            self.canvas.create_rectangle(
                x + 25,
                y + 12,
                x + 65,
                y + 30,
                fill="#85C1E9",
                outline=""
            )
        )

        # Headlight
        self.train_parts.append(
            self.canvas.create_oval(
                x + 132,
                y + 28,
                x + 142,
                y + 38,
                fill="#F7DC6F",
                outline=""
            )
        )

        # Label
        self.train_parts.append(
            self.canvas.create_text(
                x + 65,
                y + 43,
                text="EXPRESS",
                fill="white",
                font=("Segoe UI", 8, "bold")
            )
        )

        # Wheels
        for wheel_x in [
            x + 25,
            x + 85,
            x + 170,
            x + 235
        ]:

            self.train_parts.append(
                self.canvas.create_oval(
                    wheel_x,
                    y + 50,
                    wheel_x + 22,
                    y + 72,
                    fill="#17202A",
                    outline="#95A5A6"
                )
            )

    # ==============================================================
    # START TRAIN
    # ==============================================================

    def start_train(self):

        if self.running:

            return

        self.running = True

        # Start far away
        self.train_x = -330

        self.train_detected = False
        self.gates_closed = False
        self.train_crossing = False
        self.train_passed = False

        self.open_gates()

        self.train_status.config(
            text="APPROACHING",
            fg=self.yellow
        )

        self.position_status.config(
            text="FAR FROM CROSSING",
            fg=self.subtext
        )

        self.gate_status.config(
            text="OPEN",
            fg=self.green
        )

        self.warning_status.config(
            text="SAFE",
            fg=self.green
        )

        self.buzzer_status.config(
            text="OFF",
            fg=self.subtext
        )

        self.countdown_status.config(
            text="WAITING",
            fg=self.subtext
        )

        self.message_label.config(
            text="Train is approaching the crossing from a safe distance."
        )

        self.header_status.config(
            text="● TRAIN APPROACHING",
            fg=self.yellow
        )

    # ==============================================================
    # FIRST DETECTION
    # ==============================================================

    def trigger_detection1(self):

        if self.train_detected:

            return

        self.train_detected = True

        # ==========================================================
        # NO COUNTDOWN
        # IMMEDIATE GATE CLOSING
        # ==========================================================

        self.close_gates()

    # ==============================================================
    # CLOSE BOTH GATES IMMEDIATELY
    # ==============================================================

    def close_gates(self):

        self.gates_closed = True

        # Gate 1 immediately closes
        self.canvas.coords(
            self.gate1_bar,
            self.gate1_x,
            360,
            self.gate1_x,
            220
        )

        # Gate 2 immediately closes
        self.canvas.coords(
            self.gate2_bar,
            self.gate2_x,
            360,
            self.gate2_x,
            220
        )

        # Red signals ON
        self.canvas.itemconfig(
            self.signal1_red,
            fill=self.red
        )

        self.canvas.itemconfig(
            self.signal2_red,
            fill=self.red
        )

        # Green signals OFF
        self.canvas.itemconfig(
            self.signal1_green,
            fill="#145A32"
        )

        self.canvas.itemconfig(
            self.signal2_green,
            fill="#145A32"
        )

        self.train_status.config(
            text="TRAIN DETECTED",
            fg=self.yellow
        )

        self.position_status.config(
            text="DETECTION 1",
            fg=self.yellow
        )

        self.gate_status.config(
            text="CLOSED",
            fg=self.red
        )

        self.warning_status.config(
            text="STOP / CLOSED",
            fg=self.red
        )

        self.buzzer_status.config(
            text="ON",
            fg=self.red
        )

        self.countdown_status.config(
            text="DETECTED",
            fg=self.red
        )

        self.message_label.config(
            text="TRAIN DETECTED! Both gates closed immediately."
        )

        self.header_status.config(
            text="● GATES CLOSED",
            fg=self.red
        )

        # Buzzer automatically stops after short warning
        self.root.after(
            1000,
            self.stop_buzzer
        )

    # ==============================================================
    # BUZZER OFF
    # ==============================================================

    def stop_buzzer(self):

        self.buzzer_status.config(
            text="OFF",
            fg=self.subtext
        )

    # ==============================================================
    # SECOND DETECTION
    # ==============================================================

    def trigger_detection2(self):

        if not self.gates_closed:

            return

        if self.train_passed:

            return

        self.train_passed = True

        self.train_crossing = False

        self.message_label.config(
            text="TRAIN PASSED DETECTION 2. Crossing is clear."
        )

        self.train_status.config(
            text="TRAIN PASSED",
            fg=self.green
        )

        self.position_status.config(
            text="CLEAR",
            fg=self.green
        )

        # Open gates
        self.open_gates()

    # ==============================================================
    # OPEN BOTH GATES
    # ==============================================================

    def open_gates(self):

        self.gates_closed = False

        # Gate 1 open
        self.canvas.coords(
            self.gate1_bar,
            self.gate1_x,
            360,
            self.gate1_x - 100,
            225
        )

        # Gate 2 open
        self.canvas.coords(
            self.gate2_bar,
            self.gate2_x,
            360,
            self.gate2_x - 100,
            225
        )

        # Red OFF
        self.canvas.itemconfig(
            self.signal1_red,
            fill="#641E16"
        )

        self.canvas.itemconfig(
            self.signal2_red,
            fill="#641E16"
        )

        # Green ON
        self.canvas.itemconfig(
            self.signal1_green,
            fill=self.green
        )

        self.canvas.itemconfig(
            self.signal2_green,
            fill=self.green
        )

        self.gate_status.config(
            text="OPEN",
            fg=self.green
        )

        self.warning_status.config(
            text="SAFE",
            fg=self.green
        )

        self.buzzer_status.config(
            text="OFF",
            fg=self.subtext
        )

        self.countdown_status.config(
            text="CLEAR",
            fg=self.green
        )

        self.header_status.config(
            text="● SYSTEM SAFE",
            fg=self.green
        )

    # ==============================================================
    # MAIN SIMULATION
    # ==============================================================

    def update_simulation(self):

        if self.running:

            # Train continuously moves
            self.train_x += self.train_speed

            # ======================================================
            # DETECTION 1
            # ======================================================

            train_front = self.train_x + 145

            if (
                train_front >= self.detection1_x
                and not self.train_detected
            ):

                self.trigger_detection1()

            # ======================================================
            # TRAIN ENTERS CROSSING
            # ======================================================

            if (
                self.gates_closed
                and not self.train_crossing
                and train_front >= self.gate1_x
            ):

                self.train_crossing = True

                self.train_status.config(
                    text="TRAIN CROSSING",
                    fg=self.yellow
                )

                self.position_status.config(
                    text="GATE 1 → GATE 2",
                    fg=self.yellow
                )

                self.message_label.config(
                    text="Train is crossing. Both gates remain closed."
                )

                self.header_status.config(
                    text="● TRAIN CROSSING",
                    fg=self.yellow
                )

            # ======================================================
            # DETECTION 2
            # ======================================================

            # train_x represents the rear of the train.
            # Therefore Detection 2 is triggered only after
            # the COMPLETE train has passed Gate 2.

            train_rear = self.train_x

            if (
                self.gates_closed
                and self.train_crossing
                and train_rear >= self.detection2_x
                and not self.train_passed
            ):

                self.trigger_detection2()

            # ======================================================
            # TRAIN LEAVES SCREEN
            # ======================================================

            if self.train_x > 900:

                self.running = False

        # Redraw train
        self.draw_train()

        # Continue animation
        self.root.after(
            30,
            self.update_simulation
        )

    # ==============================================================
    # RESET
    # ==============================================================

    def reset_system(self):

        self.running = False

        self.train_detected = False
        self.gates_closed = False
        self.train_crossing = False
        self.train_passed = False

        self.train_x = -330

        self.open_gates()

        self.train_status.config(
            text="NO TRAIN",
            fg=self.green
        )

        self.position_status.config(
            text="STANDBY",
            fg=self.subtext
        )

        self.gate_status.config(
            text="OPEN",
            fg=self.green
        )

        self.warning_status.config(
            text="SAFE",
            fg=self.green
        )

        self.buzzer_status.config(
            text="OFF",
            fg=self.subtext
        )

        self.countdown_status.config(
            text="WAITING",
            fg=self.subtext
        )

        self.message_label.config(
            text="System reset. Waiting for train."
        )

        self.header_status.config(
            text="● SYSTEM READY",
            fg=self.green
        )

        self.draw_train()


# ==============================================================
# RUN
# ==============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = RailwayDashboard(root)

    root.mainloop()