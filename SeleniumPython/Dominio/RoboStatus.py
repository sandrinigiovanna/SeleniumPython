class RoboStatus:
    def __init__(self, nome_robo=None, nome_robo_intranet=None, status=None, problema=None):
        self.nome_robo = nome_robo
        self.nome_robo_intranet = nome_robo_intranet
        self.status = status
        self.problema = problema

    def __repr__(self):
        return (f"RoboStatus(nome_robo={self.nome_robo}, "
                f"nome_robo_intranet={self.nome_robo_intranet}, "
                f"status={self.status}, "
                f"problema={self.problema})")
