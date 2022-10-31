public class Evento {
    private String nome; 
    private double chegada;
    private double saida;
    private double tempo;

    public Evento(String nome, double chegada, double saida, double tempo){
        this.nome = nome;
        this.chegada = chegada;
        this.saida = saida;
        this.tempo = tempo;
    }
    public String getNome(){
        return this.nome;
    }
    public double getChegada(){
        return this.chegada;
    }
    public double getSaida(){
        return this.saida;
    }
    public double getTempo(){
        return this.tempo;
    }
    public void setTempo(double tempo){
        this.tempo = tempo;
    }
    
}
