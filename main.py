from mock.utils import GetRandomChoice
from form_launcher.form_launch import GFormFiller


def main():
    print("Running your Python program...")

    gformFiller = GFormFiller(
        fname="answers",
        url="https://docs.google.com/forms/d/e/1FAIpQLSdqDjQIbbXUmL7_bPZBey4ovo50VxFcvYYNkxSEZcR09Ety2g/viewform?usp=sf_link",
    )

    
    gformFiller.run()

    pass


if __name__ == "__main__":
    main()
