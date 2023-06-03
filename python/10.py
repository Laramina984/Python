class aluno:   
    def int (self, matricula, nome, nota1, nota2, traba):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.traba = traba

    def media (self):
        media_prov = (self.nota1 + self.nota2)/2
        media_final = (media_prov * 2.5 + self.traba * 2) / 5
        return media_final
    
    def final(self):
      media_final = self.media()
      if media_final <7:
          nota_final = 10 - media_final
          return
      else:
          return 0





   