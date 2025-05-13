

# **Using Frames as Pages in a Tkinter App**

### Goal

Learn how to use `Frame` widgets in Tkinter to create multiple "pages" or "windows" in your app, and how to switch between them using `tkraise()`.



##  What is a `Frame`?

A `Frame` is a **container**—like an invisible box—that holds widgets such as buttons, labels, and text inputs. You can think of each frame as a **separate screen** in your app.

**Each screen (page) in your app = one frame.**

Instead of opening new windows, you **swap which frame is visible**.



## Placing Widgets on the Right Frame

When you create a widget, you must **tell Python which frame to put it on**.
If you don’t specify the frame, the widget will go on the root window by default, which will cause layout problems.

**Correct:**

```python
Label(landing_frame, text="Landing Page")
```

**Incorrect:**

```python
Label(text="Landing Page")  # This goes on the root, not a frame!
```

**Always include the frame name as the first argument** when creating widgets for that frame.

## How Frames Work Behind the Scenes

When you use multiple frames to build an app:

* All frames are created and placed **in the same position** (e.g., `x=0, y=0`).
* Think of them like **sheets of paper stacked on top of each other**.
* Only the **top sheet (frame)** is visible.
* You can show a different frame by calling `.tkraise()`.



## How `tkraise()` Works

The `.tkraise()` method **raises a frame to the top of the stacking order**, making it the visible one.

### Visual Explanation:

```
Stack of Frames (bottom to top):
[landing_frame]
[red_frame]
[blue_frame]  ← this is visible if tkraise(blue_frame) was called
```

Calling:

```python
red_frame.tkraise()
```

moves `red_frame` to the **top of the stack**, so now **red\_frame is visible**.


