class OpeningManim(Scene):
    def construct(self):
        title = Tex(r"Dobrý den")
        title.arrange(DOWN)
        self.play(Write(title))
        self.wait()

        title2 = Tex("Chcete vidět hezké kouzlo?")
        self.play(
            Transform(title, title2),
        )
        self.wait()
        
        title3 = Tex("Opravdu?")
        title3.move_to(DOWN)
        self.play(
            Transform(title2, title3),
        )
        self.wait()
        
        title4 = Tex("No tak jo :)")
        title4.to_corner(UP)
        self.play(
            Write(title4),
            FadeOut(title),
            FadeOut(title2),
        )
        
        self.wait()
        
        #Původně jsem chtěl získat IP, výchozí prohlížeč, atd z počítače, ale lenost zvítězila
        
        sub1 = Tex("IP: 45.168.95.124")
        
        sub2 = Tex("Agent: AppleWebKit/537.36 KHTML, like Gecko")
        sub2.next_to(sub1, DOWN, buff=0.1)
        
        sub3 = Tex("Browser: Asi Safari")
        sub3.next_to(sub2, DOWN, buff=0.1)
        
        sub4 = Tex("OS: MacOS X Sonoma")
        sub4.next_to(sub3, DOWN, buff=0.1)
        
        sub5 = Tex("Foo: Bar")
        sub5.next_to(sub4, DOWN, buff=0.1)
        
        self.play(
            Write(sub1),
        )
        self.play(
            Write(sub2),
        )
        self.play(
            Write(sub3),
        )
        self.play(
            Write(sub4),
        )
        self.play(
            Write(sub5),
        )
        
        another_title = Tex("Jo a taky jsem našel tohle na wiki")
        another_title.to_corner(UP)
        self.play(
            FadeOut(sub1),
            FadeOut(sub2),
            FadeOut(sub3),
            FadeOut(sub4),
            FadeOut(sub5),
            FadeOut(title4),
            Transform(title4, another_title),
        )
        
        self.play(
            FadeOut(title4)
        )
        
        code = '''import Muhahahaha, tu, by, mel, byt, kod
        
        import ovsem as tohle
        
        mi(): 
            prislo = mnohem
            vtipnejsi()
            
        vtipnejsi():
            for snad in range(tohle):
                staci[diky] = [<3 + 1]
                
        mi()
        '''
        code_show = Code(code=code, tab_width=6, background="window",
                            language="Python", font="Z003")
        
        self.play(
            Write(code_show),
        )
        
        self.wait(5)
