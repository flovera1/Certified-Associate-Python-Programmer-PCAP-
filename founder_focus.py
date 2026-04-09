class FounderFocus:

    def __init__(self, name):
        self.name = name
        self.sector = None
        self.funding = 0

    def set_sector(self, sector):
        self.sector = sector

    def set_funding(self, funding):
        self.funding = funding

    def is_acquisition_ready(self):
        return (
            self.funding >= 500000 and
            self.sector in ["AI", "Fintech", "SaaS"]

        )
    
    def summary(self):
        return (
            f"Startup Name: {self.name}\n"
            f"Sector: {self.sector}\n"
            f"Funding: {self.funding}\n"
            f"Acquisition Ready: {self.is_acquisition_ready()}"
        )
    
    def export_summary_to_txt(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.summary())

        print(f"Exported summary to {filename}")

        