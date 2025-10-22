import tkinter as tk
from PIL import Image, ImageTk

class KhabyLameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Khaby Lame Mechanism")
        self.root.geometry("400x400")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        # Create the original character elements (body, neck, arms, etc.)
        # Thicker stick for the body
        self.body = self.canvas.create_line(200, 175, 200, 300, width=20, fill="blue")

        # Thinner stick for the neck
        self.neck = self.canvas.create_line(200, 175, 200, 150, width=5, fill="black")

        # Head on top of the neck
        self.head = self.canvas.create_oval(175, 100, 225, 150, fill="lightyellow")

        # Arms from a 3/4 angle - keep the original lines as placeholders
        self.left_arm = self.canvas.create_line(200, 225, 125, 225, width=10)
        self.right_arm = self.canvas.create_line(200, 225, 275, 225, width=10)

        # Load images using PIL
        try:
            # Load head image and resize it
            self.head_image = Image.open("khabylamehead.png")  # Using your existing image
            self.head_image = self.head_image.resize((55, 200))  # Make it bigger
            self.head_photo = ImageTk.PhotoImage(self.head_image)
            
            # Create head image item at the head center
            self.head_image_item = self.canvas.create_image(200, 200, image=self.head_photo)
            
            # Load left arm image
            self.left_arm_image = Image.open("khabylamearm.png")  # Using your arm image
            self.left_arm_image = self.left_arm_image.resize((80, 40))  # Make it bigger
            self.left_arm_photo = ImageTk.PhotoImage(self.left_arm_image)
            
            # Create left arm image item at the left arm position
            # Position the left arm image at the start of the arm (125, 225)
            self.left_arm_image_item = self.canvas.create_image(125, 225, image=self.left_arm_photo)
            
            # Load right arm image
            self.right_arm_image = Image.open("khabylamearm.png")  # Using the same arm image
            self.right_arm_image = self.right_arm_image.resize((80, 40))  # Make it bigger
            self.right_arm_photo = ImageTk.PhotoImage(self.right_arm_image)
            
            # Create right arm image item at the right arm position
            # Position the right arm image at the start of the arm (275, 225)
            self.right_arm_image_item = self.canvas.create_image(275, 225, image=self.right_arm_photo)
            
            # Bind mouse motion to move arms and keep images in place
            self.canvas.bind("<Motion>", self.move_arms)
            
        except Exception as e:
            # Fallback if image can't be loaded
            print(f"Could not load images: {e}")
            print("Keeping original drawing.")
            self.canvas.bind("<Motion>", self.move_arms)

    def move_arms(self, event):
        # Get current position of head center
        head_center_y = 125
        head_center_x = 200
        
        # Calculate mouse position relative to head center
        mouse_y = event.y
        mouse_x = event.x

        # Shrugging motion with a 3/4 perspective
        # Left arm motion
        new_left_y = 225 + (mouse_y - head_center_y) / 5
        new_left_x = 125 + (mouse_x - head_center_x) / 10

        # Right arm motion
        new_right_y = 225 + (mouse_y - head_center_y) / 5
        new_right_x = 275 - (mouse_x - head_center_x) / 10

        # Clamp the arm movement
        new_left_y = max(175, min(275, new_left_y))
        new_left_x = max(100, min(150, new_left_x))
        new_right_y = max(175, min(275, new_right_y))
        new_right_x = max(250, min(300, new_right_x))

        # Update arm positions
        self.canvas.coords(self.left_arm, 200, 225, new_left_x, new_left_y)
        self.canvas.coords(self.right_arm, 200, 225, new_right_x, new_right_y)
        
        # Update image positions for the arms - keep the images attached to the arm ends
        self.canvas.coords(self.left_arm_image_item, new_left_x, new_left_y)
        self.canvas.coords(self.right_arm_image_item, new_right_x, new_right_y)

if __name__ == "__main__":
    root = tk.Tk()
    app = KhabyLameApp(root)
    root.mainloop()