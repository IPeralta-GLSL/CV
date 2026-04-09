from fpdf import FPDF, XPos, YPos

class PDF(FPDF):
    def header(self):
        self.set_fill_color(240, 248, 239)  # Fondo verde muy claro
        self.rect(0, 0, 210, 297, 'F')

        self.set_font("Helvetica", "B", 16)
        self.set_text_color(255, 255, 255)  # Blanco sobre verde
        self.set_fill_color(45, 87, 44)  # Verde oscuro para el título

        margin = 80
        self.set_x(margin)
        self.cell(210 - margin * 2, 12, "Curriculum Vitae", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C", fill=True)
        self.ln(6)

    def chapter_title(self, title):
        # Jump to next page if we're near the bottom
        if self.get_y() > self.h - self.b_margin - 20:
            self.add_page()
        self.set_font("Helvetica", "B", 14)
        self.set_fill_color(45, 87, 44)  # Verde oscuro principal
        self.set_text_color(255, 255, 255)  # Blanco para contraste
        self.cell(0, 10, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L", fill=True)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(50, 60, 50)  # Gris oscuro verdoso, legible
        self.multi_cell(0, 6, body)
        self.ln()

    def info_row(self, label, value, reserved_right=0):
        self.set_x(self.l_margin)  # siempre empezar desde el margen izquierdo
        self.set_text_color(50, 60, 50)
        label_w = 48
        value_w = self.w - self.l_margin - self.r_margin - label_w - reserved_right
        self.set_font("Helvetica", "B", 10)
        self.cell(label_w, 6, label)
        self.set_font("Helvetica", "", 10)
        self.multi_cell(value_w, 6, value)

pdf = PDF()

# Personal Information
pdf.add_page()

# profile image: x=168 → flush al margen derecho (168+32=200=210-10)
# reserved_right=37 → texto termina en x=163, gap de 5mm antes de la foto
pdf.image("photo_2024-08-01_23-15-53.jpg", x=168, y=48, w=32)

pdf.chapter_title("Personal Information")
pdf.info_row("Name: ", "Ignacio Peralta", reserved_right=37)
pdf.info_row("Profession: ", "Software Programmer", reserved_right=37)
pdf.info_row("Email: ", "peraltaignacio64@gmail.com", reserved_right=37)
pdf.info_row("Phone: ", "+54 1130613117", reserved_right=37)
pdf.info_row("LinkedIn: ", "https://www.linkedin.com/in/ignacio-peralta-768396174/", reserved_right=37)
pdf.info_row("Website: ", "https://www.ignacioperalta.com/", reserved_right=37)
pdf.info_row("Currently studying: ", "Técnico Superior en Programación at Teclab", reserved_right=37)
pdf.ln(4)

# About Me
pdf.chapter_title("About Me")
pdf.chapter_body("I'm a software developer from Argentina with a strong passion for programming, particularly in the realm of graphics development. Over the course of my career, I've embarked on diverse projects, ranging from video games and mobile apps to bots, websites, and various development tools. My expertise in graphics programming includes working with technologies like Vulkan and DirectX, as well as advanced techniques in rendering, VFX, shader programming, offline and real-time graphics optimization.\n\nI have a solid foundation in transforming innovative ideas into tangible and functional visual experiences. My experience spans various aspects of graphics development, including offline and real-time rendering, image processing, and graphics engine design.\n\nCollaboration and teamwork are values I hold dear, and I thrive in dynamic, agile environments. My adaptability to change and commitment to delivering results make me a valuable asset to any project or team, especially those focused on cutting-edge graphics technologies and innovative visual solutions.")

# Skills, Languages, Frameworks, APIs, and Platforms
pdf.set_fill_color(45, 87, 44)

#pdf.chapter_title("Skills")
#pdf.chapter_body("- Multiplayer - Optimization - Cynamatics - Tools For Develop")

pdf.chapter_title("Languages, Technologies, and Frameworks")
pdf.chapter_body("- C - C++ - C# - Rust - Python - Lua - Javascript - GLSL\n- OpenGL - Vulkan - DirectX 12 - OpenCL - CUDA - Assimp - Numpy - TensorFlow - PyTorch - OpenCV - FFmpeg\n- Unreal Engine - Godot Engine - Open 3D Engine - Unity Engine - Qt framework - .Net - Android Studio")

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
pdf.chapter_body("- Between us (Frantic action shooter Cyberpunk game in first and third person)\n- Bullet Time Launcher (Launcher and store for Games of Bullet Time)\n- Unreal Boost Compile (Tool For Unreal engine to improve the speed fo shader and lighting compilation)\n- Flag Pit (Multiplayer Deathmatch Melee game)\n- Vulcano (NFT Multiplayer game made with Unreal Engine 5)")

pdf.output("Ignacio_Peralta_CV.pdf")
