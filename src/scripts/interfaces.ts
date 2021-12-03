export interface IChatItem {
  by: "user" | "arona",
  content: string,
  hash: number,
}

export interface IMollufyOptions {
  ignoreNounLengthLimit: boolean,
  forceMollufyForPredefinedWords: boolean,
}

export interface IStoreState {
  appVersion: string,

  enableMolluImageAnimation: boolean,
  mollufyOptions: IMollufyOptions,
}
