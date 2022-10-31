/*
 * Elias Matos e Morgana Weber
 * 
 * O código está incompleto. Pegamos a primeira versão que era em Python e também 
 * não estava correta e trouxemos para Java. 
 * Foi tentado reproduzir o pseudocódigo passado em aula. Gostaríamos de saber se 
 * o que temos até agora faz sentido para dar segmento e entregar a versão final completa. 
 * 
 */



public class Main {
    public static int capacidadeFila1 = 3; 
    public static int servidoresFila1 = 2; 
    public static int capacidadeFila2 = 3;
    public static int servidoresFila2 = 1;
    public static int countFila1  = 0;
    public static int countFila2 = 0;
    public static Evento[] fila1 = new Evento[0];
    public static Evento[] fila2 = new Evento[0];
    public static void main (String[] args){
        double[] aleatorios = {0.9921,0.0004,0.5534,0.2761,0.3398,0.8963,0.9023,0.0132,0.4569,0.5121,0.9208,0.0171,0.2299,0.8545,0.6001,0.2921};
        
        double chegada = 2.5;
        double tempo = 0;
        int inicioChegadaFila1 = 2;
        int fimChegadaFila1 = 3;
        int inicioAtendimentoFila1 = 2;
        int fimAtendimentoFila1 = 5; 
        int inicioAtendimentoFila2 = 3; 
        int fimAtendimentoFila2 = 5;
        int nEventos = 0;
        int aux = 0;
        int countEventos = 1;
        int perda = 0;
        String auxNome = "";

        //Realiza a primeira chegada 
        double proximaChegada = chegada + tempo;
        double saida  = (fimAtendimentoFila1 - inicioAtendimentoFila1) * (aleatorios[aux]) + inicioAtendimentoFila1;
        if(fila1.length < capacidadeFila1){
            aux++;
            auxNome = "(" +countEventos + ") chegada";
            Evento e = new Evento(auxNome, chegada, saida, tempo);
            fila1 = adicionaFila(fila1, e);

            System.out.println("Evento: " + e.getNome() + 
            "\ntempo para chegar: " + chegada + 
            "\nCHEGADA no minuto: " + proximaChegada +
            "\n -----");
            
            if(fila1.length <= servidoresFila1){
                agendaProcesso();
            }
            countEventos++;
        }
        else{
            perda++;
        } 

        while(aux < aleatorios.length){
            chegada = (fimChegadaFila1 - inicioAtendimentoFila1) * (aleatorios[aux]) + inicioChegadaFila1;
            countFila1++;
            if(fila1.length < capacidadeFila1){
                aux++;
                auxNome = "(" + countEventos + ") chegada";
                Evento e = new Evento(auxNome, chegada, saida, tempo);
                fila1 = adicionaFila(fila1, e);

                System.out.println("Evento: " + e.getNome() + 
                "\ntempo para chegar: " + chegada + 
                "\nCHEGADA no minuto: " + proximaChegada +
                "\n -----");

                if(fila1.length <= servidoresFila1){
                    agendaProcesso();
                }
            }else{
                perda++;
            }
        }  
    }

    public static Evento[] adicionaFila(Evento[] fila, Evento evento){
        Evento[] filaAtualiza = new Evento[fila.length + 1];
        for(int x = 0; x < fila.length; x++){
            filaAtualiza[x] = fila[x];
        }
        filaAtualiza[fila.length] = evento;
        return filaAtualiza;
    }

    public static void agendaSaida2(){
        //contabiliza tempos (FILA1, FILA2)
        countFila2--;
        if(fila2.length >= servidoresFila2){
            agendaSaida2();
        }
    }

    public static void agendaProcesso(){
        if(fila1.length >= servidoresFila1){
            agendaProcesso();
        }
        if(fila2.length < capacidadeFila2){
            countFila2++;
            if(fila2.length <= servidoresFila2){
                if(fila2.length <= servidoresFila2){
                    agendaSaida2();
                }                
            }
        }   
    }
}
