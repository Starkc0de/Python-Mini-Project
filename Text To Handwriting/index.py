import pywhatkit as pw

txt = """ron Man is a fictional superhero who wears a suit of armor. His alter ego is Tony Stark. He was created by Stan Lee, Jack Kirby and Larry Lieber for Marvel Comics in Tales of Suspense #39 in the year 1963 and appears in their comic books. He is also one of the main protagonists in the Marvel Cinematic Universe."""

pw.text_to_handwriting(txt,"demo.jpg",[0,0,138])
print("end")