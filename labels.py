from collections import defaultdict

folder_labelmap = {'01-01_Identifikation' : ['allgemein', 'identifikation'],
                   '02-01_Technische Spezifikation' : ['technische spezifikation'],
                   '02-02_Zeichnungen  Pl\udce4ne' : ['bauteile','technische zeichnung', 'zeichnung', 'abbildung'],
                   '02-03_Bauteile' : ['bauteil', 'komponente'],
                   '02-04_Zeugnisse, Zertifikate, Bescheinigungen': ['zeugnisse', 'zertifikate', 'bescheinigungen'],
                   '03-01_Montage, Demontage' : ['montage', 'demontage'], 
                   '03-02_Bedienung' : ['bedienungsanleitung', 'manual', 'lastenheft'],
                   '03-03_Allgemeine Sicherheit' : ['sicherheit'],
                   '03-04_Inspektion, Wartung, Pr\udcfcfung' : ['inspektion', 'wartung', 'pruefung', 'prüfung'],
                   '03-06_Ersatzteile' : ['teile', 'ersatzteile', 'komponenten', 'bauteil'], 
                   '10. Anhang' : ['allgemein'],
                   '10.2 Ersatzteile & \udcdcbersichtszeichnungen' : ['teile', 'ersatzteile', 'komponenten', 'bauteil', 'technische zeichnung', 'zeichnung', 'abbildung'],
                   '10.5 Dokumentation der Zulieferer' : ['dokumentation', 'zulieferer'],
                   '5. Zeichnungen' : ['zeichnung', 'abbildung'],
                   '8. Quality Manual' : ['qualität', 'bedienungsanleitung'],
                   'Bedienungsanleitung Mischsilo' : ['bedienungsanleitung', 'mischsilo'], 
                   'Betreiberinformationen' : ['betreiberinformationen'],
                   'Montageanleitung': ['montage', 'demontage', 'bedienungsanleitung'],
                   'nicht einsortieren' : ['allgemein'],
                   'unklar' : ['allgemein']
                  }


def get_filelabels(file_dirs):
    '''
    :param data: list of strings
    :return: set of all used labels, dict of set with labels for each file
    '''
    files2labels = defaultdict(set)
    labels2files = defaultdict(set)
    all_labels = set()              
    for i, path in enumerate(file_dirs):
        folder = path.split('/')[-2]
        all_labels.update(set(folder_labelmap[folder]))
        files2labels[i].update(set(folder_labelmap[folder]))
        
        for label in files2labels[i]:
            labels2files[label].add(i)
        
    
    return all_labels, files2labels, labels2files


def get_query2labels(query, all_labels):
    '''
    
    '''
    query2labels = defaultdict(set)
    for q in query:
        for label in all_labels:
            if q in label: query2labels[q].add(label)
                
    return query2labels
    
