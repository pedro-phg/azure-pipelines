
# azure-pipelines

**azure-pipelines** é uma biblioteca Python que permite criar, gerenciar e executar pipelines do Azure DevOps de forma programática, utilizando apenas código Python. Esta biblioteca oferece uma alternativa ao YAML, permitindo maior flexibilidade e integração com fluxos de trabalho Python.

---

## 🚀 Funcionalidades

- Criação de pipelines do Azure DevOps usando classes Python.
- Suporte a estágios, jobs e tarefas.
- Execução de scripts Python e Bash diretamente na definição do pipeline.
- Conversão de pipelines YAML existentes para classes Python.
- Organização modular de scripts para melhor gerenciamento.
- Exportação de pipelines para o formato YAML.

---

## 🛠️ Instalação

Instale a biblioteca usando `pip`:

```bash
pip install azure-pipelines
```

---

## 🗂️ Estrutura do Projeto

Ao usar a biblioteca, você pode organizar seu projeto da seguinte forma:

```
.
├── scripts/
│   ├── python/
│   │   ├── script1.py
│   │   └── script2.py
│   ├── bash/
│   │   ├── script1.sh
│   │   └── script2.sh
├── pipeline.py
└── pipeline.yml
```

---

## 📝 Exemplo de Uso

### Criando um Pipeline

```python
from azure_pipelines import Pipeline, Stage, Job, ScriptTask

# Criar pipeline
pipeline = Pipeline(name="ExemploPipeline")

# Criar estágio
stage = Stage(name="Build Stage")

# Criar job
job = Job(name="Build Job")

# Adicionar tarefa ao job
task = ScriptTask(name="Compile", script_path="scripts/bash/compile.sh")
job.add_task(task)

# Adicionar job ao estágio
stage.add_job(job)

# Adicionar estágio ao pipeline
pipeline.add_stage(stage)

# Executar pipeline
pipeline.execute()
```

### Convertendo YAML para Python

```python
from azure_pipelines import YAMLConverter

# Converter YAML para Python
pipeline = YAMLConverter.from_yaml("pipeline.yml")

# Executar pipeline convertido
pipeline.execute()
```
---

## 📚 Documentação

A documentação completa estará em breve disponível no repositório.


---

## 🌟 Contribuindo

Contribuições são bem-vindas! Siga os passos abaixo para colaborar:

1. Faça um fork deste repositório.
2. Crie um branch para sua feature/bugfix: `git checkout -b minha-feature`.
3. Envie um pull request para revisão.

---
## 🖥️ Exemplos e Demonstrações

Confira o repositório de exemplos para aprender mais sobre como usar a biblioteca em diferentes cenários.

---

## 🤝 Suporte

Se você tiver dúvidas, sugestões ou problemas, abra uma [issue](https://github.com/pedro-phg/azure-pipelines/issues) no repositório.

---

**Desenvolvido com ❤️ por Pedro Adalberto(https://github.com/pedro-phg).**
