from datetime import datetime, timedelta
from typing import Dict, List, Optional

class CourseInfoTool:
    def __init__(self):
        # Database dei moduli di addestramento spaziale
        self.courses = {
            "pilotaggio_navette": {
                "name": "Pilotaggio di Navette Interstellari",
                "description": "Corso pratico di manovra e atterraggio in assenza di gravità",
                "duration": "4 settimane",
                "price": "350 Crediti Galattici"
            },
            "astronavigazione": {
                "name": "Astronavigazione Quantistica",
                "description": "Calcolo delle rotte a curvatura e orientamento stellare",
                "duration": "6 settimane",
                "price": "450 Crediti Galattici"
            },
            "ingegneria_motori": {
                "name": "Ingegneria dei Motori a Curvatura",
                    "description": "Manutenzione e riparazione dei nuclei a plasma e propulsori",
                "duration": "5 settimane",
                "price": "400 Crediti Galattici"
            },
            "diplomazia_galattica": {
                "name": "Protocolli di Diplomazia e Primo Contatto",
                "description": "Studio delle leggi della Federazione e gestione delle specie aliene",
                "duration": "3 settimane",
                "price": "300 Crediti Galattici"
            }
        }

    def get_info(self, course_name: str) -> str:
        query = course_name.lower().strip()
        key = query.replace(" ", "_")
        course = self.courses.get(key)
        
        if not course:
            for k, v in self.courses.items():
                if query in k or query in v["name"].lower() or v["name"].lower() in query:
                    course = v
                    break

        if not course:
            disponibili = ", ".join([v['name'] for v in self.values()]) if hasattr(self, 'values') else ", ".join([v['name'] for v in self.courses.values()])
            return f"Modulo '{course_name}' non trovato nei registri dell'Accademia. Moduli disponibili: {disponibili}"

        return (f"Modulo: {course['name']}\n"
                f"Descrizione: {course['description']}\n"
                f"Durata: {course['duration']}\n"
                f"Costo: {course['price']}")

class ScheduleTool:
    def __init__(self):
        oggi = datetime.today()
        d1 = (oggi + timedelta(days=5)).strftime("%Y-%m-%d")
        d2 = (oggi + timedelta(days=15)).strftime("%Y-%m-%d")
        d3 = (oggi + timedelta(days=20)).strftime("%Y-%m-%d")
        d4 = (oggi + timedelta(days=30)).strftime("%Y-%m-%d")

        self.classes = [
            {"course_name": "Pilotaggio di Navette Interstellari", "start_date": d1, "end_date": (oggi + timedelta(days=33)).strftime("%Y-%m-%d"), "spots_available": 12},
            {"course_name": "Astronavigazione Quantistica", "start_date": d2, "end_date": (oggi + timedelta(days=57)).strftime("%Y-%m-%d"), "spots_available": 8},
            {"course_name": "Ingegneria dei Motori a Curvatura", "start_date": d3, "end_date": (oggi + timedelta(days=55)).strftime("%Y-%m-%d"), "spots_available": 10},
            {"course_name": "Protocolli di Diplomazia e Primo Contatto", "start_date": d4, "end_date": (oggi + timedelta(days=45)).strftime("%Y-%m-%d"), "spots_available": 15}
        ]

    def get_classes(self, course_name: Optional[str] = None, start_date: Optional[str] = None) -> str:
        filtered_classes = self.classes
        if course_name:
            filtered_classes = [c for c in filtered_classes if course_name.lower() in c["course_name"].lower()]
        if start_date:
            filtered_classes = [c for c in filtered_classes if c["start_date"] >= start_date]

        if not filtered_classes:
            return f"Nessuna sessione di addestramento trovata per i criteri specificati."

        result = "Prossime sessioni di addestramento in partenza:\n"
        for c in filtered_classes:
            result += f"- {c['course_name']}: dal {c['start_date']} al {c['end_date']} (Posti liberi: {c['spots_available']})\n"
        return result


class BookingTool:
    def __init__(self):
        oggi = datetime.today()
        slot1 = (oggi + timedelta(days=7)).strftime("%Y-%m-%d")
        slot2 = (oggi + timedelta(days=10)).strftime("%Y-%m-%d")
        slot3 = (oggi + timedelta(days=12)).strftime("%Y-%m-%d")

        self.available_slots = [
            {"teacher_id": "T001", "teacher_name": "Comandante Shepard", "date": slot1, "time": "14:00"},
            {"teacher_id": "T002", "teacher_name": "Capitano Picard", "date": slot2, "time": "15:30"},
            {"teacher_id": "T003", "teacher_name": "Ammiraglio Adama", "date": slot3, "time": "16:30"}
        ]

    def book_consultation(self, date: str, time: str, teacher_id: Optional[str] = None) -> str:
        available = [slot for slot in self.available_slots if slot["date"] == date and slot["time"] == time]
        if teacher_id:
            available = [slot for slot in available if slot["teacher_id"] == teacher_id]

        if not available:
            return f"Nessun briefing disponibile per la data {date} alle ore {time}. Ecco gli slot liberi: {self.available_slots}"

        slot = available[0]
        return f"Briefing di orientamento confermato con {slot['teacher_name']} per il giorno {slot['date']} alle ore {slot['time']}."