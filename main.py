from mock.utils import GetRandomChoice
from form_launcher.form_launch import GFormFiller


def main():
    print("Running your Python program...")

    gformFiller = GFormFiller(
        fname="answers",
        url="https://forms.gle/gJRy5t3M2EzJWwp59",
    )

    
    gformFiller.run()

    pass


if __name__ == "__main__":
    main()
