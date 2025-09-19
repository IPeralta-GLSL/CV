from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_fill_color(245, 247, 250)  # Fondo muy claro
        self.rect(0, 0, 210, 297, 'F')

        self.set_font("Arial", "B", 14)
        self.set_text_color(44, 62, 80)  # Azul grisáceo oscuro
        self.set_fill_color(100, 149, 237)  # Azul suave para el título
        self.cell(0, 10, "Curriculum Vitae", 0, 1, "C", 1)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 14)
        self.set_fill_color(230, 236, 240)  # Gris azulado claro
        self.set_text_color(52, 73, 94)  # Gris oscuro
        self.cell(0, 10, title, 0, 1, "L", 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font("Arial", "", 10)
        self.set_text_color(44, 62, 80)  # Azul grisáceo oscuro
        self.multi_cell(0, 6, body)
        self.ln()

pdf = PDF()

# Personal Information
pdf.add_page()

# Add profile image
pdf.image("photo_2024-08-01_23-15-53.jpg", x=170, y=30, w=30)

pdf.chapter_title("Personal Information")
pdf.chapter_body("Name: Ignacio Peralta\nProfession: Software Programmer\nEmail: peraltaignacio64@gmail.com\nPhone: +54 1130613117")

# About Me
pdf.chapter_title("About Me")
pdf.chapter_body("I'm a software developer from Argentina with a strong passion for programming, particularly in the realm of graphics development. Over the course of my career, I've embarked on diverse projects, ranging from video games and mobile apps to bots, websites, and various development tools. My expertise in graphics programming includes working with technologies like Vulkan and DirectX, as well as advanced techniques in rendering, VFX, shader programming, offline and real-time graphics optimization.\n\nI have a solid foundation in transforming innovative ideas into tangible and functional visual experiences. My experience spans various aspects of graphics development, including offline and real-time rendering, image processing, and graphics engine design.\n\nCollaboration and teamwork are values I hold dear, and I thrive in dynamic, agile environments. My adaptability to change and commitment to delivering results make me a valuable asset to any project or team, especially those focused on cutting-edge graphics technologies and innovative visual solutions.")

# Skills, Languages, Frameworks, APIs, and Platforms
pdf.set_fill_color(40, 44, 52)

#pdf.chapter_title("Skills")
#pdf.chapter_body("- Multiplayer - Optimization - Cynamatics - Tools For Develop")

pdf.chapter_title("Languages, Technologies, and Frameworks")
pdf.chapter_body("- C - C++ - C# - Rust - Python - Lua - Javascript - GLSL\n- OpenGL - OpenCL - CUDA - Assimp - Numpy - TensorFlow - PyTorch - OpenCV - FFmpeg\n- Unreal Engine - Godot Engine - Open 3D Engine - Unity Engine - Qt framework - .Net - Android Studio")

#pdf.chapter_body("- Unreal Engine - Godot Engine - Open 3D Engine - Unity Engine - Qt framework - .Net - Android Studio")

pdf.chapter_title("APIs")
pdf.chapter_body("- Steam - Discord - Epic Online Service - Twitch - Google Play Service - Xsolla")

pdf.chapter_title("Operating Systems")
pdf.chapter_body("- Rocky Linux (RHEL-based) - Arch - Fedora - Ubuntu Server - Debian - FreeBSD")

# Experience
pdf.chapter_title("Experience")
pdf.chapter_body("- GC-Properties S.A (november 2024 - Currently)\n - Grupo Change (February 2024 - september 2024)\n- TV Publica (February 2023 - February 2024)\n- Studio Soup (September 2022 - March 2023)\n- Teachlabs (August 2022 - September 2022)\n- Vulcano (March 2022 - May 2022)\n- Lilouli Business Solutions (December 2021 - March 2022)\n- Joy Games Interactive (December 2021 - March 2023)\n- Nota Al Pie (August 2020 - December 2021)\n- Bullet Time Games (January 2020 - August 2021)")

# Some of My Projects
pdf.chapter_title("Some of My Projects")
pdf.chapter_body("- Between us (Frantic action shooter Cyberpunk game in first and third person)\n- Bullet Time Launcher (Launcher and store for Games of Bullet Time)\n- Unreal Boost Compile (Tool For Unreal engine to improve the speed fo shader and lighting compilation)\n- Flag Pit (Multiplayer Deathmatch Melee game)\n- Vulcano (NFT Multiplayer game made with Unreal Engine 5)\n\nTo see all my works: https://www.ignacioperalta.com/")

pdf.output("Ignacio_Peralta_CV.pdf")