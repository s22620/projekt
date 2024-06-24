import os
from data_loader import DataLoader
from data_analysis import DataAnalysis
from data_visualization import DataVisualization


def main():
    # Zdefiniuj absolutną ścieżkę do pliku
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '..', 'data', 'Dataset_salary_2024.csv')

    # Sprawdź czy plik istnieje
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return

    loader = DataLoader(file_path)
    data = loader.load_data()

    if data is not None:
        analysis = DataAnalysis(data)
        visualization = DataVisualization(data)

        print("Basic Statistics:")
        print(analysis.basic_statistics())

        # Example operations
        analysis.convert_categorical_to_numeric('experience_level')
        filtered_data = analysis.filter_data('job_title', 'Data Engineer')
        sorted_data = analysis.sort_data('salary_in_usd')

        # Visualizations
        visualization.plot_histogram('salary_in_usd')
        visualization.plot_scatter('experience_level', 'salary_in_usd')


if __name__ == "__main__":
    main()
